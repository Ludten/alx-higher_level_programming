-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT ts.title AS 'title'
FROM tv_shows AS ts
WHERE title NOT IN
(SELECT ts.title AS 'title'
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg
INNER JOIN tv_genres AS tg
ON (tg.id = tsg.genre_id AND tsg.show_id = ts.id)
WHERE tg.name = 'Comedy')
ORDER BY title ASC;
