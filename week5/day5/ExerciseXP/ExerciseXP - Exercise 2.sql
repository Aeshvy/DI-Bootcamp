🌟 Exercise 2 : DVD Rental

-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id = 2
WHERE film_id IN (1, 2, 3)

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
Customer(address_id) References address(address_id)
address_id must already exists in address tables, otherwise, the insert will fail.

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review;

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) AS "Rentals outstanding"
FROM rental
WHERE return_date IS NULL;

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT film.title, film.rental_rate
FROM rental
INNER JOIN inventory ON rental.inventory_id = inventory.inventory_id
INNER JOIN film ON inventory.film_id = film.film_id
WHERE return_date IS NULL
ORDER BY film.rental_rate DESC
LIMIT 30;


-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?

-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT title, description, actor.first_name, actor.last_name
FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Penelope'
AND actor.last_name = 'Monroe'
AND description ILIKE '%sumo wrestler%'

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT title, length, rating, category.name
FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Documentary'
AND length < 60
AND rating = 'R'

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.


-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

