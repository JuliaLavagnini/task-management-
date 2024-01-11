# app.py
import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from env import SECRET_KEY, MONGO_URI, MONGO_DBNAME

app = Flask(__name__)

app.config["MONGO_DBNAME"] = MONGO_DBNAME
app.config["MONGO_URI"] = MONGO_URI
app.secret_key = SECRET_KEY

mongo = PyMongo(app)

# Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
