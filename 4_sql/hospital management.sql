CREATE DATABASE Hospital;

USE Hospital;

# SQL script for creating tables with relationships for Hospital Management System

-- Patients Table
CREATE TABLE Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    contact_number VARCHAR(15),
    address TEXT,
    medical_history TEXT
);

-- Doctors Table
CREATE TABLE Doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    contact_number VARCHAR(15),
    email VARCHAR(100)
);

-- Appointments Table
CREATE TABLE Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Canceled') DEFAULT 'Scheduled',
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Staff Table
CREATE TABLE Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(50),
    contact_number VARCHAR(15),
    salary DECIMAL(10, 2)
);

-- Billing Table
CREATE TABLE Billing (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    appointment_id INT,
    total_amount DECIMAL(10, 2),
    payment_status ENUM('Paid', 'Pending') DEFAULT 'Pending',
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id)
);

-- Rooms Table
CREATE TABLE Rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL,
    room_type ENUM('ICU', 'General Ward', 'Private') NOT NULL,
    status ENUM('Occupied', 'Available') DEFAULT 'Available',
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Medical Records Table
CREATE TABLE MedicalRecords (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    diagnosis TEXT,
    prescription TEXT,
    record_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Pharmacy Table
CREATE TABLE Pharmacy (
    medicine_id INT AUTO_INCREMENT PRIMARY KEY,
    medicine_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2),
    quantity_available INT,
    prescription_id INT
);

INSERT INTO Patients (first_name, last_name, date_of_birth, gender, contact_number, address, medical_history) 
VALUES 
('John', 'Doe', '1985-06-15', 'Male', '1234567890', '123 Street, City', 'No known allergies'),
('Jane', 'Smith', '1992-08-22', 'Female', '9876543210', '456 Avenue, City', 'Diabetic');

INSERT INTO Doctors (first_name, last_name, specialization, contact_number, email) 
VALUES 
('Alice', 'Johnson', 'Cardiologist', '1111111111', 'alice.johnson@example.com'),
('Bob', 'Williams', 'Neurologist', '2222222222', 'bob.williams@example.com');

INSERT INTO Staff (first_name, last_name, role, contact_number, salary) 
VALUES 
('Charlie', 'Brown', 'Nurse', '3333333333', 40000),
('Emily', 'Davis', 'Receptionist', '4444444444', 30000);

INSERT INTO Rooms (room_number, room_type, status) 
VALUES 
('101', 'ICU', 'Available'),
('102', 'General Ward', 'Available');

INSERT INTO Appointments (patient_id, doctor_id, appointment_date, appointment_time, status) 
VALUES 
(1, 1, '2024-01-15', '10:30:00', 'Scheduled'),
(2, 2, '2024-01-16', '14:00:00', 'Scheduled');

INSERT INTO Billing (patient_id, appointment_id, total_amount, payment_status) 
VALUES 
(1, 1, 500, 'Paid'),
(2, 2, 700, 'Pending');

INSERT INTO MedicalRecords (patient_id, doctor_id, diagnosis, prescription, record_date) 
VALUES 
(1, 1, 'Hypertension', 'Medication A', '2024-01-15'),
(2, 2, 'Migraine', 'Medication B', '2024-01-16');

INSERT INTO Pharmacy (medicine_name, price, quantity_available) 
VALUES 
('Medication A', 100, 50),
('Medication B', 200, 30);

SELECT medicine_name, price, quantity_available
FROM Pharmacy;


