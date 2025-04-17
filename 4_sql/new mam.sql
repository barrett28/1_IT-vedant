CREATE DATABASE shield;

USE shield;

USE shield;

CREATE TABLE Avengers(
	ar_id INT,
    f_name VARCHAR(30),
    l_name VARCHAR(30),
    heroicname VARCHAR(30),
    city VARCHAR(30)
);

DESC TABLE Avengers;

DESC Avengers;

SHOW TABLES;

USE sakila;

SHOW TABLES;

DESC actor;

USE shield;

INSERT INTO avengers(ar_id, f_name, l_name, heroicname, city)
VALUES(1, "Steve", "Rogers", "Captain America", "NYC") ;

DESC avengers;

SELECT * FROM avengers;

INSERT INTO avengers(ar_id, f_name, l_name, heroicname, city)
VALUES
	(2, "Tony", "Stark", "Iron Man", "NYC"),
    (3, "Thor", "Odinson", "Thor", "Asgard"),
    (4, "Peter", "Parker", "Spiderman", "Queens"),
    (5, "Scott", "Lang", "Antman", "California"),
    (6, "Stephen", "Strange", "Doctor Starnge", "Florida"),
    (7, "James", "Barnes", "Winter Soldier", "California");
    
SELECT * FROM avengers;

INSERT INTO avengers(heroicname,city, f_name, l_name, ar_id)
VALUES("Black Widow", "Russia", "Natasha", "Romanoff", 8);

SELECT * FROM avengers;

INSERT INTO avengers(ar_id, f_name, l_name)
VALUES(9, "Clint", "Barten");

SELECT * FROM avengers;

INSERT INTO avengers
VALUES(10, "Bruce", "Banner", "Hulk", "Arozina");

SELECT * FROM avengers;

INSERT INTO avengers
VALUES(11, "Wanda's", "Maximoff's", "Scarlet Witch", "NYC");

SELECT * FROM avengers;

INSERT INTO avengers
VALUES(12, 'Wanda''s', 'Maximoff\'s', "Scarlet Witch", "NYC");

SELECT * FROM avengers;

SELECT f_name, heroicname FROM avengers;

SELECT * FROM avengers
LIMIT 5;

SELECT * FROM avengers
LIMIT 3,5;

CREATE DATABASE Avenger_enemy;

USE Avenger_enemy;

CREATE DATABASE Enemy_Database;

USE Enemy_Database;

CREATE TABLE Avenger_enemy(
	ae_id INT,
    enemy_name VARCHAR(30),
    city VARCHAR(30)
);

INSERT INTO Avenger_enemy(ae_id, enemy_name, city)
VALUES(1, "Zola", "Germany");

SELECT * FROM avenger_enemy;

INSERT INTO Avenger_enemy(ae_id, enemy_name, city)
VALUES
	(2, "Loki", "Asgard"),
    (3, "Goblin", "NYC"),
    (4, "Thanos", "Titan");

SELECT * FROM avenger_enemy;

INSERT INTO Avenger_enemy(ae_id, enemy_name)
VALUES(5, "ELECTRO");

SELECT * FROM avenger_enemy;

INSERT INTO Avenger_enemy(enemy_name, ae_id, city)
VALUES("Red Skull", 6, "Vormir");

SELECT * FROM avenger_enemy;

INSERT INTO Avenger_enemy
VALUES(7, 'Dormamu''s', "Space");

SELECT * FROM avenger_enemy;

SELECT * FROM Avenger_enemy
LIMIT 3,3;

USE shield;

SELECT * FROM avengers;

DROP TABLE avengers;

create table avengers(
  ar_id int,
  f_name varchar(30),
  l_name varchar(30),
  heroic_name varchar(30),
  city varchar(30));
  
 insert into avengers(ar_id,f_name,l_name,heroic_name,city)
  VALUES(1,'Roger','Steve','Captain America','NYC'),
      (2,'Tony','Stark','Iron Man','NYC'),
  (3,'Thor','Odinson','Thor','NYC'),
  (4,'Peter','Parker','Spider-Man','NYC'),
  (5,'Scott','Lang','Ant-Man','California'),
  (6,'Stephen','Strange','Dr.Strange','Florida'),
  (7,'James','Barnes','Winter Soldier','California');
  
  SELECT * FROM avengers;
  
  SELECT * FROM avengers
  WHERE ar_id=5;
  
  SELECT * FROM avengers
  WHERE ar_id !=5;
  
 SELECT * FROM avengers
 WHERE ar_id >5;
 
  SELECT * FROM avengers
 WHERE f_name > "R";
 
