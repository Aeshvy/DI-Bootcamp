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

-- INSERT INTO students(first_namme, last_name, birth_date)
-- VALUES('Marc', 'Benichou', '02/11/1998'),
-- ('Yoan', 'Cohen', '03/12/2010'),
-- ('Lea', 'Benichou', '27/07/1987'),
-- ('Amelia', 'Dux', '07/04/1996'),
-- ('David', 'Grez', '14/06/2003'),
-- ('Omer', 'Simpson', '03/10/1980');

COPY students
FROM 'C:\Users\eshvo\Desktop\Fullstack\DI-Bootcamp\week5\day2\ExerciseXP\students.csv'
DELIMITER ','
CSV HEADER;

-- SELECT * FROM students

