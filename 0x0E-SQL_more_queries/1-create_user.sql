-- creates a MySQL server user user_0d_1 and grant previleges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
