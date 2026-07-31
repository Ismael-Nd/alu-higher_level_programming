# SQL_introduction

This project covers the basics of MySQL: listing, creating and
dropping databases, creating and describing tables, and performing
`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `GROUP BY` and aggregate
queries.

## Tasks

| File | Description |
| --- | --- |
| 0-list_databases.sql | Lists all databases of the MySQL server |
| 1-create_database_if_missing.sql | Creates the database `hbtn_0c_0` if missing |
| 2-remove_database.sql | Deletes the database `hbtn_0c_0` if it exists |
| 3-list_tables.sql | Lists all tables of a database |
| 4-first_table.sql | Creates the table `first_table` if missing |
| 5-full_table.sql | Prints the full description of `first_table` |
| 6-list_values.sql | Lists all rows of `first_table` |
| 7-insert_value.sql | Inserts a new row in `first_table` |
| 8-count_89.sql | Counts records with `id = 89` in `first_table` |
| 9-full_creation.sql | Creates `second_table` and inserts initial records |
| 10-top_score.sql | Lists score and name of `second_table`, top score first |
| 11-best_score.sql | Lists score and name of records with `score >= 10` |
| 12-no_cheating.sql | Updates Bob's score to 10, matched by name only |
| 13-change_class.sql | Removes records with `score <= 5` |
| 14-average.sql | Computes the average score of `second_table` |
| 15-groups.sql | Counts records per score, ordered by count (descending) |
| 16-no_link.sql | Lists score and name for rows with a non-null name |

## Usage

Each script is meant to be piped into the `mysql` client:

```
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```
