import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

#Configure Application
app = Flask(__name__)

#load config.py
app.config.from_object('config.Config')

#configure session
session = Session()
session.init_app(app)

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

        

        