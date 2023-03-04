SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM studentpersonal;

DELETE FROM students WHERE id=123456789;
DELETE FROM courses WHERE id=123;
DELETE FROM studentpersonal WHERE id=313354672;

SELECT SUM(courses.creditPoints*grades.grade)/SUM(courses.creditPoints) AS TotalAvrage
FROM courses INNER JOIN studentpersonal AS grades
WHERE grades.courseId = courses.id AND grades.id = '313354672';

SELECT SUM(courses.creditPoints*grades.grade)/SUM(courses.creditPoints) AS YearlyAvrage
FROM courses INNER JOIN studentpersonal AS grades
WHERE grades.courseId = courses.id AND grades.id = '313354672' AND yearTaken ='2';