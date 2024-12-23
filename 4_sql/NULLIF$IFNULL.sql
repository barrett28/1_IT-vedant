USE shield;

SELECT NULLIF(city,"NYC") AS ""
FROM avengers;

SELECT IFNULL(ar_id,6)
FROM avengers_enemy;

SELECT * FROM avengers_enemy;

SELECT * FROM avengers;