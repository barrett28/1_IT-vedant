-- trigger===============
USE shield;

CREATE TABLE avenger_Audit(
	audit_id INT PRIMARY KEY AUTO_INCREMENT,
    ar_id INT,
    heroic_name VARCHAR(30),
    actions VARCHAR(30),
    action_time TIMESTAMP
);

DELIMITER //

CREATE TRIGGER log_audit_before_insert
BEFORE INSERT ON Avengers
FOR EACH ROW
BEGIN 

INSERT INTO Avengers_Audit(ar_id, heroic_name, actions, action_time)
VALUES(NEW.ar_id, NEW.heroic_name, "DATE AND TIME OF INSERTION", NOW());

END //

DELIMITER ;

SELECT * FROM Avengers;

SELECT * FROM Avengers_Audit;

INSERT INTO Avengers(ar_id, f_name, l_name, heroic_name, city)
VALUES(8, "Natasha", "Roman-off", "Black Widow", "Russia");
