-- join and constraints

create database jc;
use jc;

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    dept_id INT,
    manager_id INT
);

INSERT INTO employee (emp_id, emp_name, salary, dept_id, manager_id) VALUES
(1, 'Rahul', 60000, 1, NULL),
(2, 'Priya', 55000, 1, 1),
(3, 'Amit', 58000, 2, 1),
(4, 'Sneha', 62000, 2, 2),
(5, 'Karan', 48000, 3, 2),
(6, 'Divya', 70000, 1, 3),
(7, 'Pooja', 50000, 2, 3),
(8, 'Raj', 45000, 3, 5),
(9, 'Meena', 51000, 2, 4);

create table departments(
	dept_id INT primary key,
    name VARCHAR(50)
);

insert into departments(dept_id, name)
values(1, "IT"),
(2, "HR"),
(3, "FINANCE");

select dept_id, COUNT(*) as total_employees from employee 
group by dept_id;

select dept_id, SUM(salary) from employee
group by dept_id
having sum(salary) > 150000;

select dept_id, avg(salary) as average_salary, count(*) as total_employee from employee
group by dept_id;

select e.emp_name as employee_name, d.name as dept_name from employee as e 
left JOIN departments as d 
ON e.dept_id = d.dept_id;

select e.emp_name as employee, m.emp_name as manager from employee as e join employee as m on e.manager_id = m.emp_id;