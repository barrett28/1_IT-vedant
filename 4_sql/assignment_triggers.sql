-- Trigger assignment
USE gs;

CREATE TABLE employee(
	emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    dept VARCHAR(50),
    salary FLOAT
);

CREATE TABLE after_insert(
	emp_id INT,
    name VARCHAR(50),
    dept VARCHAR(50),
    salary float
);

CREATE TABLE AuditLog(
	employee_id INT,
    Action varchar(50)
);


INSERT INTO employee(name, dept, salary)
VALUES("jusuu", "IT", 25000),
("ugandaaa", "cashier", 22000 );

SELECT * FROM employee;

DELIMITER //

CREATE TRIGGER after_insert
AFTER INSERT ON employee
FOR EACH ROW
BEGIN

INSERT INTO after_insert(emp_id,action)
VALUES(NEW.emp_id,"employee created");

END //

DELIMITER ;

DROP TRIGGER triggersdb.after_insert;

SELECT * FROM employee;
SELECT * FROM after_insert;

INSERT INTO employee(emp_id, name, dept, salary)
VALUES(3, "sham", "automation", 900000);

DELIMITER //

INSERT INTO employee 
VALUES(1,"first", "qqq", 1212),
(8,"def", "rrr", 2222);
