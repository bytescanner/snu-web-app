from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from passlib.hash import sha256_crypt
from flask.helpers import flash
engine = create_engine('mysql+pymysql://root:0Mtadmin@localhost:3306/pythonlogin')
db=scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main-page.html")

#login form
@app.route("/login",methods=["GET","POST"])
def login():

    if request.method == "POST":
        username = request.form.get("name")
        
        password = request.form.get("password")

        usernamedata = db.execute("SELECT username FROM accounts WHERE username=:username",{"username":username}).fetchone()
        passwordata = db.execute("SELECT password FROM accounts WHERE username=:username",{"username":username}).fetchone()

        if usernamedata is None:
            flash("No username","danger")
            return render_template("login-page.html")
        else:
            for passwor_data in passwordata:
                if sha256_crypt.verify(password,passwor_data):
                    flash("you are now login","success")
                    return redirect(url_for('main-page.html'))
                else:
                    flash("incorrect password")

if __name__ =="__main__":
    app.secret_key="1234567dailywebcoding"
    app.run(debug=True)
      