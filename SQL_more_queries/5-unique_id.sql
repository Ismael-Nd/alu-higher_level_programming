-- Creates the table unique_id, where id defaults to 1 and must be unique, if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
