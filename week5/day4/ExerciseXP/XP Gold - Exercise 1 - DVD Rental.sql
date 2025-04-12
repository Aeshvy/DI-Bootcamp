-- You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
-- Find out how many films there are for each rating.
SELECT rating, COUNT(*) AS movie_count
FROM film
GROUP BY rating
ORDER BY movie_count DESC;

-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
UPDATE customer
SET first_name = 'Alexander', last_name = 'Eshy', email = 'Eshvovych@gmail.com'
WHERE customer_id = 1;

UPDATE address
SET address = '23 Jan Kur', district = 'Netanya'
WHERE address_id = 5;

-- Get a list of all the movies that have a rating of G or PG-13.
-- Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
SELECT film_id, title, rating, rental_rate
FROM film
WHERE (rating = 'G' OR rating = 'PG-13') AND length < 120 AND rental_rate < 3.00
ORDER BY title ASC;