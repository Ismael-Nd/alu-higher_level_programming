-- Lists all cities of California, using a subquery instead of a JOIN
SELECT id, name FROM cities
    WHERE state_id = (SELECT id FROM states WHERE name = "California")
    ORDER BY id ASC;
