Exercise 1 : Bonus Public Database (Continuation of XP)

-- Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
-- Use SQL to delete all purchases made by Scott.
-- Does Scott still exist in the customers table, even though he has been deleted? Try and find him.
-- Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will appear, although instead of the customer’s    first and last name, you should only see empty/blank. (Which kind of join should you use?).
-- Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will NOT appear. (Which kind of join should you use?)

SELECT first_name, last_name
FROM customers
ORDER BY first_name ASC
LIMIT 2 OFFSET 3;

DELETE FROM customers WHERE customer_id = 3;

SELECT 
    purchases.id,
    customers.first_name,
    customers.last_name
FROM purchases
LEFT JOIN customers
ON purchases.customer_id = customers.customer_id;

SELECT 
    purchases.id,
    customers.first_name,
    customers.last_name
FROM purchases
INNER JOIN customers
ON purchases.customer_id = customers.customer_id;