🌟 Exercise 1: DVD Rental

-- Get a list of all the languages, from the language table.
SELECT name FROM language;

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT title, description, language.name AS language_name
FROM film
LEFT JOIN language ON film.language_id = language.language_id;

-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
SELECT title, description, language.name AS language_name
FROM language
LEFT JOIN film ON film.language_id = language.language_id;

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film (
id SERIAL PRIMARY KEY,
name VARCHAR(100)
);

INSERT INTO new_film (name)
VALUES 
('The Lighthouse'),
('Everything Everywhere All At Once'),
('Inception'),
('Parasite'),
('Interstellar');

-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

CREATE TABLE customer_review (
review_id SERIAL NOT NULL PRIMARY KEY,
film_id INT,
language_id INT,
title TEXT,
score INT,
review_text TEXT,
last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
FOREIGN KEY (language_id) REFERENCES language (language_id)
);

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES
(5, 1, 'Outstanding!', 10, 'Truly a once in a lifetime masterpiece', '2019/05/25'),
(3, 5, 'Magnifique', 7, "Plutôt peu inspirant, c'est le moins qu'on puisse dire.", '2025/04/19');

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film
WHERE id = 5

SELECT*FROM customer_review

