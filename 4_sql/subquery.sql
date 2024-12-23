

SELECT heroic_name FROM avengers WHERE ar_id=3;

SELECT enemy_name FROM avengers_enemy WHERE ar_id=3;

-- SINGLE SUBQUERY

SELECT heroic_name FROM avengers WHERE ar_id=(SELECT ar_id FROM avengers_enemy WHERE enemy_name="hela");


-- MULTIPLE ROW SUBQUERY

SELECT heroic_name FROM avengers WHERE ar_id IN (SELECT ar_id FROM avengers_enemy WHERE enemy_name IN ("hela","electro","armin zola"));

SELECT * FROM xx;

SELECT name, salary FROM xx WHERE salary > ANY (SELECT salary FROM xx WHERE salary IN (5,12,9));

SELECT name, salary FROM xx WHERE salary > ALL (SELECT salary FROM xx WHERE salary IN (5,12,9));