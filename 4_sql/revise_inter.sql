create database reivse_inter;
use reivse_inter;

CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    dept_id INT
);

INSERT INTO employee (id, name, salary) VALUES
(19, 'juyieena', 51000);

select * from employee;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO departments (dept_id, name) VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance');

alter table departments


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


delimiter //

create procedure AllEmployee()
begin
	select * from employee;
end //

delimiter ;

call AllEmployee();


create table employeeDate(
	emp_id INT auto_increment primary key,
    name varchar(50),
    action_time timestamp default current_timestamp
);

select * from employee;
select * from employeeDate;

delimiter //

create trigger after_employee_insert
AFTER INSERT ON employee
for each row 

begin 
	insert into employeeDate( name)
    values (NEW.name);
end//

delimiter ;

drop trigger if exists after_employee_insert;

insert into employee(id, name, salary, dept_id)
values (21,"bb", 56565, 2);


select * from employee;

insert into employee(id,  name, salary)
values (21, "ajit", 23567);

select e.name, d.dept_id from employee as e 
inner join departments as d 
on e.id = d.dept_id;

SELECT e.id, e.name, d.name AS department
FROM employee e
INNER JOIN departments as d ON e.id = d.dept_id;








