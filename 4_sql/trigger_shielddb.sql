USE shield;-- 

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
 VALUES(10,'Natashaaa','Romaaan-Off','Black Widow','Russiaa');

 -- ======= Before Delete =======
 DELIMITER //
 
 CREATE TRIGGER log_avenger_before_delete
 BEFORE DELETE ON Avengers
 FOR EACH ROW
 BEGIN
 
 INSERT INTO Avenger_Audit(ar_id,heroic_name,actions,action_time)
 VALUES(OLD.ar_id,OLD.heroic_name,'BEFORE DELETE',NOW());
 
 END //
 
 DELIMITER ;
 
 SELECT * FROM avengers;
 SELECT * FROM avenger_audit;
 
 DELETE FROM Avengers WHERE ar_id=1;
 
  -- ======= Before Update =======
 DELIMITER //
 
 CREATE TRIGGER log_avenger_before_update
 BEFORE UPDATE ON Avengers
 FOR EACH ROW
 BEGIN
 
 IF OLD.city != NEW.city THEN
 INSERT INTO Avenger_Audit(ar_id,heroic_name,actions,action_time)
 VALUES(OLD.ar_id,NEW.heroic_name,'BEFORE UPDATE',NOW());
 
 END IF;
 END //
 
 DELIMITER ;

 UPDATE Avengers
 SET city='LA'
 where ar_id=2;
 
 
SELECT * FROM Avengers;
 
 SELECT * FROM Avenger_Audit;
 
 -- ======= AFTER Delete =======
 DELIMITER //
 
 CREATE TRIGGER log_avenger_after_delete
 AFTER DELETE ON Avengers
 FOR EACH ROW
 BEGIN
 
 INSERT INTO Avenger_Audit(ar_id,heroic_name,actions,action_time)
 VALUES(OLD.ar_id,OLD.heroic_name,'AFTER DELETE',NOW());
 
 END //
 
 DELIMITER ;
 
 DELETE FROM Avengers WHERE ar_id=8;
 
 SELECT * FROM avengers;
 SELECT * FROM avenger_audit;

 
 