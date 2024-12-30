-- assignment view 

USE shield;

CREATE TABLE employee (
	id INT, 
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary INT,
    dept_id INT,
    role VARCHAR(50)
);

INSERT INTO employee (id, first_name, last_name, salary, dept_id, role)
VALUES 
(1, 'Rahul', 'Sharma', 45000, 1, 'IT_PROG'),
(2, 'Pratik', 'Gajne', 67000, 2, 'ML_ENGG'),
(3, 'Naresh', 'Bhatt', 48000, 1, 'IT_PROG'),
(4, 'Nisha', 'Shetty', 65000, 1, 'IT_PROG'),
(5, 'Vishal', 'Kumar', 56000, 2, 'TESTER'),
(6, 'Niranjan', 'Pandey', 43000, 1, 'IT_PROG'),
(7, 'Simran', 'Mehta', 56000, 1, 'SUPPORT'),
(8, 'Vipul', 'Shekhawat', 67000, 2, 'SUPPORT'),
(9, 'Binay', 'Gosh', 32000, 1, 'IT_PROG'),
(10, 'Nitin', 'Rao', 54000, 2, 'TESTER');

CREATE TABLE department (
	id INT,
    dept_name VARCHAR(50)
);

INSERT INTO Department (id, dept_name)
VALUES 
(1, 'IT'),
(2, 'CS');

CREATE VIEW EmployeeView AS
SELECT e.id, e.first_name, e.last_name FROM employee AS e
WHERE role="IT_PROG";

SELECT * FROM EmployeeView;

INSERT INTO employee
VALUES (11, "Piyush", "Bansal", 52000,2,"Data Analyst");

SELECT * FROM employee;

DELETE FROM employee 
WHERE id="5";

UPDATE employee 
SET role="IT_PROGRAMMER"
WHERE role="IT_PROG";

DROP VIEW EmployeeView;

-- ========================2nd question================= 

CREATE TABLE employee(
	id INT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    salary INT,
    dept_id INT,
    role VARCHAR(30)
);

INSERT INTO employee (id, first_name, last_name, salary, dept_id, role)
VALUES 
(1, 'Rahul', 'Sharma', 45000, 1, 'IT_PROG'),
(2, 'Pratik', 'Gajne', 67000, 2, 'ML_ENGG'),
(3, 'Naresh', 'Bhatt', 48000, 1, 'IT_PROG'),
(4, 'Nisha', 'Shetty', 65000, 1, 'IT_PROG'),
(5, 'Vishal', 'Kumar', 56000, 2, 'TESTER'),
(6, 'Niranjan', 'Pandey', 43000, 1, 'IT_PROG'),
(7, 'Simran', 'Mehta', 56000, 1, 'SUPPORT'),
(8, 'Vipul', 'Shekhawat', 67000, 2, 'SUPPORT'),
(9, 'Binay', 'Gosh', 32000, 1, 'IT_PROG'),
(10, 'Nitin', 'Rao', 54000, 2, 'TESTER');

CREATE VIEW EmployeeDetails AS 
SELECT id, first_name, last_name, salary FROM employee WHERE salary> (SELECT AVG(salary) FROM employee);
SELECT * FROM EmployeeDetails;

CREATE VIEW EmployeeDet AS 
SELECT e.id, e.first_name, e.last_name, e.salary, d.dept_name AS department_name FROM employee AS e
INNER JOIN department AS d
ON e.dept_id=d.id;

SELECT * FROM EmployeeDet;

SELECT * FROM employee;


