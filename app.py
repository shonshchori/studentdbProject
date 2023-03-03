from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, EmailField, IntegerField
from wtforms.validators import DataRequired, Email

import db_connection
import students_list
import gradesSheet
import submit_course
import submit_grade
import courseDetails

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
    student_id = StringField("Student ID", validators=[DataRequired()])
    submit = SubmitField("Submit")


class GradeSubmitForm(FlaskForm):
    student_id = StringField("Student ID", validators=[DataRequired()])
    # course_id = StringField("Course ID", validators=[DataRequired()])
    course_id = SelectField("Course",
                            choices=courseDetails.courses_db(), validate_choice=True)
    year_taken = SelectField("Year Taken",
                             choices=[("1", "1"), ("2", "2"),
                                      ("3", "3"), ("4", "4")], validate_choice=True)
    grade = IntegerField("Grade", validators=[DataRequired()])
    submit = SubmitField("Submit")


class CourseForm(FlaskForm):
    course_id = StringField("course ID", validators=[DataRequired()])
    submit = SubmitField("Submit")


class CourseSubmitForm(FlaskForm):
    course_id = StringField("ID", validators=[DataRequired()])
    course_name = StringField("Name", validators=[DataRequired()])
    credit_points = StringField("Credit Points", validators=[DataRequired()])
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
        new_stud = (student_id, first_name,last_name,  birth_date, email, address, major)
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

@app.route('/courses_database', methods=['GET', 'POST'])
def courses_details():
    course_id = None
    course = None
    form = CourseForm()
    # Validate Form
    if form.validate_on_submit():
        course_id = form.course_id.data
        form.course_id.data = ''
        course = courseDetails.get_course(course_id=course_id)

    return render_template("courses_database.html",
                           course=course,
                           course_columns=courseDetails.columns, form=form)

@app.route('/grade_submit', methods=['GET', 'POST'])
def grade_submit():
    student_id = None
    course_id = None
    year_taken = None
    grade = None
    form = GradeSubmitForm()
    # Validate Form
    if form.validate_on_submit():
        student_id = form.student_id.data
        course_id = form.course_id.data
        year_taken = form.year_taken.data
        grade = form.grade.data
        form.student_id.data = ''
        form.course_id.data = ''
        form.year_taken.data = ''
        form.grade.data = ''
        submit_grade.submit_grade(student_id=student_id,course_id=course_id,
                                  year_taken=year_taken, grade=grade)

    return render_template("submit_grade.html",
                           student_id=student_id, course_id=course_id,
                           year_taken=year_taken, grade=grade, form=form)


@app.route('/course_submit', methods=['GET', 'POST'])
def course_submit():
    course_id = None
    course_name = None
    credit_points = None
    form = CourseSubmitForm()
    # Validate Form
    if form.validate_on_submit():
        course_id = form.course_id.data
        course_name = form.course_name.data
        credit_points = form.credit_points.data
        form.course_id.data = ''
        form.course_name.data = ''
        form.credit_points.data = ''
        submit_course.submit_course(course_id=course_id, course_name=course_name,
                                    credit_points=credit_points)

    return render_template("submit_course.html",
                           course_id=course_id, course_name=course_name,
                           credit_points=credit_points, form=form)