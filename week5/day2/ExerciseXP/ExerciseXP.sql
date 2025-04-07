-- Database: public

-- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
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
-- 🌟 Exercise 1 : Items and customers
-- Create a database called public.
-- Add two tables:
-- items
-- customers.

-- CREATE TABLE items(
-- item_id SERIAL PRIMARY KEY,
-- item_name VARCHAR (50) NOT NULL,
-- price SMALLINT NOT NULL
-- );

-- CREATE TABLE customers(
-- customer_id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL
-- );

-- INSERT INTO items (item_name, price)
-- VALUES('Small Desk', 100),
-- ('Large Fan', 300),
-- ('Fan', 80);

INSERT INTO customers ()




SELECT * FROM items;