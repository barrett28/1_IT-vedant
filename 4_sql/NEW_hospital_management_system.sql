CREATE DATABASE hospitalms;

USE hospitalms;

-- four tables patients, doctor, appointments, department, billing

show tables;

CREATE TABLE patients(
	patientid INT PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    contact VARCHAR(15) NOT NULL,
    address VARCHAR(100)
);



CREATE TABLE doctors(
	doctorid INT PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    specilaity VARCHAR(30) NOT NULL,
    contact VARCHAR(10) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

DROP TABLE doctors;
DROP TABLE department;
DROP TABLE appointments;


CREATE TABLE department(
	dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(30),
    location VARCHAR(30)
);

CREATE TABLE appointments(
	appoint_id INT AUTO_INCREMENT PRIMARY KEY,
    patientid INT NOT NULL,
    doctorid INT NOT NULL,
    appoint_date DATE NOT NULL,
    reason VARCHAR(50),
    FOREIGN KEY (patientid) REFERENCES patients(patientid),
    FOREIGN KEY (doctorid) REFERENCES doctors(doctorid)
);

CREATE TABLE bills (
	billid INT AUTO_INCREMENT PRIMARY KEY,
    patientid INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    billdate DATE NOT NULL,
    billstatus ENUM("paid", "pending"),
    FOREIGN KEY (patientid) REFERENCES patients(patientid)    
);

INSERT INTO patients(firstname, lastname, age,contact, address)
VALUES ("joy", "patel", 45, '9876543210', "Kalyan"),
("shubham", "verma", 20, "8574961230", "Thane"),
("jane", "foster", 30, "9865321245", "Pune"),
("Sham","Mahajan", 22, "8574963214", "Kalyan"),
("Yash", "Ghorpade", 22, "9638527410", "Dombivali"),
('Priya', 'Sharma', 28,  '8877665544', ' Lajpat Nagar, Mumbai'),
('Emma', 'Taylor', 35,'7766554433', 'Pine Road, London'),
('Arjun', 'Verma', 40,'6677889900', 'Brigade Road, Bangalore'),
('Sophia', 'Lopez', 25, '5566778899', 'Sunset Blvd, Los Angeles'),
('Amit', 'Desai', 60,'4455667788', '9 Shantiniketan, Ahmedabad'),
('Isabella', 'Martinez', 32, '3344556677', 'Maple Drive, Toronto'),
('Rahul', 'Singh', 20,'2233445566', 'DLF Phase 1, Gurgaon');

SELECT * FROM patients;

INSERT INTO doctors(firstname, lastname,specilaity, contact, dept_id)
VALUES("abhijeet", "sharma", "Orthopedic", 3216549871, 2),
("Suraj", "Manda", "Pediatricts", 7894561232, 3),
("Bharat", "Singh", "cardiology", 857474855,1),
("mehek", "kanchan", "dentist", 5454545454, 4);

SELECT * FROM doctors;

SELECT * FROM hospitalms;



INSERT INTO department(dept_name, location)
VALUES("cardiology", "first floor"),
("Orthopedic", "first floor"),
("Pediatrics", "second floor"),
("dentist", "third floor");

SELECT * FROM department;
SELECT * FROM patients;
SELECT * FROM doctors;

INSERT INTO appointments(patientid, doctorid, appoint_date, reason)
VALUES(1, 1, "2024-10-13", "Joint Pain"),
(3, 1, "2024-10-13", "Heavy Joint Pain "),
(2,2,"2023-12-30", "health related"),
(5,3,"2024-08-25", "Blood pressure Issue"),
(4, 4, "2024-10-13", "Tooth Pain");

SELECT * FROM appointments;

INSERT INTO bills(patientid, total_amount, billdate, billstatus)
VALUES(1, 1200.0, "2024-10-13", "Paid"),
(2, 1200.0, "2023-12-30", "Pending"),
(3, 1000.0,"2024-10-13", "paid"),
(4, 800.0,"2024-10-13", "paid"),
(5,1200.0,"2024-08-25", "pending");

SELECT * FROM bills;	

-- UPDATE bills
-- SET billstatus="dfdknk"
-- WHERE patientid=2;

USE hospitalms;

SHOW TABLEs;
