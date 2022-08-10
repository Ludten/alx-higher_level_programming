-- lists all genres of the show Dexter
SELECT tg.name as 'name'
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg
INNER JOIN tv_shows AS ts
ON (tg.id = tsg.genre_id AND tsg.show_id = ts.id)
WHERE ts.title = 'Dexter'
ORDER BY name ASC;