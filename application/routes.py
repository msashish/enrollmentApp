from application import app
from application.models import User, Course, Enrollment
from application.forms import LoginForm, RegisterForm
from flask import render_template, request, Response, json, flash, redirect, url_for, session

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
    # courses_data = Course.objects.all()
    courses_data = Course.objects.order_by('course_id')
    return render_template("courses.html", courseData=courses_data, courses=True, term=term)


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get('user_id'):
        return redirect(url_for('index'))
    register_form = RegisterForm()
    if register_form.validate_on_submit():  # Only when data is entered and submitted
        """Inside validate_on_submit(): Method `validate` gets called only if the form is submitted.
           validate_on_submit() is a shortcut for ``form.is_submitted() and form.validate()``.
        """

        email = register_form.email.data
        password = register_form.password.data
        first_name = register_form.first_name.data
        last_name = register_form.last_name.data
        user_id = User.objects.count()
        user_id += 1
        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You have been successfully registered !! Login to access", 'success')
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=register_form, register=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get('user_id'):
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit(): # Only when data is entered and submitted
        email_from_form = login_form.email.data
        password_from_form = login_form.password.data
        user_document = User.objects(email=email_from_form).first()

        if user_document and user_document.get_password(password_from_form):
            flash(f"{user_document.first_name} !!, you have been successfully logged in", 'success')
            session["user_id"] = user_document.user_id
            session["user_name"] = user_document.first_name
            return redirect(url_for('index'))
        else:
            flash("Login Failed. You have to first register inorder to login", 'danger')
    return render_template("login.html", title='Login', form=login_form, login=True)


@app.route("/logout")
def logout():
    session['user_id'] = False
    session.pop('user_name', None)
    return redirect(url_for('index'))


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    # id = request.args.get('courseID')   # Works when we use method="GET" inside courses html which calls enrollment method
    # title = request.args.get('title')
    # term = request.args.get('term')
    course_id_from_form = request.form.get('course_id')
    title_from_form = request.form.get('title')
    user_id_from_session = session.get('user_id')
    # Check if course is already enrolled by this user. If not, then enroll and take him to enrollment oage
    if course_id_from_form:
        if Enrollment.objects(user_id=user_id_from_session, course_id=course_id_from_form):
            flash(f"Oops! You are already enrolled in this course {title_from_form}!", "danger")
            return redirect(url_for('courses'))
        else:
            Enrollment(user_id=user_id_from_session, course_id=course_id_from_form).save()
            flash(f"You have been successfully enrolled in {title_from_form}!", "success")
    # Fetch list of enrolled courses by this user
    enrolled_courses = list(User.objects.aggregate(*[
        {
            '$lookup': {
                'from': 'enrollment',
                'localField': 'user_id',
                'foreignField': 'user_id',
                'as': 'r1'
            }
        }, {
            '$unwind': {
                'path': '$r1',
                'includeArrayIndex': 'r1_id',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'course',
                'localField': 'r1.course_id',
                'foreignField': 'course_id',
                'as': 'r2'
            }
        }, {
            '$unwind': {
                'path': '$r2',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$match': {
                'user_id': user_id_from_session
            }
        }, {
            '$sort': {
                'course_id': 1
            }
        }
    ]))
    return render_template("enrollment.html", enrollment=True, title="Enrollment", enrolled_courses=enrolled_courses)


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if idx is None:
        jdata = Course.objects.order_by('course_id')
    else:
        jdata = Course.objects(course_id=idx)
    return Response(json.dumps(jdata), mimetype='application/json')


@app.route("/user")
def user():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    # User(user_id=1, first_name='Ashish', last_name='Sheelavantar', email='pluckyashish@gmail.com', password='1234').save()
    # User(user_id=2, first_name='Adam', last_name='Zeal', email='adam@gmail.com', password='time1234').save()
    users = User.objects.all()
    return render_template("users.html", users=users)
