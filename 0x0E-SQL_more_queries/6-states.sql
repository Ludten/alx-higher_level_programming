-- creates database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on MySQL server
CREATE IF NOT EXISTS DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT IDENTITY(1,1) UNIQUE NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
