from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import students_list

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "MySecretKey"

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

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

# Students page
@app.route('/submit', methods=['GET', 'POST'])
def studentsubmit():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("StudentSubmit.html", name=name, form=form)