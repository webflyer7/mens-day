create database email;
use email;
create table user_data
(
user_email varchar(70),
user_password varchar(30),
user_emailagain varchar(70),
recipient_email varchar(70),
user_message varchar(500)
);
select* from user_data;

delete from user_data where user_emailagain = "codemaster041@gmail.com";
delete from user_data where user_email = "codemaster041@gmail.com" and recipient_email = "paridivyansh7@gmail.com";