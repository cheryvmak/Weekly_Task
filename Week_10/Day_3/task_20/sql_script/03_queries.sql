--- Q1
--- List all books published after 2015 along with their authors' names

SELECT 
    b.title AS book_title,
    a.author_name,
    b.date_of_publication FROM Books b
JOIN Authors a
ON 
b.Author_Id = a.Author_Id
WHERE 
b.date_of_publication > '2015-12-31'
ORDER BY 
b.date_of_publication;

--- Q2
--- Find all members who joined in the last 2 years and have a 'Premium' membership.

SELECT 
member_name,type_of_membership,date_of_membership
FROM Members
WHERE type_of_membership = 'Premium'
AND date_of_membership >= (SELECT MAX(date_of_membership) - 
INTERVAL '2 years' FROM Members)
ORDER BY 
date_of_membership DESC;


--- Q3
-- Display the total number of books written by each author, ordered by count (descending).

SELECT 
    a.author_name,
    COUNT(b.book_id) AS total_books
FROM 
    Authors a
JOIN 
    Books b
ON 
    b.Author_Id = a.Author_Id
GROUP BY 
    a.author_name
ORDER BY 
    total_books DESC;


--- Q4
-- Show all currently borrowed books (books with no return date) along with the member's name and borrow date.

SELECT 
    b.title AS book_title,
    m.member_name,
    bh.Borrow_Date
FROM 
    BorrowHistory bh
JOIN 
    Books b
ON 
    bh.Book_id = b.Book_id
JOIN 
    Members m
ON 
    bh.Member_id = m.Member_id
WHERE 
    bh.Return_Date IS NULL
ORDER BY 
    bh.Borrow_Date DESC;

--- Q5
-- List all library staff members working in the 'Circulation' department.

SELECT 
    s.Staff_id,
    s.s_Name,
    d.Department_Name  
FROM 
    LibraryStaff s
JOIN 
    Departments d ON s.Dept_Id = d.Dept_Id
WHERE 
    d.Department_Name= 'Circulation'
ORDER BY 
    s.s_Name;

--- Q6
-- Calculate the total cost of all book orders placed in 2024, grouped by fulfillment status.

SELECT 
    FulFillment_Status,
    SUM(o_Cost) AS total_order_cost
FROM 
    BookOrders
WHERE 
    EXTRACT(YEAR FROM Order_Date) = 2024
GROUP BY 
    FulFillment_Status
ORDER BY 
    total_order_cost DESC;


--- Q7
-- Find the top 5 most borrowed books along with the number of times each has been borrowed.

SELECT 
    b.title AS book_title,
    COUNT(bh.Book_Id) AS times_borrowed
FROM 
    BorrowHistory bh
JOIN 
    Books b 
ON 
    bh.Book_Id = b.Book_Id
GROUP BY 
    b.title
ORDER BY 
    times_borrowed DESC
LIMIT 5;


--- Q8
-- Identify members who have never borrowed a book
SELECT 
    m.Member_Id,
    m.Member_Name
FROM 
    Members m
JOIN 
    BorrowHistory bh 
ON 
    m.Member_Id = bh.Member_Id
WHERE 
    bh.Member_Id IS NULL
ORDER BY 
    m.Member_Name;



--- Q9
---Show the average number of available copies per genre.

SELECT 
    Genre,
	--AVG(Available_Copies) AS Avg_Available_Copies
	ROUND(AVG(Available_Copies), 2) AS Avg_Available_Copies
FROM 
    Books
GROUP BY 
    Genre
ORDER BY 
    Avg_Available_Copies DESC;



--- Q10
-- List all books that are currently overdue (borrowed more than 30 days ago with no return date).

SELECT 
    b.Book_Id,
    b.title,
    m.Member_Name,
    bh.Borrow_Date,
    CURRENT_DATE - bh.Borrow_Date AS days_borrowed
FROM 
    BorrowHistory bh
JOIN 
    Books b ON bh.Book_Id = b.Book_Id
JOIN 
    Members m ON bh.Member_Id = m.Member_Id
WHERE 
    bh.Return_Date IS NULL
    AND bh.Borrow_Date < CURRENT_DATE - INTERVAL '30 days'
ORDER BY 
    bh.Borrow_Date ASC;




-- Q 12
-- Generate a report showing monthly borrowing trends for the past year (count of books borrowed per month).

SELECT 
    TO_CHAR(borrow_date, 'YYYY-MM') AS borrow_month,
    COUNT(*) AS total_borrowed
FROM 
    BorrowHistory
WHERE
    borrow_date >=(SELECT MAX(borrow_date) - INTERVAL '1 year' FROM BorrowHistory)
GROUP BY 
    borrow_month
ORDER BY 
    borrow_month;


-- Q 14
-- Calculate the total revenue from book orders per supplier, showing only suppliers with orders exceeding $5,000.

SELECT 
   supplier_name,
    SUM(quantity * o_cost) AS total_revenue

FROM 
    bookorders

GROUP BY 
Supplier_Name

HAVING 
    SUM(quantity * o_cost) > 5000
ORDER BY 
    total_revenue DESC;

