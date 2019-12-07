from application import app
from flask import render_template

courseData = [
    {"courseID":"101", "title":"Python", "description":"Basics of Python language", "credits":"3", "term":"Fall, Spring"},
    {"courseID":"102", "title":"Core Java", "description":"Intro to Java Programming", "credits":"4", "term":"Spring"},
    {"courseID":"103", "title":"Docker", "description":"Basics of Containerisation", "credits":"3", "term":"Fall"},
    {"courseID":"104", "title":"Angular", "description":"Intro to Angular", "credits":"3", "term":"Fall, Spring"},
    {"courseID":"105", "title":"React", "description":"Intro to React", "credits":"4", "term":"Fall"}]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)


@app.route("/courses")
def courses():
    return render_template("courses.html", courseData=courseData, courses=True)


@app.route("/register")
def register():
    return render_template("register.html", register=True)


@app.route("/login")
def login():
    return render_template("login.html", login=True)

