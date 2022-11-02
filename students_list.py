# This file pulls the students from 'students' table.

import db_connection

my_cursor = db_connection.mydb.cursor()

my_cursor.execute("SELECT * FROM students")
students = list()
for student in my_cursor:
    students.append(student)

columns = ["Birth date","Email","Address","Major"]