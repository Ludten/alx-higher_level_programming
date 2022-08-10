-- list all genres not linked to the show Dexter
SELECT tg.name AS 'name'
FROM tv_genres tg
WHERE name NOT IN
(SELECT tg.name AS 'name'
FROM tv_genres tg
LEFT JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
LEFT JOIN tv_shows ts
ON tsg.show_id = ts.id
WHERE ts.title = 'Dexter')
ORDER BY name ASC;
