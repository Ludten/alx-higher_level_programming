-- creates database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on MySQL server
CREATE IF NOT EXIST DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXIST cities (id INT IDENTITY(1,1) UNIQUE PRIMARY KEY NOT NULL, state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
