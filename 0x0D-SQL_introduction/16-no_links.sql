-- A script that lists all records that has data in a given column
SELECT `score`, `name` FROM `second_table`
WHERE `name` != "" ORDER BY `score` DESC
