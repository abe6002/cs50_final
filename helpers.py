import os
import requests
from functools import wraps
from flask import Flask, flash, jsonify, redirect, render_template, request, session

#decorates routes to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function