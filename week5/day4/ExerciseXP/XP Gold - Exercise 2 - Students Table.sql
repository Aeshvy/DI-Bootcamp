-- Exercise 2: students table

Update

-- ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
UPDATE students
SET birth_date = '02/11/1998'
WHERE id = 1 

UPDATE students
SET birth_date = '02/11/1998'
WHERE id = 3;

-- Change the last_name of David from ‘Grez’ to ‘Guez’.
UPDATE students
SET last_name = 'Guez'
WHERE id = 5;


Delete

-- Delete the student named ‘Lea Benichou’ from the table.
DELETE FROM students
WHERE first_name = 'Lea'


Count

-- Count how many students are in the table.
SELECT COUNT (*) FROM students;

-- Count how many students were born after 1/01/2000.
SELECT COUNT (*)
FROM students
WHERE birth_date > '1/01/2000';


Insert / Alter

-- Add a column to the student table called math_grade.
ALTER TABLE students
ADD math_grade SMALLINT;

-- Add 80 to the student which id is 1.
UPDATE students
SET math_grade = 80
WHERE id = 1;

-- Add 90 to the students which have ids of 2 or 4.
UPDATE students
SET math_grade = 90
WHERE id IN (2, 4);

-- Add 40 to the student which id is 6.
UPDATE students
SET math_grade = 40
WHERE id = 6;

-- Count how many students have a grade bigger than 83
SELECT COUNT (*)
FROM students
WHERE math_grade > 83;

-- Add another student named ‘Omer Simpson’ with the same 	birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO students (id, first_name, last_name, birth_date, math_grade)
VALUES (3, 'Omer', 'Simpson', '1980/10/03', 70);
-- Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam.


SUM

-- Find the sum of all the students grades.
SELECT SUM(math_grade) AS student_grade_sum
FROM students