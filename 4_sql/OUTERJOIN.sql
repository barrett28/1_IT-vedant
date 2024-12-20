USE shield;

SELECT a.ar_id, heroic_name, enemy_name FROM avengers as a
LEFT JOIN avengers_enemy as ae
ON a.ar_id=ae.ar_id; 

SELECT a.ar_id, heroic_name, enemy_name FROM avengers as a
RIGHT JOIN avengers_enemy as ae
ON a.ar_id=ae.ar_id; 

SELECT a.ar_id, heroic_name, enemy_name FROM avengers as a
JOIN avengers_enemy as ae
ON a.ar_id=ae.ar_id; -- ye inner ka query hai 

-- ------------------

SELECT a.ar_id, heroic_name, enemy_name FROM avengers as a
LEFT JOIN avengers_enemy as ae
ON a.ar_id=ae.ar_id 
UNION
SELECT a.ar_id, heroic_name, enemy_name FROM avengers as a
RIGHT JOIN avengers_enemy as ae
ON a.ar_id=ae.ar_id; 

SELECT a.ar_id, heroic_name, enemy_name FROM avengers as a
LEFT JOIN avengers_enemy as ae
ON a.ar_id=ae.ar_id 
UNION ALL
SELECT a.ar_id, heroic_name, enemy_name FROM avengers as a
RIGHT JOIN avengers_enemy as ae
ON a.ar_id=ae.ar_id; 

