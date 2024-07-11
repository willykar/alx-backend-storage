-- Creates a table users with the following attributes
-- id integer never null, auto increment ad primary key
-- email string (255 characters) never null
-- name string (255 characters)

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
