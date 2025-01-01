CREATE TABLE Avenger_Audit(
audit_id INT PRIMARY KEY AUTO_INCREMENT,
ar_id INT,
heroic_name VARCHAR(30),
actions VARCHAR(30),
action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

 DELIMITER //
 
 CREATE TRIGGER log_avenger_before_inserts
 BEFORE INSERT ON Avengers
 FOR EACH ROW
 BEGIN
 
 INSERT INTO Avenger_Audit(ar_id,heroic_name,actions,action_time)
 VALUES(NEW.ar_id,NEW.heroic_name,'BEFORE INSERT',NOW());
 
 END //
 
 DELIMITER ;
 
 SELECT * FROM Avengers;
 
 SELECT * FROM Avenger_Audit;
 
 INSERT INTO Avengers(ar_id,f_name,l_name,heroic_name,city)
 VALUES(8,'Natasha','Roman-Off','Black Widow','Russia');
 
 DROP TRIGGER shield.log_avenger_before_inserts;
 
 CREATE DATABASE TRIGGERSDB;
 
 USE TRIGGERSDB;
 
 CREATE TABLE Avenger_Audit(
audit_id INT PRIMARY KEY AUTO_INCREMENT,
ar_id INT,
heroic_name VARCHAR(30),
actions VARCHAR(30),
action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table avengers(
  ar_id int PRIMARY key AUTO_INCREMENT,
  f_name varchar(30),
  l_name varchar(30),
  heroic_name varchar(30),
  city varchar(30));
  

  insert into avengers(f_name,l_name,heroic_name,city)
  VALUES('Roger','Steve','Captain America','NYC'),
        ('Tony','Stark','Iron Man','NYC'),
  ('Thor','Odinson','Thor','NYC'),
  ('Peter','Parker','Spider-Man','NYC'),
    ('Scott','Lang','Ant-Man','California'),
  ('Stephen','Strange','Dr.Strange','Florida'),
  ('James','Barnes','Winter Soldier','California');

 DELIMITER //
 
 CREATE TRIGGER log_avenger_before_inserts
 BEFORE INSERT ON Avengers
 FOR EACH ROW
 BEGIN
 
 INSERT INTO Avenger_Audit(ar_id,heroic_name,actions,action_time)
 VALUES(NEW.ar_id,NEW.heroic_name,'BEFORE INSERT',NOW());
 
 END //
 
 DELIMITER ;
 
 SELECT * FROM Avengers;
 
 SELECT * FROM Avenger_Audit;
 
 INSERT INTO Avengers(ar_id,f_name,l_name,heroic_name,city)
 VALUES(8,'Natasha','Roman-Off','Black Widow','Russia');
 
 USE triggersdb;
 
 