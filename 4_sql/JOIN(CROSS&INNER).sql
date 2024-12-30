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

create table avengers_enemy(
  ae_id int PRIMARY key AUTO_INCREMENT,
  enemy_name varchar(30),
  ar_id int,
  FOREIGN KEY (ar_id) REFERENCES avengers(ar_id)
 
);                                                                                                                                                                                                                                                                                                                                                                                                                    


INSERT INTO avengers_enemy(enemy_name,ar_id)
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
		
SELECT heroic_name , enemy_name FROM avengers
CROSS JOIN avengers_enemy;

SELECT heroic_name, enemy_name from avengers as a 
INNER JOIN avengers_enemy as ae
ON a.ar_id=ae.ar_id;

SELECT heroic_name, enemy_name from avengers as a 
INNER JOIN avengers_enemy as ae
ON a.ar_id!=ae.ar_id;

SELECT heroic_name, enemy_name from avengers
NATURAL JOIN avengers_enemy;

SELECT heroic_name, enemy_name, weapon_name FROM avengers as a
INNER JOIN avengers_enemy as ae 
ON a.ar_id=ae.ar_id
INNER JOIN weapon as w
ON a.ar_id=w.ar_id;



create table weapon(
  wp_id int PRIMARY key AUTO_INCREMENT,
  weapon_name varchar(30),
  ar_id int,
  ae_id int,
  FOREIGN key(ar_id) REFERENCES avengers(ar_id),
  FOREIGN key(ae_id) REFERENCES avengers_enemy(ae_id)
  );

 insert into weapon(weapon_name,ar_id,ae_id)
  VALUES ('web',4,2),
                 ('pym particle',5,null),
                 ('magic',6,3),
                 ('shield',1,6),
              ('suit',2,7),
                ('milonir',3,8),
                ('vibranium Hand',null,null);
                
DROP TABLE avengers;
DROP TABLE avengers_enemy;