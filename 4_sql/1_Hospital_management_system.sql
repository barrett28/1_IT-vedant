CREATE DATABASE hospital_management_sys;
USE hospital_management_sys;

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


CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Specialty VARCHAR(50) NOT NULL,
    ContactNumber VARCHAR(15) NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);


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
VALUES
(1, 1, '2024-12-30', 'Heart Checkup'),
(2, 2, '2024-12-31', 'Knee Pain');
SELECT * FROM appointments;

INSERT INTO bills (patient_id, amount, bill_date, payment_status)
VALUES
(1, 1500.00, '2024-12-30', 'Paid'),
(2, 2000.00, '2024-12-31', 'Pending');

SELECT * FROM bills;







