CREATE TABLE `studentsdb`.`students` (
  `student_id` VARCHAR(16) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `birth_date` DATE NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `major` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE INDEX `student_id_UNIQUE` (`student_id` ASC) VISIBLE);