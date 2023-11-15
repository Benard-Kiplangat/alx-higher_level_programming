-- A script that creates a table id_not_null with a unique default value for id
CREATE TABLE IF NOT EXISTS `unique_id` (
	id INT UNIQUE, name VARCHAR(256) NOT NULL);
