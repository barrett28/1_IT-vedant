-- ==========isme work hai============

CREATE DATABASE hospital_management_sys;
USE hospital_management_sys;
-- SHOW TABLES;

CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    contact VARCHAR(15) NOT NULL,
    address TEXT
);

CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(100)
);


-- CREATE TABLE Doctors (
--     DoctorID INT AUTO_INCREMENT PRIMARY KEY,
--     FirstName VARCHAR(50) NOT NULL,
--     LastName VARCHAR(50) NOT NULL,
--     Specialty VARCHAR(50) NOT NULL,
--     ContactNumber VARCHAR(15) NOT NULL,
--     DepartmentID INT,
--     FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
-- );


create table dr_name 
(
	dr_id int auto_increment primary key,
	full_name varchar (100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

INSERT INTO dr_name(full_name, dept_id)
VALUES ("Sham Singh", 1),
("Satendra Joshi", 2),
("Mohan Rathod", 3);

SELECT * FROM dr_name;
SELECT * FROM dr_contact;

INSERT INTO dr_contact(dr_id, contact)
VALUES(1, "2154874521"),
(2,"9856325698"),
(3,8574966589);

create table dr_contact 
(
	dr_id int,
    foreign key (dr_id) references dr_name (dr_id),
    contact varchar (15) NOT NULL
);

INSERT INTO dr_contact(dr_id, contact)
VALUES(1, "2154874521"),
(2,"9856325698"),
(3,8574966589);

CREATE VIEW doctor_info AS
SELECT dr.dr_id, dr.full_name, dr.dept_id, dc.contact FROM dr_name as dr INNER JOIN dr_contact as dc ON dr.dr_id=dc.dr_id;

SELECT * FROM doctor_info;

CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    dr_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    purpose VARCHAR(255),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (dr_id) REFERENCES dr_name(dr_id)
);

CREATE TABLE bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    bill_date DATE NOT NULL,
    payment_status ENUM('Paid', 'Pending') NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

INSERT INTO departments (Dept_name, location)
VALUES 
('Cardiology', 'First Floor'),
('Orthopedics', 'Second Floor'),
('Pediatrics', 'Third Floor');

SELECT * FROM departments;

INSERT INTO patients (patient_name, Age, gender, contact, address)
VALUES
('Joy', 45, 'Male', '9876543210', '123 Elm Street'),
('Luna', 30, 'Female', '8765432109', '456 Oak Avenue'),
('Michael', 45, 'Male', '9876543210', '123 Elm Street'),
('Sarah', 30, 'Female', '8765432109', '456 Oak Avenue'),
('Aarav', 25, 'Male', '9871234567', '12 MG Road, Bengaluru'),
('Ananya', 32, 'Female', '8762345678', '45 Park Street, Kolkata'),
('David', 50, 'Male', '7653456789', '789 Pine Lane, New York'),
('Sophia', 29, 'Female', '6544567890', '101 Maple Drive, Toronto'),
('Rajiv', 40, 'Male', '5435678901', '67 Lodhi Road, Delhi'),
('Priya', 27, 'Female', '4326789012', '23 Anna Salai, Chennai'),
('Liam', 36, 'Male', '3217890123', '85 Victoria Street, London'),
('Isabella', 41, 'Female', '2108901234', '77 Queen Street, Sydney'),
('Rohan', 33, 'Male', '9876543221', '78 Residency Road, Mumbai'),
('Kiara', 28, 'Female', '8765432198', '34 Ashok Vihar, Jaipur'),
('Ethan', 38, 'Male', '7654321987', '15 Oak Lane, Los Angeles'),
('Emma', 26, 'Female', '6543219876', '89 Birch Avenue, Boston'),
('Manoj', 50, 'Male', '5432198765', '22 Civil Lines, Lucknow'),
('Neha', 35, 'Female', '4321987654', '12 Canal Road, Pune'),
('Alexander', 42, 'Male', '3219876543', '95 Thames Street, London'),
('Olivia', 29, 'Female', '2109875432', '88 Harbor Drive, Auckland'),
('Kabir', 45, 'Male', '1234567899', '16 Brigade Road, Bengaluru'),
('Simran', 31, 'Female', '9876543101', '57 Shanti Nagar, Ahmedabad');

SELECT * FROM patients;

INSERT INTO appointments (patient_id, dr_id, appointment_date, purpose)
VALUES(1,1,1,"2024-12-30","Heart Checkup"),
(2, 2, 2, "2024-12-31", "Knee pain"),
(3, 3, '2024-08-30', 'regular checkup'),
(4, 2, '2024-07-31', 'routine checkup');


SELECT * FROM appointments;

INSERT INTO bills (patient_id, amount, bill_date, payment_status)
VALUES(1, 1, 1500.00, "2024-12-30", "Paid"),
(2,2 , 2000.00, "2024-12-31", "Pending"),
(3, 150.00, '2024-08-30', 'Paid'),
(4, 200.00, '2024-07-31', 'Pending');

SELECT * FROM bills;




CREATE DATABASE hospital_management_sys;
USE hospital_management_sys;
SHOW TABLES;


-- ===============================
-- QUERIES===============================


SELECT appointment_id, purpose FROM appointments;

SELECT patient_id, patient_name, address FROM patients WHERE contact="9876543211";


SELECT * FROM patients; 

update patients SET contact="9876543222" WHERE patient_id=1;


SELECT appointment_id, purpose, patient_id FROM appointments ORDER BY appointment_id DESC;

SELECT * FROM patients LIMIT 5;

SELECT amount, amount*1.18 AS bill_after_tax FROM bills;

SELECT AVG(age) AS Average_Age FROM patients;

SELECT amount, amount-100 AS REMAINING_PAYMENT FROM bills
WHERE payment_status="PENDING";

-- SELECT p.patient_name, b.payment_status FROM patients AS p
-- INNER JOIN bills AS b
-- ON p.patient_id=b.patient_id
-- WHERE gender="female" and payment_status="pending";

select * FROM patients;

SELECT patient_name, age FROM patients 
WHERE gender="female" AND age>30; 

SELECT patient_name, age FROM patients 
WHERE gender="male" OR age>45; 

SELECT patient_name, age 
FROM patients 
WHERE NOT (gender = 'Male' OR age <= 30);

SELECT patient_id, amount
FROM bills
WHERE amount BETWEEN 100 AND 1500;

SELECT patient_id, patient_name, age FROM patients
WHERE age>45;

SELECT p.patient_id, p.patient_name, a.purpose FROM patients AS p
INNER JOIN appointments AS a
ON p.patient_id=a.patient_id
WHERE p.patient_id IN (SELECT patient_id FROM appointments WHERE appointment_id>2 );

SELECT patient_id, patient_name FROM patients 
WHERE patient_name LIKE "a%";

SELECT DISTINCT gender FROM patients;

ALTER TABLE patients
ADD COLUMN alternative_number VARCHAR(10) AFTER contact;

ALTER TABLE patients
ADD COLUMN hospital_id INT FIRST;

SELECT * FROM patients;

ALTER TABLE patients
CHANGE COLUMN hospital_id hos_id INT;

SELECT * FROM patients;

ALTER TABLE patients
MODIFY COLUMN contact VARCHAR(12);

SELECT * FROM patients;

ALTER TABLE patients
DROP COLUMN hos_id,
DROP COLUMN alternative_number;

SELECT * FROM patients;

-- UPDATE TABLE 

DELETE FROM patients
WHERE patient_id=22;

SELECT * FROM Patients;

SELECT patient_name AS full_name, contact AS Phone_number FROM patients;


SELECT CONCAT(patient_name, "-> ", address) AS patient_details FROM patients;

SELECT UPPER(patient_name) FROM patients;

SELECT SUBSTRING("patientName", 2, 5) AS SubString_Example;

SELECT patient_id, amount, ROUND(amount) AS rounded_amount
FROM bills;

SELECT patient_id, amount, SQRT(amount) AS sqrt_amount
FROM bills;

SELECT * FROM bills;

 SELECT bill_id, bill_date, YEAR(bill_date), MONTH(bill_date) FROM bills;
 
 SELECT bill_id, DAYNAME(bill_date) FROM bills;
 
 SELECT COUNT(patient_name) FROM patients;
 
 SELECT AVG(amount) AS Avg_Amount FROM bills;
 
SELECT payment_status, SUM(amount) AS grouped_amount 
FROM bills
GROUP BY payment_status;

SELECT payment_status, SUM(amount)
FROM bills
GROUP BY payment_status
HAVING SUM(amount)<2000;

ALTER TABLE patients
MODIFY contact VARCHAR(10) NOT NULL;

ALTER TABLE patients
MODIFY contact VARCHAR(15);

SELECT * FROM patients;

INSERT INTO patients(patient_name,age, gender, contact, address )
VALUES("Atharva", 20, "Male","", "Badlapur West");

DELETE FROM patients
where patient_id=23;
-- ==================================================
ALTER TABLE patients
ADD CONSTRAINT contact UNIQUE (contact);

ALTER TABLE patients
DROP CONSTRAINT contact;

-- ==================================================

SELECT  *  FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'patients';

SELECT * from appointments
CROSS JOIN bills;

SELECT * FROM dr_name AS d
INNER JOIN appointments AS a
ON d.dr_id!=a._id;

SELECT * FROM appointments
NATURAL JOIN dr_name;

SELECT b.bill_id, b.bill_date, b.amount, p.patient_name FROM bills AS b
LEFT JOIN patients AS p
ON b.patient_id=p.patient_id;

SELECT d.dr_id, d.full_name, a.appointment_id FROM dr_name AS d
RIGHT JOIN appointments AS a
ON d.dr_id = a.dr_id;

SELECT p.patient_id, p.patient_name, a.appointment_id, a.appointment_date, a.purpose FROM patients AS p
LEFT JOIN appointments AS a
ON p.patient_id = a.patient_id
UNION
SELECT p.patient_id, p.patient_name, a.appointment_id, a.appointment_date, a.purpose
FROM patients AS p
RIGHT JOIN appointments AS a
ON p.patient_id = a.patient_id;


