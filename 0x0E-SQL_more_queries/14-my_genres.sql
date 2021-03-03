-- import the database dump
SELECT tv_genres.name FROM tv_shows
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
