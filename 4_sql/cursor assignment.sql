CREATE DATABASE CURSOR_DB;
USE CURSOR_DB;

DELIMITER //

CREATE PROCEDURE display_employee_details()
BEGIN
    DECLARE emp_cursor CURSOR FOR 
    SELECT first_name, last_name, email, salary FROM employee;
    
    DECLARE v_first_name VARCHAR(50);
    DECLARE v_last_name VARCHAR(50);
    DECLARE v_email VARCHAR(50);
    DECLARE v_salary FLOAT;
    
    DECLARE done INT DEFAULT FALSE;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN emp_cursor;

    read_loop: LOOP
        FETCH emp_cursor INTO v_first_name, v_last_name, v_email, v_salary;
        
        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT CONCAT('Name: ', v_first_name, ' ', v_last_name, 
                      ', Email: ', v_email, 
                      ', Salary: ', v_salary) AS employee_info;
    END LOOP;

    CLOSE emp_cursor;
END//

DELIMITER ;

CALL display_employee_details();
