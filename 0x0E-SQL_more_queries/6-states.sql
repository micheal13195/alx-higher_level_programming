-- scripts that create a database hbtn_0d_usa 
-- a table inside the data base name state
CREATE DATABASE
	IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE
	IF NOT EXISTS `hbtn_0d_usa`.`states` (PRIMARY KEY(`id`), `id` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(256) NOT NULL)