SELECT * FROM avengers
 WHERE ar_id <5;
 
 SELECT * FROM avengers
 WHERE f_name < "R";  -- isme r inclide nhi karega
 
 SELECT * FROM avengers
 Where ar_id >=5;
 
 SELECT * FROM avengers
 Where f_name >="R";
 
 SELECT * FROM avengers
 Where ar_id <=5;
 
 SELECT * FROM avengers
 Where f_name <="R";   -- isme r nhi ayega (exception) 
 
  DROP TABLE avengers;

create table avengers(
  ar_id int,
  f_name varchar(30),
  l_name varchar(30),
  heroic_name varchar(30),
  city varchar(30));
 insert into avengers(ar_id,f_name,l_name,heroic_name,city)
  VALUES(1,'Roger','Steve','Captain America','NYC'),
      (2,'Tony','Stark','Iron Man', NULL),
  (3,'Thor','Odinson','Thor','NYC'),
  (4,'Peter','Parker','Spider-Man', NULL),
  (5,'Scott','Lang','Ant-Man','California'),
  (6,'Stephen','Strange','Dr.Strange','Florida'),
  (7,'James','Barnes','Winter Soldier' ,NULL); 
  
  SELECT * FROM avengers;
  
  SELECT * FROM avengers
  WHERE city IS NULL;
  
  SELECT * FROM avengers
  WHERE city IS NOT NULL;
  
  SELECT * FROM avengers
  WHERE city="NYC" AND ar_id=3;

SELECT * FROM avengers
WHERE city="NYC" OR ar_id=6;

SELECT * from avengers; 

SELECT * FROM avengers
WHERE city="NYC" OR (f_name ="Stephen" AND l_name="Strange");

SELECT * FROM avengers
WHERE city IN ("NYC", "California");

SELECT * FROM avengers;

SELECT * FROM avengers
WHERE ar_id NOT IN (2,4,7);

SELECT * FROM avengers
WHERE ar_id BETWEEN 2 AND 5;  -- ye date and number pr sahi kaam karega

SELECT * FROM avengers
WHERE f_name BETWEEN "p" AND "T";  -- isme last ka T consider nhi ayega 

SELECT * FROM avengers
WHERE ar_id NOT BETWEEN 2 and 5;

SELECT * FROM avengers
WHERE f_name NOT BETWEEN "p" and "T";    -- isme p include nhi hoga 

SELECT * FROM avengers
WHERE f_name LIKE "s%";

SELECT * FROM avengers
WHERE heroic_name LIKE "%man";

SELECT * FROM avengers
WHERE f_name LIKE "%o%";

SELECT * FROM avengers
WHERE f_name LIKE "_o%";

SELECT * FROM avengers
WHERE f_name LIKE "__o%";

SELECT * FROM avengers
WHERE f_name NOT LIKE "s%";

SELECT * FROM avengers
ORDER BY f_name DESC;

SELECT DISTINCT CITY FROM avengers;

SELECT DISTINCT CITY FROM avengers
ORDER by city;

-- --------------------------------------------------------------

USE shield;


UPDATE avengers
SET city="Mumbai"
WHERE ar_id=2;

UPDATE avengers
SET city=
	CASE 
		WHEN ar_id=1 THEN "THANE"
        WHEN ar_id=2 THEN "Kalyan"
        ELSE "INDIA"
	END;
    
DELETE FROM avengers
WHERE ar_id=5;

INSERT INTO avengers (ar_id, f_name, l_name, heroic_name, city)
value (5, "Scott", "Lang", "AntMan", "NYC");
-- ======================================

USE hospital;

CREATE TABLE employee(
	employe_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(30),
    salary FLOAT,
    hire_date DATE,
    manager_id INT,
    dept_id INT,
    FOREIGN KEY (dept_id) references depart(dept_id)
);

INSERT INTO employee(emp_name, salary, hire_date, manager_id)
VALUES("joy", 123456.45, "2024-08-22", 2);

SELECT * FROM employee;

DROP TABLE employee;

CREATE TABLE depart(
	dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(30)
);

INSERT INTO depart(dept_name)
VALUES("IT"),
("Marketing"),
("Sales");

SELECT * FROM depart;

CREATE DATABASE newdb;
USE newdb;






