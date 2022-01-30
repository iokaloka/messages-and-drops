from flask import Flask
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from os import getenv

#################################################################################################################################

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

# The database URL is fetched from environmental variable in .env file.
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

# Removes the SQLAlchemy warning when the application is ran.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#################################################################################################################################

@app.route("/")
def index():
    return render_template("index.html", error="")
  
@app.route("/home")
def home():
    sql = "SELECT thread_id, content, created_at, username FROM messages ORDER BY created_at DESC"
    result = db.session.execute(sql)
    messages = result.fetchall()
    return render_template("home.html", messages=messages)
  
@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if not user:
        # Invalid username: I want the application to behave similarry if either username of password does not match.
        # This way inputting random usernames cannot be used to find out what usernames are actually stored in the database.
        return render_template("index.html", error="Wrong username or password")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            # If the credential match, we will set the username to session and redirect to home page.
            session["username"] = username
            return redirect("/home")
        else:
            # Invalid username: I want the application to behave similarry if either username of password does not match.
            # This way inputting random usernames cannot be used to find out what usernames are actually stored in the database.
            return render_template("index.html", error="Wrong username or password")
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")    

@app.route("/init_registration/<int:id>")
def init_registration(id):
    if id == 0:
        return  render_template("register.html", error="")
    elif id == 1:
        return  render_template("register.html", error="The passwords did not match!")
    else:
        return  render_template("register.html", error="User with that name already exists")

@app.route("/register", methods=["POST"])
def register():
    registration_success = False
    username_to_add = request.form["username"]
    sql_find_existing_user = "SELECT DISTINCT username FROM users WHERE username = :username_to_add";
    result = db.session.execute(sql_find_existing_user, {"username_to_add":username_to_add})
    existing_user = result.fetchone()
    already_exists = existing_user != None and existing_user[0] == username_to_add
    
    # First we make sure the 2 passwords in the form match each other
    password1 = request.form["password"]
    password2 = request.form["password2"]
    if not password1 == password2:
        return redirect("/init_registration/1")
    
    # If the user does not already exist we create it;
    if not already_exists:
        hash_value = generate_password_hash(request.form["password"])
        user_role = "USER"
        sql = "INSERT INTO users (username, password, role) VALUES (:username, :password, :role)"
        db.session.execute(sql, {"username":username_to_add, "password":hash_value, "role":user_role})
        db.session.commit()
        registration_success = True
    
    if registration_success:
        return redirect("/registration_complete")
    else:
        return redirect("/init_registration/2")
    
@app.route("/registration_complete")
def registration_complete():
    return render_template("registration_complete.html")

def new():
    return render_template("new.html")
    
@app.route("/new")
def new():
    return render_template("new.html")
    
@app.route("/create", methods=["POST"])
def create():
    topic = request.form["topic"]
    sql = "INSERT INTO polls (topic, created_at) VALUES (:topic, NOW()) RETURNING id"
    result = db.session.execute(sql, {"topic":topic})
    poll_id = result.fetchone()[0]
    choices = request.form.getlist("choice")
    for choice in choices:
        if choice != "":
            sql = "INSERT INTO choices (poll_id, choice) VALUES (:poll_id, :choice)"
            db.session.execute(sql, {"poll_id":poll_id, "choice":choice})
    db.session.commit()
    return redirect("/")
    
@app.route("/poll/<int:id>")
def poll(id):
    sql = "SELECT topic FROM polls WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT id, choice FROM choices WHERE poll_id=:id"
    result = db.session.execute(sql, {"id":id})
    choices = result.fetchall()
    return render_template("poll.html", id=id, topic=topic, choices=choices)
    
@app.route("/answer", methods=["POST"])
def answer():
    poll_id = request.form["id"]
    if "answer" in request.form:
        choice_id = request.form["answer"]
        sql = "INSERT INTO answers (choice_id, sent_at) VALUES (:choice_id, NOW())"
        db.session.execute(sql, {"choice_id":choice_id})
        db.session.commit()
    return redirect("/result/" + str(poll_id))
    
@app.route("/result/<int:id>")
def result(id):
    sql = "SELECT topic FROM polls WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT c.choice, COUNT(a.id) FROM choices c LEFT JOIN answers a " \
          "ON c.id=a.choice_id WHERE c.poll_id=:poll_id GROUP BY c.id"
    result = db.session.execute(sql, {"poll_id":id})
    choices = result.fetchall()
    return render_template("result.html", topic=topic, choices=choices)

@app.route("/search", methods=["GET"])
def search():
    query = request.args["query"]
    sql = "SELECT id, content FROM messages WHERE content LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    messages = result.fetchall()
    return render_template("search_results.html", count=len(messages), messages=messages)
    
@app.route("/send_message/", methods=["POST"])
def send_message():
    content = request.form["content"]
    thread_id = '1';
    user = session["username"]
    sql = "INSERT INTO messages (thread_id, content, created_at, username) VALUES (:thread_id, :content, NOW(), :user)"
    db.session.execute(sql, {"thread_id":thread_id, "content":content, "user":user})
    db.session.commit()
    return redirect("/home")
    
#################################################################################################################################

#@app.route("/")
#def index():
#    result = db.session.execute("SELECT content FROM messages")
#    messages = result.fetchall()
#    return render_template("index.html", count=len(messages), messages=messages) 

#@app.route("/new")
#def new():
#    return render_template("new.html")

#@app.route("/")
#def index():
#    words = ["apina", "banaani", "cembalo"]
#    return render_template("index.html", message="Welcome", items=words)
    
#@app.route("/page1")
#def page1():
#    return "This is page 1"
    
#@app.route("/page2")
#def page2():
#    return "This is page 2"
    
#@app.route("/test")
#def test():
#    content = ""
#    for i in range(100):
#        content += str(i+1) + " "
#    return content
    
#@app.route("/page/<int:id>")
#def page(id):
#    return "This is page " + str(id)
    
#@app.route("/form")
#def form():
#    return render_template("form.html")
    
#@app.route("/result", methods=["POST"])
#def result():
#    return render_template("result.html", name=request.form["name"])
    
#@app.route("/result", methods=["POST"])
#def result():
#    pizza = request.form["pizza"]
#    extras = request.form.getlist("extra")
#    message = request.form["message"]
#    return render_template("result.html", pizza=pizza,
#                                          extras=extras,
#                                          message=message)
    
#@app.route("/order")
#def order():
#    return render_template("order.html")

#@app.route("/")
#def index():
#    return "Hello there!"

#value = randint(1, 100)

#@app.route("/")
#def index():
#    return "Satunnainen luku: " + str(value)

#@app.route("/")
#def index():
#    value = randint(1, 100)
#    return "Satunnainen luku: " + str(value)    