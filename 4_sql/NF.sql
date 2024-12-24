USE shield;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    enrolled_subjects VARCHAR(100),  -- This column violates 1NF
    phone_numbers VARCHAR(100)       -- This column also violates 1NF
);

-- Insert data with multiple values in the same column
INSERT INTO students (student_id, student_name, enrolled_subjects, phone_numbers)
VALUES
(1, 'John Smith', 'Math, Science, English', '123-456-7890, 987-654-3210'),
(2, 'Jane Doe', 'Science', '555-123-4567'),
(3, 'Alice Brown', 'Math, History, Physics', '789-456-1230, 321-654-9870');


SELECT * FROM students;

DROP TABLE IF EXISTS students;


CREATE TABLE students (
    student_id INT,
    student_name VARCHAR(50),
    enrolled_subject VARCHAR(50),  -- Now each row contains only one subject
    phone_number VARCHAR(15),      -- Now each row contains only one phone number
    PRIMARY KEY (student_id, enrolled_subject, phone_number)
);


INSERT INTO students (student_id, student_name, enrolled_subject, phone_number)
VALUES
(1, 'John Smith', 'Math', '123-456-7890'),
(1, 'John Smith', 'Science', '123-456-7890'),
(1, 'John Smith', 'English', '123-456-7890'),
(1, 'John Smith', 'Math', '987-654-3210'),
(1, 'John Smith', 'Science', '987-654-3210'),
(1, 'John Smith', 'English', '987-654-3210'),
(2, 'Jane Doe', 'Science', '555-123-4567'),
(3, 'Alice Brown', 'Math', '789-456-1230'),
(3, 'Alice Brown', 'History', '789-456-1230'),
(3, 'Alice Brown', 'Physics', '789-456-1230'),
(3, 'Alice Brown', 'Math', '321-654-9870'),
(3, 'Alice Brown', 'History', '321-654-9870'),
(3, 'Alice Brown', 'Physics', '321-654-9870');
