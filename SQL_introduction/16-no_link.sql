-- Lists score and name of second_table for rows with a name, ordered by score (descending)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
