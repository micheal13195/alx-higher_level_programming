-- Script that creates a table unique_id on MySQL server
CREATE TABLE
	IF NOT EXISTS `unique_id`(`id` INT, `name` VARCHAR(256));
	UNIQUE `id` = 1
