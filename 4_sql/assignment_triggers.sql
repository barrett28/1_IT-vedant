-- Trigger assignment

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


INSERT INTO employee(name, dept, salary)
VALUES("charat", "IT", 25000),
("uganda", "cashier", 22000 );

SELECT * FROM employee;

DELIMITER //

CREATE TRIGGER after_insert
AFTER INSERT ON employee
FOR EACH ROW
BEGIN

INSERT INTO after_insert(emp_id, name, dept, salary)
VALUES(NEW.emp_id, NEW.name, NEW.dept, NEW.salary);

END //

DELIMITER ;

DROP TRIGGER triggersdb.after_insert;

SELECT * FROM employee;
SELECT * FROM after_insert;

INSERT INTO employee(emp_id, name, dept, salary)
VALUES(3, "sham", "automation", 900000);
