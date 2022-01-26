from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

# The database URL is fetched from environmental variable in .env file.
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

# Removes the SQLAlchemy warning when the application is ran.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute("SELECT content FROM messages")
    messages = result.fetchall()
    return render_template("index.html", count=len(messages), messages=messages) 

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = "INSERT INTO messages (content) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/")

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