create database reivse_inter;
use reivse_inter;

CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    dept_id INT
);

INSERT INTO employee (id, name, salary, dept_id) VALUES
(1, 'Rahul', 60000, 1),
(2, 'Priya', 55000, 1),
(3, 'Amit', 58000, 2),
(4, 'Sneha', 62000, 2),
(5, 'Karan', 48000, 3),
(6, 'Divya', 70000, 1),
(7, 'Pooja', 50000, 2),
(8, 'Raj', 45000, 3),
(9, 'Meena', 51000, 2);

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO departments (dept_id, name) VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance');




select dept_id, MIN(salary), d.name from employee
JOIN departments
group by dept_id
having MIN(salary)>50000;


select  d.name, COUNT(*) as total_employee, SUM(salary) as total_salary from employee  JOIN departments as d on employee.dept_id = d.dept_id
group by d.dept_id
having count(*)>2;


select salary from employee
where salary > (select avg(salary) from employee );

select name from employee
where dept_id IN (select dept_id from departments where name IN ('IT', 'HR'));

select name, salary from employee
where salary > ANY (select salary from employee where dept_id = (select dept_id from departments where name = 'HR'));


SELECT e.name, d.name AS department_name
FROM employee e
INNER JOIN departments d ON e.dept_id = d.dept_id;

SELECT e.name, d.name AS department_name
FROM employee e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

SELECT e.name, d.name AS department_name
FROM employee e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;






