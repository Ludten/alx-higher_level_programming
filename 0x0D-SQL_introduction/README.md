# SQL - Introduction
> Each file in this repository holds code that illustrates MySQL Introduction
> specific to the SQL programming language

## Description of what each file shows:
* 0-list_databases.sql: A script that lists all databases of your MySQL server.

* 1-create_database_if_missing.sql: A script that creates the database `hbtn_0c_0` in your MySQL server.

	- If the database `hbtn_0c_0` already exists, your script should not fail
	- You are not allowed to use the `SELECT` or `SHOW` statements

* 2-remove_database.sql: A script that deletes the database `hbtn_0c_0` in your MySQL server.

	- If the database `hbtn_0c_0` doesn’t exist, your script should not fail
	- You are not allowed to use the `SELECT` or `SHOW` statements

* 3-list_tables.sql: A script that lists all the tables of a database in your MySQL server.

	- The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)

* 4-first_table.sql: A script that creates a table called first_table in the current database in your MySQL server.

	- first_table description:
		- [ ] `id` INT
		- [ ] `name` VARCHAR(256)
	- The database name will be passed as an argument of the `mysql` command
	- If the table `first_table` already exists, your script should not fail
	- You are not allowed to use the `SELECT` or `SHOW` statements

* 5-full_table.sql: A script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

	- The database name will be passed as an argument of the `mysql` command
	- You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements

* 6-list_values.sql: A script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

	- All fields should be printed
	- The database name will be passed as an argument of the `mysql` command

* 7-insert_value.sql: A script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

	- New row:
		- [ ] `id` = 89
		- [ ] `name` = Best School
	- The database name will be passed as an argument of the `mysql` command

* 8-count_89.sql: A script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

	- The database name will be passed as an argument of the `mysql` command

* 9-full_creation.sql: A script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.

	- second_table description:
		- [ ] `id` INT
		- [ ] `name` VARCHAR(256)
		- [ ] `score` INT
	- The database name will be passed as an argument to the `mysql` command
	- If the table `second_table` already exists, your script should not fail
	- You are not allowed to use the `SELECT` and `SHOW` statements
	- Your script should create these records:
		- [ ] `id` = 1, `name` = “John”, `score` = 10
		- [ ] `id` = 2, `name` = “Alex”, `score` = 3
		- [ ] `id` = 3, `name` = “Bob”, `score` = 14
		- [ ] `id` = 4, `name` = “George”, `score` = 8

* 10-top_score.sql: A script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

	- Results should display both the score and the name (in this order)
	- Records should be ordered by score (top first)
	- The database name will be passed as an argument of the `mysql` command

* 11-best_score.sql: A script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

	- Results should display both the score and the name (in this order)
	- Records should be ordered by score (top first)
	- The database name will be passed as an argument of the `mysql` command

* 12-no_cheating.sql: A script that updates the score of Bob to `10` in the table `second_table`.

	- You are not allowed to use Bob’s id value, only the `name` field
	- The database name will be passed as an argument of the `mysql` command

* 13-change_class.sql: A script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

	- The database name will be passed as an argument of the `mysql` command

* 14-average.sql: A script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

	- The result column name should be `average`
	- The database name will be passed as an argument of the `mysql` command

* 15-groups.sql: A script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

	- The result should display:
		- [ ] the `score`
		- [ ] the number of records for this `score` with the label `number`
	- The list should be sorted by the number of records (descending)
	- The database name will be passed as an argument to the `mysql` command

* 16-no_link.sql: A script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

	- Don’t list rows without a `name` value
	- Results should display the score and the name (in this order)
	- Records should be listed by descending score
	- The database name will be passed as an argument to the `mysql` command

* 100-move_to_utf8.sql: A script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.

  You need to convert all of the following to UTF8:

	- Database hbtn_0c_0
	- Table first_table
	- Field name in first_table


* 101-avg_temperatures.sql: Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql)

  A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

* 102-top_city.sql: Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as `Temperatures #0`)

  A script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

* 103-max_state.sql: Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as `Temperatures #0`)

  A script that displays the max temperature of each state (ordered by State name).
