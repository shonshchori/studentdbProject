# This file pulls the student's grades from 'studentpersonal' table.

import db_connection

my_cursor = db_connection.mydb.cursor()


def get_grades(student_id):
    my_cursor.execute('''SELECT studentpersonal.id,courses.name, studentpersonal.courseId,
                    courses.creditPoints, studentpersonal.grade,
                    studentpersonal.yearTaken
                    FROM studentpersonal INNER JOIN courses
                    ON studentpersonal.courseId = courses.id
                      WHERE (studentpersonal.id = %s)''' % student_id)
    grades = list()
    for grade in my_cursor:
        grades.append(grade)
    return grades

columns = ['Course ID', 'Credit Points', 'Grade', 'Year Taken']
# this list used in "Students.html" page.
# Places in the list:
# Student ID - 0, Course ID - 1, Course Name - 2, Credit Points - 3, Grade - 4, Year Taken - 5