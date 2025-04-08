-- Database: Hollywood

-- DROP DATABASE IF EXISTS "Hollywood";

-- CREATE DATABASE "Hollywood"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'en-US'
--     LC_CTYPE = 'en-US'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;
----------------------------------------------------------------------

CREATE TABLE actors(
actor_id SERIAL PRIMARY KEY,
first_name VARCHAR (50) NOT NULL,
last_name VARCHAR (100) NOT NULL,
age DATE NOT NULL,
number_oscars SMALLINT NOT NULL
)

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);

----------------------------------------------------------------------
-- Add two more female actors in the table actors. Add them one by one
-- Add three more actors, add all of them in one query !
-- Retrieve everything from the table actors
----------------------------------------------------------------------

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Natalie', 'Portman', '05/25/1985', 10);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Jennifer', 'Anniston', '04/17/1989', 7);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Brad', 'Pitt', '08/19/1975', 17),
		('John', 'Cena', '05/05/2001', 0),
		('Keanu', 'Reeves', '01/01/1981', 5);

SELECT first_name, last_name FROM actors;
SELECT * FROM actors WHERE number_oscars >= 10
SELECT first_name, last_name FROM actors WHERE first_name = 'Brad'
AND last_name = 'Pitt'

SELECT * FROM actors WHERE last_name LIKE '%mon%';
SELECT first_name FROM actors WHERE last_name LIKE '%y';
SELECT first_name FROM actors WHERE last_name LIKE 'da%';
SELECT first_name FROM actors WHERE last_name iLIKE 'da%';

SELECT * FROM actors WHERE number_oscars >= 10 LIMIT 2 OFFSET 1;

SELECT * FROM actors WHERE number_oscars >=7 ORDER BY first_name ASC;

----------------------------------------------------------------------
-- Use the table actors to retrieve:

-- The first 4 actors
-- The first 4 actors ordered in descending order of the last_name (ie. sorted DESCENDING by the "last_name" column))
-- The actors that have the letter 'e' in their first_name
-- The actors that got at least 5 oscars
----------------------------------------------------------------------

SELECT * FROM actors LIMIT 4;
SELECT * FROM actors ORDER BY last_name DESC LIMIT 4;
SELECT * FROM actors WHERE first_name ILIKE '%e%';
SELECT * FROM actors WHERE number_oscars >=5;

UPDATE actors SET number_oscars=12 WHERE first_name='Brad'
RETURNING first_name, last_name, number_oscars;

DELETE FROM actors WHERE actor_id=4
RETURNING first_name, last_name, number_oscars;

----------------------------------------------------------------------
-- In the table actors, write the following commands:

-- Update the first name of Matt Damon to Maty
-- Update the number of oscars of George Clooney to 4, and return the updated record
-- Rename the age column to birthdate
-- Delete one actor and return it
----------------------------------------------------------------------

UPDATE actors SET first_name='Maty' WHERE first_name='Matt';

UPDATE actors SET actor_id=1 WHERE first_name='George'
RETURNING actor_id, first_name, last_name, number_oscars;

ALTER TABLE actors RENAME COLUMN age TO birthdate;

DELETE FROM actors WHERE actor_id=6
RETURNING actor_id, first_name, birthdate;

----------------------------------------------------------------------

-- ✅ DAILY CHALLENGE

SELECT COUNT (*) FROM actors;
INSERT INTO actors (first_name, last_name, birthdate, number_oscars)
VALUES ('', '', '05/25/1995', 0);

SELECT * FROM actors;


