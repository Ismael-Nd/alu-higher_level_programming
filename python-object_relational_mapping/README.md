# python-object_relational_mapping

This project covers accessing a MySQL database from Python, first with the
`MySQLdb` driver (raw SQL, parameterized queries, SQL injection) and then
with the SQLAlchemy ORM (declarative models, sessions, querying, inserting,
updating and deleting records).

## Requirements

- Ubuntu 20.04 LTS, python3 (3.8.5)
- `MySQLdb` (mysqlclient) 2.0.x
- `SQLAlchemy` 1.4.x
- A MySQL server running on `localhost:3306`

## Tasks

| File | Description |
| --- | --- |
| 0-select_states.py | Lists all states from a database |
| 1-filter_states.py | Lists all states whose name starts with `N` |
| 2-my_filter_states.py | Lists states matching a name (SQL injection possible) |
| 3-my_safe_filter_states.py | Lists states matching a name (SQL injection safe) |
| 4-cities_by_state.py | Lists all cities with their state |
| 5-filter_cities.py | Lists all cities of a given state |
| model_state.py | SQLAlchemy `State` model, mapped to the `states` table |
| 7-model_state_fetch_all.py | Lists all `State` objects |
| 8-model_state_fetch_first.py | Prints the first `State` object |
| 9-model_state_filter_a.py | Lists `State` objects containing the letter `a` |
| 10-model_state_my_get.py | Prints the id of a `State` matching a name |
| 11-model_state_insert.py | Adds a new `State` (`Louisiana`) |
| 12-model_state_update_id_2.py | Renames the `State` with `id = 2` |
| 13-model_state_delete_a.py | Deletes all `State` objects containing `a` |
| model_city.py | SQLAlchemy `City` model, mapped to the `cities` table |
| 14-model_city_fetch_by_state.py | Lists all `City` objects with their state |

## Usage

Each script takes the MySQL username, password and database name as its
first three arguments (some scripts take a 4th argument, e.g. a state name):

```
./0-select_states.py <mysql user> <mysql password> <database>
```
