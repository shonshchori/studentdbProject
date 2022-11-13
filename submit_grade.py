# This file pulls the student's grades from 'studentpersonal' table.

import db_connection

my_cursor = db_connection.mydb.cursor()


def submit_grade(student_id, course_id, year_taken, grade):
    grade_details = (student_id, course_id, year_taken, grade)
    print(grade_details)
    my_cursor.execute('''INSERT INTO studentpersonal
                        VALUES ('%s', '%s', '%s', '%s')'''
                      % grade_details)
    db_connection.mydb.commit()

columns = ['Student ID', 'Course ID', 'Year Taken', 'Grade']
# this list used in "Students.html" page.
# Places in the list:
# Student ID - 0, Course ID - 1, Course Name - 2, Credit Points - 3, Grade - 4, Year Taken - 5