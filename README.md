# Student Database Project

This project is a student database built using MySQL, Flask, and other Python libraries. It allows users to perform various actions related to students, courses, and grades, directly from a web interface.

## Automatic Database Updates

This project allows for automatic updates to the MySQL database through the web app. When a user submits a new student, course, or grade, the information is automatically added to the database. Similarly, when a user views a student's grades sheet or average, the app queries the database and retrieves the relevant information.

This feature makes it easy for users to manage the database without needing to access it directly. All changes are made through the web app, which provides a simple and intuitive interface for managing the data.


## Getting Started

Once you have the dependencies installed (Flask and mySQL connector librarys), you can run the project by executing `flask run` on the terminal:

This will start the Flask web server and you can access the application by navigating to `http://localhost:5000` in your web browser.

## Features

This project has the following features:

1. <b>Submit a new student</b> - Allows you to add a new student to the database by providing their details such as ID, name, major, and contact information.

2. <b>View students' details</b> - Allows you to view a list of all the students in the database along with their details.

3. <b>Submit a new course</b> - Allows you to add a new course to the database by providing its ID, name and credit points.

4. <b>View courses' details</b> - Allows you to view a list of all the courses in the database along with their details.

5. <b>Submit a new grade</b> - Allows you to add a new grade to the database by selecting the student, course, and grade value.

6. <b>View student's grades sheet</b> - Allows you to view a list of all the grades for a particular student.

7. <b>View student's average</b> - Allows you to view the average grade for a student either yearly or overall.

## Screenshots

Below are some screenshots of the application:

### Student Submit Page

![Student Submit Page](https://github.com/shonshchori/studentdbProject/blob/65a27af8d31d1327eca0febf0b7ce195371384f6/student%20submit.png)
| :--: |

### Grade Submit Page

![Grade Submit Page](https://github.com/shonshchori/studentdbProject/blob/65a27af8d31d1327eca0febf0b7ce195371384f6/Grade%20Submit.png)
| :--: |

### Grades Sheet Page

![Grades Sheet Page](https://github.com/shonshchori/studentdbProject/blob/65a27af8d31d1327eca0febf0b7ce195371384f6/Grades%20Sheet.png)
| :--: |

### Averages Page

![Averages Page](https://github.com/shonshchori/studentdbProject/blob/65a27af8d31d1327eca0febf0b7ce195371384f6/Averages.png)
| :--: |

### MySQL Screenshot

![MySQL Screenshot](https://github.com/shonshchori/studentdbProject/blob/65a27af8d31d1327eca0febf0b7ce195371384f6/mySQL.png)
| :--: |

## Conclusion

This project demonstrates how to build a student database using MySQL and Flask. It provides a simple interface for managing students, courses, and grades. Feel free to modify and customize the project to meet your specific needs.
