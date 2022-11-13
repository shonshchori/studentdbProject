# This file pulls the student's grades from 'studentpersonal' table.

import db_connection

my_cursor = db_connection.mydb.cursor()


def submit_course(course_id, course_name, credit_points):
    course_details = (course_id, course_name, credit_points)
    print(course_details)
    my_cursor.execute('''INSERT INTO courses
                        VALUES ('%s', '%s', '%s')'''
                      % course_details)
    db_connection.mydb.commit()
