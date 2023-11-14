-- A script that groups records
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score`;
