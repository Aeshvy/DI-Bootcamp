-- Exercise 3 : Items and customers


Part I

-- Create a table named purchases. It should have 3 columns :
-- id : the primary key of the table
-- customer_id : this column references the table customers
-- item_id : this column references the table items
-- quantity_purchased : this column is the quantity of items purchased by a certain customer

CREATE TABLE purchases (
	id SERIAL PRIMARY KEY,
	customer_id int,
	item_id int,
	quantity_purchased int,
	FOREIGN KEY (item_id) REFERENCES items(item_id),
	FOREIGN KEY (customer_id) REFERENCES 			
	customers(customer_id)
)

-- Insert purchases for the customers, use subqueries:
-- Scott Scott bought one fan
-- Melanie Johnson bought ten large fans
-- Greg Jones bougth two small desks

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
(SELECT customer_id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'),
(SELECT item_id FROM items WHERE item_name = 'Fan'), 1
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
(SELECT customer_id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
(SELECT item_id FROM items WHERE item_name = 'Large Fan'), 10
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
(SELECT customer_id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
(SELECT item_id FROM items WHERE item_name = 'Small Desk'), 2
);


Part II

-- Use SQL to get the following from the database:
-- All purchases. Is this information useful to us?
-- All purchases, joining with the customers table.
-- Purchases of the customer with the ID equal to 5.
-- Purchases for a large desk AND a small desk

SELECT SUM (quantity_purchased)
FROM purchases;

SELECT * FROM purchases
INNER JOIN customers ON purchases.customer_id = customers.customer_id;

SELECT 
  purchases.id,
  items.item_name,
  purchases.quantity_purchased
FROM purchases
INNER JOIN items ON purchases.item_id = items.item_id
WHERE purchases.customer_id = 5;

SELECT 
  purchases.id,
  customers.first_name,
  customers.last_name,
  items.item_name,
  purchases.quantity_purchased
FROM purchases
INNER JOIN customers ON purchases.customer_id = customers.customer_id
INNER JOIN items ON purchases.item_id = items.item_id
WHERE items.item_name IN ('Large Desk', 'Small Desk');