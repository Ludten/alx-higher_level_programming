# SQL - More queries
> Each file in this repository holds code that illustrates MySQL Queries
> specific to the SQL programming language

## Description of what each file shows:
* 0-privileges.sql: script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).

* 1-create_user.sql: A script that creates the MySQL server user `user_0d_1`.

	- `user_0d_1` should have all privileges on your MySQL server
	- The `user_0d_1` password should be set to `user_0d_1_pwd`
	- If the user `user_0d_1` already exists, your script should not fail

* 2-create_read_user.sql: A script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

	- `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
	- The `user_0d_2` password should be set to `user_0d_2_pwd`
	- If the database `hbtn_0d_2` already exists, your script should not fail
	- If the user `user_0d_2` already exists, your script should not fail

* 3-force_name.sql: A script that creates the table `force_name` on your MySQL server.

	- `force_name` description:
		- `id` INT
		- `name` VARCHAR(256) can’t be null
	- The database name will be passed as an argument of the `mysql` command
	- If the table `force_name` already exists, your script should not fail

* 4-never_empty.sql: A script that creates the table `id_not_null` on your MySQL server.

	- `id_not_null` description:
		- `id` INT with the default value 1
		- `name` VARCHAR(256)
	- The database name will be passed as an argument of the `mysql` command
	- If the table `id_not_null` already exists, your script should not fail

* 5-unique_id.sql: A script that creates the table `unique_id` on your MySQL server.

	- `unique_id` description:
		- `id` INT with the default value `1` and must be unique
		- `name` VARCHAR(256)
	- The database name will be passed as an argument of the `mysql` command
	- If the table `unique_id` already exists, your script should not fail

* 6-states.sql: A script that creates the database `hbtn_0d_usa` and the table states (in the database `hbtn_0d_usa`) on your MySQL server.

	- states description:
		- `id` INT unique, auto generated, can’t be null and is a primary key
		- `name` VARCHAR(256) can’t be null
	- If the database `hbtn_0d_usa` already exists, your script should not fail
	- If the table `states` already exists, your script should not fail

* 7-cities.sql: A script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.

	- `cities` description:
		- `id` INT unique, auto generated, can’t be null and is a primary key
		- `state_id` INT, can’t be null and must be a `FOREIGN KEY` that references to `id` of the `states` table
		- `name` VARCHAR(256) can’t be null
	- If the database `hbtn_0d_usa` already exists, your script should not fail
	- If the table `cities` already exists, your script should not fail

* 8-cities_of_california_subquery.sql: A script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

	- The `states` table contains only one record where `name` = `California` (but the `id` can be different, as per the example)
	- Results must be sorted in ascending order by `cities.id`
	- You are not allowed to use the `JOIN` keyword
	- The database name will be passed as an argument of the `mysql` command

* 9-cities_by_state_join.sql: A script that lists all cities contained in the database `hbtn_0d_usa`.

	- Each record should display: `cities.id` - `cities.name` - `states.name`
	- Results must be sorted in ascending order by `cities.id`
	- You can use only one `SELECT` statement
	- The database name will be passed as an argument of the `mysql` command

* 10-genre_id_by_show.sql: Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

  A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

* 11-genre_id_all_shows.sql: Import the database dump of `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `10-genre_id_by_show.sql`)

  A script that lists all shows contained in the database `hbtn_0d_tvshows`.

* 12-no_genre.sql: Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `11-genre_id_all_shows.sql`)

  A script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

* 13-count_shows_by_genre.sql: Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `12-no_genre.sql`)

  A  script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

* 14-my_genres.sql: Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `13-count_shows_by_genre.sql`)

  A script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

* 15-comedy_only.sql: Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `14-my_genres.sql`)

  A script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

* 16-shows_by_genre.sql: Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `15-comedy_only.sql`)

  A script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

* 100-not_my_genres.sql: Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `16-shows_by_genre.sql`)

  A script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`

* 101-not_a_comedy.sql: Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `100-not_my_genres.sql`)

  A script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`.

* 102-rating_shows.sql: Import the database dump from `hbtn_0d_tvshows_rate` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql)

  A script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.

* 103-rating_genres.sql: Import the database dump from `hbtn_0d_tvshows_rate` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql) (same as `102-rating_shows.sql`)

  A script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.
