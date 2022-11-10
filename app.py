from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, EmailField
from wtforms.validators import DataRequired, Email

import db_connection
import students_list
import gradesSheet

# Create a Flask Instance
app = Flask(__name__)

# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:7466@localhost/our_users'
# Secret Key
app.config['SECRET_KEY'] = "MySecretKey"

# Create a Form Class
class StudentForm(FlaskForm):
    student_id = StringField("ID", validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    birth_date = DateField("Birth Date", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    address = StringField("Address", validators=[DataRequired()])
    major = SelectField("Major",
                        choices=[("Industrial Engineering", "Industrial Engineering"),
                                 ("Civil Engineering", "Civil Engineering"),
                                 ("Mechanic Engineering", "Mechanic Engineering"),
                                 ("Electrical Engineering", "Electrical Engineering")], validate_choice=True)
    submit = SubmitField("Submit")


class GradesForm(FlaskForm):
    student_id = StringField("ID", validators=[DataRequired()])
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
def student_submit():
    student_id = None
    first_name = None
    last_name = None
    birth_date = None
    email = None
    address = None
    major = None
    form = StudentForm()
    # Validate Form
    if form.validate_on_submit():
        student_id = form.student_id.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        birth_date = form.birth_date.data
        email = form.email.data
        address = form.address.data
        major = form.major.data
        form.student_id.data = ''
        form.first_name.data = ''
        form.last_name.data = ''
        form.birth_date.data = ''
        form.email.data = ''
        form.address.data = ''
        form.major.data = ''

        my_cursor = db_connection.mydb.cursor()
        new_stud = (student_id, last_name, first_name, birth_date, email, address, major)
        my_cursor.execute("INSERT INTO students VALUES(%s, '%s', '%s', '%s', '%s', '%s', '%s')" % new_stud)

        db_connection.mydb.commit()
    return render_template("StudentSubmit.html",
                           student_id=student_id, first_name=first_name, last_name=last_name, birth_date=birth_date,
                           email=email, address=address, major=major, form=form)

@app.route('/grades_sheet', methods=['GET', 'POST'])
def grades_sheet():
    student_id = None
    grades = None
    form = GradesForm()
    # Validate Form
    if form.validate_on_submit():
        student_id = form.student_id.data
        form.student_id.data = ''
        grades = gradesSheet.get_grades(student_id=student_id)

    return render_template("grades_sheet.html",
                           grades=grades,
                           grade_columns=gradesSheet.columns, form=form)