CREATE TABLE xx (
    id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(20),
    salary int
);

insert INTO
    xx (name, salary)
values ('a', 1),
    ('a', 2),
    ('a', 3),
    ('a', 4),
    ('b', 5),
    ('b', 6),
    ('b', 7),
    ('b', 8),
    ('c', 9),
    ('c', 10),
    ('c', 11),
    ('c', 12),
    ('d', 13),
    ('d', 14),
    ('d', 15),
    ('d', 16);
    
SELECT * FROM xx;

SELECT name, sum(salary) FROM xx GROUP BY name;

SELECT name, sum(salary) FROM xx GROUP BY name HAVING sum(salary)>20;

SELECT distinct salary 
FROM xx
ORDER BY salary DESC 
LIMIT 1 OFFSET 1; 

-- SELECT salary FROM xx GROUP BY salary HAVING salary>10;





TRUNCATE TABLE xx; -- Clear existing data


CREATE TABLE xx_1 (
    name varchar(20),
    salary int
);
INSERT INTO xx_1 (name, salary)
VALUES
    ('a', 1), ('a', 1), ('a', 2), ('a', 2),
    ('b', 3), ('b', 3), ('b', 4), ('b', 4),
    ('c', 5), ('c', 5), ('c', 6), ('c', 6),
    ('d', 7), ('d', 7), ('d', 8), ('d', 8);
    
SELECT * FROM xx_1;

SELECT MAX(salary) AS second_highest_salary
from xx_1
WHERE salary < (SELECT max(salary) FROM xx_1);


use shield;


CREATE TABLE con(
	age INT UNIQUE,
    name VARCHAR(30) 
);

INSERT INTO con(age, name)
VALUES(3,"abc");

ALTER TABLE con
DROP constraint age;

ALTER TABLE con
DROP PRIMARY KEY;

SELECT  * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
 WHERE TABLE_NAME = 'con';


DESC con;

SELECT * FROM con;

DROP TABLE con;





