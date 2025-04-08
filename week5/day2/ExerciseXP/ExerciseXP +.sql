-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
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
-- CREATE TABLE students(
-- id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL,
-- birth_date DATE NOT NULL
-- )

-- INSERT INTO students(first_name, last_name, birth_date)
-- VALUES('Marc', 'Benichou', '11/02/1998'),
-- ('Yoan', 'Cohen', '12/03/2010'),
-- ('Lea', 'Benichou', '07/27/1987'),
-- ('Amelia', 'Dux', '04/07/1996'),
-- ('David', 'Grez', '06/14/2003'),
-- ('Omer', 'Simpson', '10/03/1980');

-- COPY students(first_name, last_name, birth_date)
-- FROM 'students.csv'
-- DELIMITER ','
-- CSV HEADER;

-- SET DateStyle = 'ISO, DMY';

-- SELECT * FROM students
-- SELECT first_name, last_name FROM students
-- SELECT * FROM students WHERE id = 2




