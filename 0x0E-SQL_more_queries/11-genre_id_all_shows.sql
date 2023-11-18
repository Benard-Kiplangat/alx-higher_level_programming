-- A script that lists all shows contained in hbtn_0d_tvshows
-- that have atleast one genre linked
SELECT gt.title, gi.genre_id FROM tv_shows AS gt
LEFT JOIN tv_show_genres AS gi
ON gt.id = gi.show_id
ORDER BY gt.title ASC, gi.genre_id ASC;
