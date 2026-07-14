-- Student Management System Database
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no VARCHAR(20) UNIQUE NOT NULL,
    course VARCHAR(50),
    marks FLOAT
);

INSERT INTO students (name, roll_no, course, marks) VALUES
('Ali Khan', 'CS001', 'Computer Science', 85.5),
('Sara Ahmed', 'CS002', 'Software Engineering', 92.0);
