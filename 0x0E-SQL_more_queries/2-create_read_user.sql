-- creates database and a user
CREATE DATABASE IF NOT EXISTS hbtn_0D_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0D_2`.* TO 'user_0d_2'@'localhost';
