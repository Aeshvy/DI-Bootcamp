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




SELECT * FROM customers
SELECT * FROM items
SELECT * FROM purchases