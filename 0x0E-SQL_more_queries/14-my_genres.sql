--  script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

SELECT g.name AS name FROM tv_genres g WHERE g.id IN (SELECT genre_id FROM tv_show_genres WHERE show_id = (SELECT id FROM tv_shows WHERE title = "Dexter")) ORDER BY g.name;
