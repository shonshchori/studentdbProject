# This file makes a connection with the MySQL Data Base.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="7466",
    database="studentsdb",
    auth_plugin='mysql_native_password'
)