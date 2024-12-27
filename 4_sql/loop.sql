DELIMITER //

CREATE PROCEDURE printNumber()

BEGIN 

DECLARE counter INT DEFAULT 1;

print_num: LOOP
	SELECT counter;
    
IF counter >=5 THEN 
	LEAVE print_num;
END IF;

SET counter = counter+1;

END LOOP;

END //

CALL printNumber()



-- ======================== WHILE LOOP -----=================-

DELIMITER //

CREATE PROCEDURE SumNumber( OUT total_sum INT )

BEGIN

DECLARE counter INT DEFAULT 1;

SET total_sum=0;

WHILE counter<=5 DO

SET total_sum = total_sum + counter;
SET counter = counter+1;

END WHILE ;

END //

DELIMITER ;

CALL SumNumber(@total_sum);
SELECT @total_sum;


-- ============================REPEAT=========================


DELIMITER //

CREATE PROCEDURE MultiplyNumber(OUT total_mul INT )

BEGIN 

DECLARE counter INT DEFAULT 1;

SET total_mul= 1;

REPEAT
SET total_mul = total_mul*counter;
SET counter = counter+1;
UNTIL counter>=5
END REPEAT ;

END //

DELIMITER ;

CALL MultiplyNumber(@total_mul);
SELECT @total_mul;




