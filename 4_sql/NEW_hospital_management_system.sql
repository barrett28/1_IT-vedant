CREATE DATABASE hospitalms;

USE hospitalms;

-- four tables patients, doctor, appointments, department, billing

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
    contact VARCHAR(10) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

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


