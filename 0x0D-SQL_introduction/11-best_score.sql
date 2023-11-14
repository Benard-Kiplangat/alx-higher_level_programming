-- A script that selects the best scores: those greater than or equal to 10
SELECT `score`, `name` FROM `second_table`
WHERE `score` >= 10 ORDER BY `score` DESC;
