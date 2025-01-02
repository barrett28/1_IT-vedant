CREATE DATABASE hoi_ms;
USE hoi_ms;

CREATE TABLE patient_name(
	patient_id INT PRIMARY KEY AUTO_INCREMENT, 
    patient_fullname VARCHAR(100),
    age INT
);

INSERT INTO patient_name(patient_fullname, age)
VALUES("Bharat Ganguly", 23);

Select * FROM patient_name;

CREATE TABLE patient_contact(
	patient_id INT ,
    foreign key (patient_id) references patient_name(patient_id),
    contact VARCHAR(100),
    address text
);

INSERT INTO patient_contact(patient_id,contact, address)
VALUES(1, 9865326598, "Kalyan West"),
(2, 9865526588, "Kalyan East");

SELECT * FROM patient_contact;

create view patients_info as

select 
	pt.patient_id,
    pt.patient_fullname,
    pc.contact,
    pc.address
    
from
	patient_name pt
    
inner join
	patient_contact pc
    
on
 pt.patient_id = pc.patient_id;
 
select * from patients_info;

insert into patient_name ( fullname, age )
values ( "Shyam Mahajan", 22 );

drop table patient_name;
drop table patient_contact;


create table dr 
( dr_id int auto_increment primary key,
full_name varchar (100),
dr_number varchar (30)
);

insert into dr ( full_name, dr_number )
values ( "Bharat Singh", "12345678, 12358997" ),
("Shyam Mahajan", "8564123657, 7452136598");

select * from dr;

create table dr_name 
(
	dr_id int auto_increment primary key,
	full_name varchar (100)
);

insert into dr_name (full_name)
values ( "Bharat singh" ),
("Shyam Mahajan");

create table dr_contact 
(
	dr_id int,
    foreign key (dr_id) references dr_name (dr_id),
    contact varchar (50)
);

insert into dr_contact (dr_id, contact)
values (1,"12345678" ),
(1,"12358997" ),
(2, "8564123657"),
(2, "7452136598");

select * from dr_contact ;

create view dr_info as

select 

	dn.dr_id,
    dn.full_name,
    dc.contact
    
from

	dr_name dn
    
inner join 
	dr_contact dc
    
on 
	dn.dr_id = dc. dr_id;
    
select full_name, contact from dr_info where full_name = "Bharat Singh";

update dr_contact
set contact = "12358999"
where contact = "12358997";


