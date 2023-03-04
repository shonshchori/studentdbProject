# This file pulls the student's grades from 'studentpersonal' table.

import db_connection

my_cursor = db_connection.mydb.cursor()
def get_average(student_id, year):

    my_cursor.execute('''SELECT SUM(courses.creditPoints*grades.grade)/SUM(courses.creditPoints)
               FROM courses INNER JOIN studentpersonal AS grades
               WHERE (grades.courseId = courses.id AND grades.id = %s)''' % student_id)

    stud_average = list()
    for average in my_cursor:
        stud_average.append(average)
    return stud_average


columns = ['Student ID', 'Year', 'Average']
# this list used in "Students.html" page.
# Places in the list:
# Student ID - 0, Year - 1, Average - 2.