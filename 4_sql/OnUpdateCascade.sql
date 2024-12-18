CREATE TABLE avengers(
	ar_id INT PRIMARY KEY AUTO_INCREMENT,
    f_name VARCHAR(30),
    l_name VARCHAR(30),
    heroic_name VARCHAR(30),
    city VARCHAR(30)
);

INSERT INTO avengers(f_name, l_name, heroic_name, city)
 VALUES('Roger','Steve','Captain America','NYC'),
  ('Tony','Stark','Iron Man','NYC'),
  ('Thor','Odinson','Thor','NYC'),
  ('Peter','Parker','Spider-Man','NYC'),
    ('Scott','Lang','Ant-Man','California'),
  ('Stephen','Strange','Dr.Strange','Florida'),
  ('James','Barnes','Winter Soldier','California');
  
SELECT * FROM avengers;

CREATE TABLE avengers_enemy(
	ae_id INT PRIMARY KEY AUTO_INCREMENT,
    enemy_name VARCHAR(30),
    ar_id INT,
    FOREIGN KEY (ar_id) REFERENCES avengers(ar_id)
    ON UPDATE CASCADE
);

INSERT INTO avengers_enemy(enemy_name, ar_id)
VALUES('Armin Zola',1),
     ('Doctor octopus',4),
      ('Dormammu',6),
      ('Electro',4),
      ('Green Goblin',4),
      ('Red Skull',1),
      ('Obadiah Stane',2),
      ('Hela',3);
      
UPDATE avengers
SET ar_id=14
WHERE ar_id = 4;

SELECT * FROM avengers;
SELECT * FROM avengers_enemy;
      
DROP TABLE avengers;

DROP TABLE avengers_enemy;