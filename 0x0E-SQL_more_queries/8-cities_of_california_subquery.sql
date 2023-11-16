-- A script that lists all cities of california that can be found in hbtn_0d_usa
-- The states table contains only one record where name=California
-- Results be sorted in ascending order by cities.id
SELECT id, name FROM cities WHERE `state_id` = (
	SELECT id FROM `states` WHERE `name`=`California`)
	ORDER BY states.id ASC;
