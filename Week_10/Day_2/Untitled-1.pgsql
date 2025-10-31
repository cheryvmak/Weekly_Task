SELECT * FROM  Books;

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



--- Find all members who joined in the last 2 years and have a 'Premium' membership.

SELECT 
member_name,type_of_membership,date_of_membership
FROM Members
WHERE type_of_membership = 'Premium'
AND date_of_membership >= (SELECT MAX(date_of_membership) - 
INTERVAL '2 years' FROM Members)
ORDER BY 
date_of_membership DESC;


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
    book_title
ORDER BY 
    times_borrowed DESC
LIMIT 5;






