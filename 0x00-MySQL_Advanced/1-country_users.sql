-- Creates table users with the following attributes
-- id integer never null, auto increment, primary key
-- email string, never null unique
-- name string
-- country enumerations of countries: US, CO and TN, never null

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
