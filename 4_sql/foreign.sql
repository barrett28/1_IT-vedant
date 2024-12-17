USE shield;

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
      
 INSERT INTO avengers_enemy(enemy_name)
VALUES('Gorr'),
	('Whiplash'),
	('zemo');
    
CREATE TABLE weapon(
	wp_id INT PRIMARY KEY AUTO_INCREMENT,
    weapon_name VARCHAR(30),
    ar_id INT,
    ae_id INT,
    FOREIGN KEY(ar_id) REFERENCES avengers(ar_id),
    FOREIGN KEY(ae_id) REFERENCES avengers_enemy(ae_id)
);

INSERT INTO weapon(weapon_name, ar_id, ae_id)
VALUES('web',4,2),
	('pym particle',5,null),
	('magic',6,3),
	('shield',1,6),
	('suit',2,7),
	('milonir',3,8),
	('vibranium Hand',null,null);
    
SELECT heroic_name from avengers WHERE ar_id = (SELECT ar_id FROM avengers_enemy WHERE enemy_name="Armin Zola");

SELECT weapon_name from weapon WHERE ar_id = (SELECT ar_id FROM avengers WHERE heroic_name="Iron Man");

SELECT * from avengers WHERE ar_id = (SELECT ar_id FROM weapon WHERE weapon_name="shield");


