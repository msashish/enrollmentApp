from application import app
from flask import render_template, request, Response, json

courseData = [
    {"courseID":"101", "title":"Python", "description":"Basics of Python language", "credits":"3", "term":"Semister 1"},
    {"courseID":"102", "title":"Core Java", "description":"Intro to Java Programming", "credits":"5", "term":"Semister 2"},
    {"courseID":"103", "title":"Docker", "description":"Basics of Containerisation", "credits":"3", "term":"Fall"},
    {"courseID":"104", "title":"Angular", "description":"Intro to Angular", "credits":"3", "term":"Fall, Spring"},
    {"courseID":"105", "title":"React", "description":"Intro to React", "credits":"4", "term":"Fall"}]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="2020"):
    return render_template("courses.html", courseData=courseData, courses=True, term=term)


@app.route("/register")
def register():
    return render_template("register.html", register=True)


@app.route("/login")
def login():
    return render_template("login.html", login=True)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    # id = request.args.get('courseID')   # Works when we use method="GET" inside courses html which calls enrollment method
    # title = request.args.get('title')
    # term = request.args.get('term')
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment=True, data={'id': id, 'title': title, 'term': term})


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if idx is None:
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype='application/json')
