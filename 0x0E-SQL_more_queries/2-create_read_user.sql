-- create database hbtn_0d_2 and user user_0d_2
CREATE IF NOT EXIST DATABASE hbtn_0d_2;
CREATE IF NOT EXIST USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT on hbtn_0d_2.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
