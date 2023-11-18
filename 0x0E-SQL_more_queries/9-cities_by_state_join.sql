-- A script that list all cities contained in hbtn_0d_usa
-- Should display as cities.id - cities.name - states.name
-- Sorted in ascending order using cities.id
SELECT `cities`.`id`, `cities`.`name`, `states`.`name` 
FROM states INNER JOIN cities
ON states.id = cities.state_id
ORDER BY cities.id ASC;
