import os
import re
import qrcode

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

#Configure Application
app = Flask(__name__)

#load config.py
app.config.from_object('config.Config')

#configure session
sess = Session()
sess.init_app(app)

#configure database: #TODO

#Dashboard - #TODO
@app.route("/")
@login_required
def dashboard():

    return render_template("layout.html")


#Login Screen - #TODO
@app.route("/login", methods=["GET", "POST"])
def login():
    #Forgets old user_id
    session.clear()

    #if user submits form via POST
    if request.method == "POST":

        #ensure username was submitted
        if not request.form.get("username"):
            return None

        #ensure password was submitted
        elif not request.form.get("password"):
            return None
        
        #query database for username
        #rows = #TODO
        
        #ensures username exists and password matches input
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return None

        #creating a session for the user
        session["user_id"] = rows[0]["id"]

        #redirect to home page
        return redirect("/")

    #if user reachs login via GET
    else:
        return render_template("login.html")

#Register - registers user to use website
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        #ensure username, email, password, confirm password was submitted
        if not request.form.get("username") or not request.form.get("email") or not request.form.get("password") or not request.form.get("conf_password"):
            return None

        #ensures passwords match
        if not request.form.get("password") == request.form.get("conf_password"):

        #set variables, ensure email is in approximate email format
        username = request.form.get("username")
        email = request.form.get("email")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return None

        #query database for usernames and emails
        #TODO

        #if username or email exists, return error
        if not len(rows) == 0:
            return None

        #now that we've ensured UI is being used correctly and that the user or email doesn't already exist, we can register the account

        #salt password
        unsalted_pass = request.form.get("password")
        password = generate_password_hash(unsalted_pass, method='pbkdf2:sha256', salt_length=8)

        #create unique QR code:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(username)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('./static/qr_codes/qrcode_{username}.png')   

        #open user data base
        #insert variables into respective columns
        


    
    else:
        return render_template("register.html")


#Create Event #TODO
"""@app.route("/event", methods=["GET", "POST"])
def event():

    if request.method == "POST":

        if not request.form.get("event_name"):
            return None

        if no items on item form:
            return None

        add event to event table



    

    else:
        return render_template("create_event.html")"""

        

        