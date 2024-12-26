USE shield;


-- ---------------------if =-------------------------

DELIMITER //

CREATE PROCEDURE CheckIfExists( IN city_name VARCHAR(30), OUT message VARCHAR(100))

BEGIN

DECLARE avenger_count INT;

SELECT COUNT(*) INTO avenger_count FROM avengers WHERE city=city_name;

IF avenger_count>0 THEN 
	SET message ="Avenger exists in the city";
END IF;

END //

DELIMITER ;

CALL CheckIfExists("NC", @message);
SELECT @message;

 
-- ------------------------------------if else----------------------

DELIMITER //

CREATE PROCEDURE CheckIfExists2( IN city_name VARCHAR(30), OUT message VARCHAR(100))

BEGIN 

DECLARE avenger_count INT;

SELECT COUNT(*) INTO avenger_count FROM avengers WHERE city=city_name;

IF avenger_count>0 THEN 
	SET message='EXISTS';
ELSE
	SET message="DOES NOT EXISTS";
END IF;

END //

DELIMITER ;

CALL CheckIfExists2("NYC", @message);
SELECT @message	;


-- ---------------------if then else if then ----------------------


DELIMITER //

CREATE PROCEDURE CheckIfExists3( IN city_name VARCHAR(100), OUT message VARCHAR(100))

BEGIN 

DECLARE avenger_count INT;

SELECT COUNT(*) INTO avenger_count FROM avengers WHERE city=city_name;

IF avenger_count>2 THEN 
	SET message="Avenger activity is high";
ELSEIF avenger_count BETWEEN 1 AND 2 THEN 
	SET message="Avenger activity is Moderate";
ELSE 
	SET message="DOES NOT EXISTS";
END IF;

END //

DELIMITER ;

CALL CheckIfExists3("california", @message);

SELECT @message;


-- ----------------------------CASE--------------

DELIMITER //

CREATE PROCEDURE CheckIfExists4( IN city_name VARCHAR(100), OUT message VARCHAR(100))

BEGIN 

DECLARE avenger_count INT;

SELECT COUNT(*) INTO avenger_count FROM avengers WHERE city=city_name;

CASE 
WHEN avenger_count>2 THEN 
	SET message="Avenger activity is high";
WHEN avenger_count BETWEEN 1 AND 2 THEN 
	SET message="Avenger activity is Moderate";
ELSE 
	SET message="DOES NOT EXISTS";
END CASE;

END //

DELIMITER ;

CALL CheckIfExists4("california", @message);

SELECT @message;




