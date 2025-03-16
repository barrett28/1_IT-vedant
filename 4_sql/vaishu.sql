create database student;
use student;


create table student_info(
	roll_no int primary key not null,
    stu_name varchar(20) not null,
    stu_address varchar(100) not null,
    stu_class varchar(10) not null
);
insert into student_info
values (101,"Bharat","kalyan","12");