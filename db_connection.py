# This file makes a connection with the MySQL Data Base.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="7466",
    database="studentsdb",
    auth_plugin='mysql_native_password'
)

# my_cursor = mydb.cursor()
#
# my_cursor.execute("INSERT INTO students VALUES('123456789', 'Check', 'Checkidi',"
#                   "'1995-01-01', 'thisischeck@gmail.com', 'Checks, Israel', 'Mechanic Engineering')")
#
# mydb.commit()
