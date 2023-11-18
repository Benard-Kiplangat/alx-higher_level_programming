-- A script that lists all shows contained in hbtn_0d_tvshows
-- that have atleast one genre linked
SELECT gi.`name` AS genre, count(*) AS number_of_shows
FROM `tv_genres` AS gi
INNER JOIN `tv_show_genres` as gt
ON gi.`id` = gt.`genre_id`
GROUP BY gi.`name`
ORDER BY number_of_shows DESC;
