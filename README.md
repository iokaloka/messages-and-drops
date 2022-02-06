# Messages and drops

## Update 6.2.2022
The week has been everything else but porductional. CoVid-19 found it's way to the house and my decreaded physical condition has highly affected the amount of work I have been able to to. I did some designs and edited the home page of the application more to it's intended form. Tomorrow (hopefully) I start to work with the **threads**.

## Update 30.1.2022
Right. Things have started to fall into place even though there is more to do than there is time available.
- The application is running in Heroku.
    - Any one is free to go and test/use it as they will at: https://messages-and-drops.herokuapp.com/
    - Just create an account for yourself, login and start sending messages to the main thread that is currently the only one available.
- There are still no proper security means taken into use. No input sanitation, no CSF countermeasures etc. I did implement the registration so that only one account with a certain name can be created. During registration you are asked to input your password of choise twice to help you get it right. The system **does not** give information which one, the username or password is wrong during the login process.
- I have base templates for many features, but I intend to work one part at a time so it might seem there are a lot of un-used and unnecessary files/code in the project. That is actually true but we'll see how things shape up on the upcoming weeks.

Accomplishments this week:
- Registration
- Login
- Home page / main thread view.
- Sending messages to main thread.
- Searching messages
- Projects github and README.md are up to date
- Project is running on Heroku and Herokus repository is up to date.

Coming up next:
- Creation of threads
- Deletion of messages
- Deletion of threads
- Some ADMIN functionality
- Probably the first drops.
- Limited thread access rights
- ...

---

## Background

So, the idea of having to design a application as an excercise has not become too comfortable to me yet. I have always been pretty eager to create my own apps and projects, but the lack of free time kind of suppresses me. The situation is the same even now, as I work 4 days a week and try to complete some studies at the same time.

So here are the two factors to consider:
- How to decide on a subject that is simple enough so that I have enough time and resources to complete it along with everything else?
- How to sill choose a subject that is both generally beneficial to learn and a bit innovative at the same time?

Since application development is somewhat creative process and thus has characteristics of art as well, I may choose a pretty simple and useful application to hone my skills as a developer, and just add my own twist there so it become unique.

## Application idea
I will create a discussion application mentioned in the courses example applications. I think different kinds of message/image boards are still pretty solid part of internet and I have always considered them useful.

### The twist:
I will add a mini-game to the software. Basic use of the program will randomly reward resources used to play. The idea behind this is to encourage users to be active on the application. The game will not be anything too fancy, maybe text-based role play battles, stats are determined by items (maybe cards) received by using the application.

This should not be too complicated or time consuming to create and yet the application will have a bit of depth. To be honest, I maybe overestimating my capabilities or misevaluating how much there is to do, but at least now I have a direction to proceed in.

---
## Key features
- The user needs to be able to log in to the application with their personal credentials. I will probably not implement any MFA-features at least in the beginning. I will try to retain from asking user for their email addresses or any other personal data as then I would have to take GDPR in consideration. Therefore:
    - Users will create a new account for themselves simply by giving a password and a unique username.
    - Having the system inform about taken usernames is not necessary the best practise especially in terms of security, but so far I have no ideas while not using email-addresses.
    - Not having personal information stored naturally limits my options for example in regards of password recovery and such features. If someone indeed comes to me filled by misery and sadness towards their lost account, I promise to give another tought for this.
    - Ofc even messages sent to the system can be considered personal data, but I will somehow handle this in terms of use.
- I will initially have 2 levels of permissions. Developer role and users. All users will have equal permissions within the system. Users will have administrative permissions regarding their own posts and their own messaging threads. 
    - The hierarchy here will be so that a developer role may administrate basically everything. Illegal or application user term breaking content must be possible to be removed by developer. Inappropriate use of the application will result in deletion of the user account along with all content tied to them. If this is not to keep the application and it's database clean of anything suspicious, the application will be stopped and not taken into use until preventive actions have been taken to use and developer so decides. Developer may do some DevOps work within the application to fix and investigate issues of malfunctions.
    - Users will have administrative permissions regarding the messaging chains/threads created by them. The users may delete posts within the thread or the thread itself. Users may edit the threads information to some extent. Users will be able to restrict access to their threads for all others than developers.
    - Users will have administrative access regarding their posts. Users may edit or delete their own posts.
- Users may send posts: These posts may be individual ones, or answers to another posts. These posts may be visible on general post channel, or on separate threads. The posts may include text (and/or images if I feel like it)
- Users may create threads/message chains. There threads may have varying access for different users.
- Each user has their individual numeric profile stats. These stats will be something like:
    - Health
    - Strength
    - Defense
    - Accuracy
    - Evasion
    - Luck
- These stats can be manipulated by editing a card hand that has room for x cards.
- The cards may be randomly acquired by using the application. The idea is to encourage the use of the application with a "prize system".
- I will add a possibility to challenge a constantly stronger AI-encounter. The battle itself will probably be just a simple loop of actions taken in turn and the profile / encounter stats making the difference and deciding the outcome. Winning an encounter will increase the card hand size.
- I will probably restrict the interval how often this kind of encounter can be taken.
- In other words, users will use the messaging board application and gain a random collection of cards that can be used to enhance the profiles propability of winning increasingly difficult AI-enemies.
---

Please note that the above mentioned spec is not final in any way and will more than likey chance during the process.

---



