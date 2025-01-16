--  FUNCTIONS code

DELIMITER //

CREATE FUNCTION HeroNameLength(hero_name VARCHAR(30))
RETURNS INT
DETERMINISTIC

BEGIN 

RETURN CHAR_LENGTH(hero_name);

END //

DELIMITER ;

SELECT HeroNameLength("thor");


-- Function In procedure-------------------------------------

DELIMITER //

CREATE PROCEDURE HeroNameAsPerLength( IN heroic_name VARCHAR(30))

BEGIN 

DECLARE counter INT DEFAULT 1;

hero_name : LOOP
SELECT * FROM avengers WHERE ar_id=counter;
SET counter = counter+1;

IF counter>HeroNameLength(heroic_name) THEN 
	LEAVE hero_name;
END IF ;
END LOOP;

END //

DELIMITER ;

CALL HeroNameAsPerLength("thor");

USE shield;
SELECT * FROM avengers;

 -- =====================================
 
