create database revise;
use revise;

create table employee(
  id INT PRIMARY KEY,
  name VARCHAR (50),
  department VARCHAR(50),
  salary INT,
  joining_date DATE
);

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