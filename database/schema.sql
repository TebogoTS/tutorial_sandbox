CREATE DATABASE IF NOT EXISTS people_db;
USE people_db;

CREATE TABLE people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO people (name) VALUES ('John Doe'), ('Jane Doe');
