# This file pulls the student's grades from 'studentpersonal' table.

import db_connection

my_cursor = db_connection.mydb.cursor()


def submit_grade(student_id, course_id, year_taken, grade):
    grade_details = (student_id, course_id, year_taken, grade)
    my_cursor.execute('''INSERT INTO studentpersonal
                        VALUES ('%s', '%s', '%s', '%s')'''
                      % grade_details)
    db_connection.mydb.commit()