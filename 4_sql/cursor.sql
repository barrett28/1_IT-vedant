-- cursor===================


DELIMITER //

CREATE PROCEDURE ProcessAvengerByCity(IN city_name VARCHAR(30))

BEGIN

DECLARE hero_name VARCHAR(30);
DECLARE done INT DEFAULT 0;

DECLARE avenger_cursor CURSOR FOR
SELECT heroic_name FROM Avengers WHERE city = city_name;

DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;

OPEN avenger_cursor;

heros:LOOP
 FETCH avenger_cursor INTO hero_name;
 
 IF done THEN
    LEAVE heros;
END IF;

IF hero_name= 'iron man' THEN
UPDATE avengers
SET f_name ='potts'
WHERE ar_id=2;
END IF;

IF hero_name ='thor' THEN
DELETE FROM Avengers where ar_id =3;
END IF;

IF hero_name ='Ant-man' THEN
DELETE FROM Avengers where ar_id =5;
END IF;

END LOOP;

CLOSE avenger_cursor;

END //

DELIMITER ;

DROP PROCEDURE ProcessAvengerByCity;

CALL ProcessAvengerByCity('NYC');
SELECT * FROM avengers;
USE shield;
