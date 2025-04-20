create database revise;
use revise;

create table employee(
  id INT PRIMARY KEY,
  name VARCHAR (50),
  department VARCHAR(50),
  salary INT,
  joining_date DATE
);


insert into employee(id, name, department, salary, joining_date, email)
values(6, "Amit", "Sales", 410000, "2023-02-15", "amit@gmail.com");

update employee
set dept_id = 3
where id = 6;

update employee
set dept_id = 1
where department = "IT";

update employee
set dept_id = 2
where department = "HR";

update employee
set dept_id = 3
where department = "Sales";

update employee
set dept_id = 4
where department = "Finance";

select * from employee;


insert into employee(id, name, department, salary, joining_date)
values(1, "Rahul", "IT", 60000, "2020-01-15"),
(2, "Priya", "HR", 50000, "2021-03-22"),
(3, "Amit", "IT", 55000, "2019-07-30"),
(4, "Shreya", "Finance", 65000, "2018-11-10"),
(5, "Karan", "Sales", 48000, "2022-05-18");

select name , department 
from employee
where salary>50000; 

select * from employee
order by joining_date ;

update employee
set salary = 52000
where name = "Priya";

select * from employee;

delete from employee
where id = 5;

select DISTINCT department from employee;

create table departments(
	dept_id INT,
    name VARCHAR(50)
);

alter table departments
add primary key (dept_id);

alter table departments
drop foreign key fk_employee;

alter table departments
drop column id;

select * from departments;

alter table employee
add column dept_id INT,
add constraint fk_deptid
foreign key (dept_id) references departments(dept_id);

select * from employee;




alter table departments change column id dept_id INT (20);

select * from departments;

insert into departments(id, name)
values(1, "IT"),
(2, "HR"),
(3, "Finance"),
(4, "Sales");

select e.name, d.name from employee as e
inner join departments as d 
on e.department = d.name;


select department, avg(salary) as average_salary from employee 
group by department;

select department, avg(salary) as average_salary from employee
group by department
having avg(salary)>55000;

select name, salary from employee 
where salary > (select avg(salary) from employee); 

select avg(salary) from employee;


select name, salary from employee
where department IN ("IT", "HR") 
and salary between 50000 and 60000 
and (name like "P%" or "R%");

select name, salary, 
	case 
		when salary >= 60000 then 'High'
        when salary between 50000 and 59999 then 'Medium'
        when salary <= 50000 then 'Low'
	end as salary_grade
from employee;


alter table employee 
modify column email varchar(50) NOT NULL;

update employee
set email="hcbd@hbk.com" where name="Rahul";

update employee 
set email=null
where name="Rahul";

UPDATE employee SET email = 'rahul@example.com' WHERE name = 'Rahul';
UPDATE employee SET email = 'priya@example.com' WHERE name = 'Priya';
UPDATE employee SET email = 'amit@example.com' WHERE name = 'Amit';
UPDATE employee SET email = 'shreya@example.com' WHERE name = 'Shreya';


select * from employee;

select d.name , AVG(e.salary) AS average_salary 
from departments as d
join employee as e on d.dept_id = e.dept_id
group by e.department;

SELECT d.name AS department, AVG(e.salary) AS average_salary
FROM departments AS d
JOIN employee AS e ON d.dept_id = e.dept_id
GROUP BY d.name;






