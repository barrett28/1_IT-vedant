
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    manager_id INT
);

INSERT INTO
    employees (
        employee_id,
        employee_name,
        manager_id
    )
VALUES (1, 'John Doe', 3),
    (2, 'Jane Smith', 1),
    (3, 'Alice Johnson', NULL),
    (4, 'Bob Brown', 2),
    (5, 'Emily White', 2);


SELECT * from employees;

DROP TABLE employees;

SELECT e.employee_name as Employee ,m.employee_name as Manager FROM employees as e
INNER JOIN employees as m ON e.manager_id = m.employee_id;