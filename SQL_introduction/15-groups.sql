-- Lists the number of records for each score in second_table, ordered by number (descending)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
