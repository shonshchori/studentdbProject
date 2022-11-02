from flask import Flask, render_template, request

import students_list

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
    return render_template("index.html")

# localhost:5000/user/shon
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"), 500

# Students page
@app.route('/students')
def students():
    return render_template("students.html", students=students_list.students, columns=students_list.columns)

