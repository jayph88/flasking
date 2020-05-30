from flask import render_template, request, Response, json

from application import app, db


course_data = [
        {"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
        {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4,
         "term": "Spring"},
        {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": 3,
         "term": "Fall"}, {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": 3,
                           "term": "Fall, Spring"},
        {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4,
         "term": "Fall"}]


@app.route("/home")
@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", index=True)


@app.route("/courses/<year>")
@app.route("/courses")
def courses(year="2020"):
    return render_template("courses.html", course_data=course_data, courses=True, year=year)


@app.route("/register")
def register():
    return render_template("register.html",  register=True)


@app.route("/login")
def login():
    return render_template("login.html", login=True)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    # for get
    # requests.args
    course_id = request.form.get('course_id')
    course_title = request.form.get('course_title')
    course_description = request.form.get('course_description')
    data = {"id" : course_id, "course_title": course_title, "course_description":course_description }
    return render_template("enrollment.html", data=data)


@app.route("/api")
@app.route("/api/<idx>")
def api(idx=None):
    if idx:
        jdata = course_data[int(idx)]
    else:
        jdata = course_data

    return Response(response=json.dumps(jdata), mimetype="application/json")


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=50)
    password = db.StringField(max_length=50)


@app.route("/students")
def students():
    # User(user_id=1, first_name="Jayant", last_name="Fegade", email="jay.ph88@gmail.com", password="abcd").save()
    # User(user_id=2, first_name="Sanjana", last_name="Patil", email="s.p@gmail.com", password="abcd").save()
    user=User.objects.all()
    return render_template("students.html", user=user)