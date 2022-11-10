# This file pulls the student's grades from 'studentpersonal' table.

import db_connection

my_cursor = db_connection.mydb.cursor()


def get_course(course_id):
    my_cursor.execute("SELECT * FROM courses WHERE (id = %s)" % course_id)
    course = list()
    for item in my_cursor:
        course.append(item)
    return course

columns = ['Course Name', 'Credit Points']

print(get_course(4210110))
# this list used in "Students.html" page.
# Places in the list:
# Course Name - 0, Credit Points - 1