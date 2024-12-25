DELIMITER //

CREATE PROCEDURE AvengerAssemble()
BEGIN

DROP TABLE IF EXISTS avengers;

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
 
  SELECT * FROM Avengers;
 
  END //
 
DELIMITER ;

CALL AvengerAssemble();

  -- ========================================

DELIMITER //

CREATE PROCEDURE GetAvengerByCity( IN city_name VARCHAR(30))
BEGIN

SELECT * FROM avengers WHERE city= city_name;

END //

DELIMITER ;

CALL GetAvengerByCity("NYC");


-- ==================================


DELIMITER //

CREATE PROCEDURE CountAvengerInCity( IN city_name VARCHAR(30), OUT avenger_count INT)
BEGIN

SELECT COUNT(*) INTO avenger_count FROM avengers WHERE city=city_name;

END //

DELIMITER ;

CALL CountAvengerInCity("california", @avenger_count);
SELECT @avenger_count;


-- =============================

DELIMITER //

CREATE PROCEDURE UpdateHeroicName(INOUT hero_name VARCHAR(30))

BEGIN 

SET hero_name = CONCAT("I am ",hero_name);

END //

DELIMITER ;

SET @hero_name = "Iron Man";
CALL UpdateHeroicName(@hero_name);
SELECT @hero_name;
