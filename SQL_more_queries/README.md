# SQL_more_queries

This project covers MySQL user management and privileges (`CREATE
USER`, `GRANT`, `SHOW GRANTS`), column constraints (`NOT NULL`,
`DEFAULT`, `UNIQUE`, `AUTO_INCREMENT`, `PRIMARY KEY`, `FOREIGN KEY`),
and multi-table queries with subqueries, `JOIN` and `LEFT JOIN`,
`GROUP BY` and aggregates.

## Tasks

| File | Description |
| --- | --- |
| 0-privileges.sql | Lists all privileges of `user_0d_1` and `user_0d_2` |
| 1-create_user.sql | Creates `user_0d_1` with all privileges |
| 2-create_read_user.sql | Creates `hbtn_0d_2` and a read-only `user_0d_2` |
| 3-force_name.sql | Creates `force_name`, `name` can't be null |
| 4-never_empty.sql | Creates `id_not_null`, `id` defaults to 1 |
| 5-unique_id.sql | Creates `unique_id`, `id` defaults to 1 and is unique |
| 6-states.sql | Creates `hbtn_0d_usa` and the `states` table |
| 7-cities.sql | Creates the `cities` table with a FK to `states` |
| 8-cities_of_california_subquery.sql | Cities of California, via subquery |
| 9-cities_by_state_join.sql | Cities and their state name, via `JOIN` |
| 10-genre_id_by_show.sql | Shows with at least one genre linked |
| 11-genre_id_all_shows.sql | All shows and their genre id (`NULL` if none) |
| 12-no_genre.sql | Shows with no genre linked |
| 13-count_shows_by_genre.sql | Number of shows per genre |
| 14-my_genres.sql | Genres of the show Dexter |
| 15-comedy_only.sql | All Comedy shows |
| 16-shows_by_genre.sql | All shows and their genres (`NULL` if none) |

## Usage

Each script is meant to be piped into the `mysql` client:

```
cat 6-states.sql | mysql -hlocalhost -uroot -p
cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
```

Tasks 10-16 require importing the `hbtn_0d_tvshows` dump first:

```
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```
