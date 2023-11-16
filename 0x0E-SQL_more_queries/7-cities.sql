-- A script that creates the database hbtn_0d_usa and the table cities
-- state_id INT, not null and must be a FOREIGN KEY that references states id
-- states have a unique id INT autogenerated and primary key and VARCHAR name
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT PRIMARY KEY,
	state_id INT, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256));
