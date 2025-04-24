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

SELECT d.name AS department, AVG(e.salary) AS average_salary
FROM departments AS d
JOIN employee AS e ON d.dept_id = e.dept_id
GROUP BY d.name;

-- =================== stored procedure 


DELIMITER //

create procedure ShowAllEmployee()
begin 
select * from employee;
end //
DELIMITER ;

CALL ShowAllEmployee();

DELIMITER //

create procedure GetHighPaidEmployees()
begin
	select * from employee where salary > 500000;
end //

delimiter ;

call GetHighPaidEmployees();

drop procedure if exists GetHighPaidEmployees;

-- ================== variable

delimiter //

create procedure ShowBonus()

begin
	DECLARE base_salary INT DEFAULT 50000;
    DECLARE bonus INT;
    
    SET bonus = base_salary * 0.1;
    
    select base_salary as Base_Salary , bonus AS Bonus_amount;

end //

delimiter ;

call ShowBonus();

-- ===================================
delimiter //

create procedure GetEmployeeCount()

begin 
	DECLARE total_count INT;
	
    SELECT COUNT(*) INTO total_count from employee;
    
    SELECT total_count;

end//

delimiter ;

call GetEmployeeCount();

drop procedure if exists GetEmployeeCount;


-- ======================== session variable

delimiter //

create procedure MinSalary()
begin 
	SET @min_salary = 60000;
    
    SELECT salary from employee where salary > @min_salary;
    
    select salary;

end //

delimiter ;

call MinSalary;

drop procedure MinSalary;


delimiter //
create procedure checkGreater(IN varCheck INT)
begin 
    set @currAmount = 5000;
    
    if varCheck > @currAmount then 
		select "HIgh" as levelRange;
	else
		select "Low" as levelRange;
	end if;
end //
delimiter ;

call checkGreater(2000);
drop procedure if exists checkGreater;
-- ====================================== parameter 

delimiter //

create procedure EmployeeAboveSalary(IN min_sal INT)

begin 
	select salary from employee where salary > min_sal;
end // 

delimiter ;

call EmployeeAboveSalary(60000);


-- =========================== if else 

delimiter //
create procedure CheckSalaryLevel(IN sal INT)
begin 

	if sal < 50000 then 
		select "Low" as level;
	elseif sal between 50000 and 59999 then 
		select "Medium" AS level;
	else
		select "High" as level; 
	end if;
    

end //

delimiter ;

call CheckSalaryLevel(51000);

drop procedure if exists CheckSalaryLevel;

call CheckSalaryLevel()

-- ================================ loop 

delimiter //

create procedure SimpleLoop()

begin
	declare x INT default 1;
	
    loop_label: LOOP
		if x>5 then 
			leave loop_label;
		end if;
        
        select x;
        set x = x+1;
	end loop loop_label;

	
end // 
 delimiter ;
 
 call SimpleLoop;
 
 
 
 delimiter //
 
 create procedure WhileLoop()
 
 begin
	declare x INT default 1;
    
    while x <= 5 do
		select x;
        set x = x+1;
	end while;

 end //
 
 delimiter ;
 
 call WhileLoop;
 
 
 delimiter //
 
 create procedure repeatLoop()
 
 begin 
	declare i INT default 1; 	
    
    repeat 
		select i;
        set i = i + 1;
	until i > 5
    end repeat;
 
 end //
 
 delimiter ;
 
 call repeatLoop;


delimiter //

create procedure CountToN( IN n INT)

begin 
	declare i int default 1;
    
	while i <=n do
		select i;
        set i = i + 1;
	end while;

end //

delimiter ;
call CountToN(10);
drop procedure CountToN;


-- ======================= cursor 


delimiter //

create procedure ExampleCurosr()
begin

	declare done INT default FALSE;
    DECLARE emp_name VARCHAR(50);
    
    -- cursor declare 
    declare emp_cursor cursor for select name from employee;
    
    -- handle no more rows ko 
    declare continue handler for not found set done = TRUE;
    
    -- open cursor
    OPEN emp_cursor;
    
    read_loop : LOOP
		fetch emp_cursor INTO emp_name;
        
        if done then
			leave read_loop;
		end if;
        
        select emp_name;
	end loop;
    
    close emp_cursor;

end //

delimiter ;
call ExampleCurosr;


delimiter //
create procedure nameExample()
begin 
	declare done INT default FALSE;
    declare emp_name VARCHAR(50);
    
    -- declare cursor 
    declare emp_cursor cursor for select salary from employee where salary > 50000;
    
    -- handler 
    
    declare continue handler for not found set done = TRUE;
    
    -- open cursor 
    OPEN emp_cursor ;
    
    reading_loop : LOOP
		fetch emp_cursor into emp_name;
        
        if done then 
			leave reading_loop;
		end if;
        
        select emp_name;
        
	end loop;
    
    close emp_cursor;

end //
delimiter ;
call nameExample;


-- triggers

create table employee_log(
	log_id int auto_increment primary key,
    name varchar(50),
    action_time timestamp default current_timestamp
);

delimiter //

create trigger after_employee_insert
AFTER INSERT ON employee
for each row 

begin 
	insert into employee_log(name)
    value(NEW.name);

end //

delimiter ;

select * from employee;
select * from employee_log;
insert into employee(id, name, department, salary, joining_date, email, dept_id)
value(7, "ashish", "HR", 700000, "2023-03-15", "ash@gmail.com", 2);


create table employee_delete_log(
name VARCHAR(50), 
curr_time timestamp default current_timestamp
);

drop table employee_delete_log;

delimiter //
create trigger before_employee_delete
BEFORE DELETE on employee
for each row 

begin 
	insert into employee_delete_log(name)
    values(OLD.name);

end //

delimiter ;

delete from employee where id = 2;
select * from employee;
select * from employee_delete_log;

-- DROP TRIGGER [IF EXISTS] trigger_name;

--  -----fucntions

delimiter //
create function CalculateBonus(sal INT)
returns INT
deterministic

begin 
	return sal * 0.1;
end //

delimiter ;

select name, salary, CalculateBonus(salary) as bonus from employee;


select * from employee;
select * from departments;


SELECT name 
FROM employee
WHERE dept_id IN (
    SELECT dept_id FROM departments WHERE name IN ('IT', 'HR')
);