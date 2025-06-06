CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

SELECT * FROM FirstTab

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)


SELECT * FROM SecondTab

-- Table1 – FirstTab
ID  	Name
5   	Pawan
6   	Sharlee
7   	Krish
NULL    Avtaar

-- Table2 – SecondTab
ID
5
NULL



-- Q1. What will be the OUTPUT of the following statement?
    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
-- COUNT: 0 ( 5,6,7,NULL != NULL = UNKOWN (0) )

-- Q2. What will be the OUTPUT of the following statement?
    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- COUNT: 2 ( 6,7 != 5 (2) )

-- Q3. What will be the OUTPUT of the following statement?
    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- COUNT: 0 ( 5,6,7,NULL != 5,NULL = UNKNOWN (0) )
			

-- Q4. What will be the OUTPUT of the following statement?
    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- COUNT: 2 ( 5 != 5 = 0, THEREFORE = 6,7 )

