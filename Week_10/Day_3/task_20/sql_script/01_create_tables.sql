
-- To create authors table
CREATE TABLE Authors (
    Author_id INT PRIMARY KEY,
	Author_name VARCHAR(255) NOT NULL,
    Country_of_origin VARCHAR(255),
    Number_of_Books_Written INT
  );

-- To create members table
CREATE TYPE Gender AS ENUM('Female','Male');
CREATE TYPE member_status AS ENUM('Active','Suspended');
CREATE TABLE Members (
    Member_id INT PRIMARY KEY,
	Member_Name VARCHAR(255),
    Gender Gender,
    Email_Address VARCHAR(255),
	PhoneNumber VARCHAR(20),
	Address VARCHAR(255),
	Age INT,
	Type_of_Membership VARCHAR(255),
	Date_of_Membership DATE,
	status member_status
  );

-- To create Books table
  CREATE TABLE Books (
    Book_id INT PRIMARY KEY,
	Title VARCHAR(255),
    Author_Id INT REFERENCES Authors(Author_Id),
    Genre VARCHAR(255),
	Date_of_Publication DATE,
	Publisher VARCHAR(255),
	ISBN VARCHAR(255),
	B_Language VARCHAR(255),
	Available_Copies INT,
	AgeRating VARCHAR(255)
	);

-- To create departments table
CREATE TABLE Departments (
Dept_Id INT PRIMARY KEY,
Department_Name VARCHAR(255),
Manager_Name VARCHAR(255)
);

-- To create librarystaff table
-- CREATE TYPE Gender AS ENUM('Female','Male');
CREATE TABLE LibraryStaff(
Staff_Id INT PRIMARY KEY,
s_Name VARCHAR(255),
Job_Title VARCHAR(255),
Dept_Id INT REFERENCES Departments(Dept_Id),
Gender Gender,
Address VARCHAR(256),
Phone_Number VARCHAR(15),
Hire_Date DATE,
Manager_Id INT  
);

-- To create borrowhistory table
CREATE TABLE BorrowHistory(
Borrow_Id INT PRIMARY KEY,
Book_Id INT REFERENCES Books(Book_Id),
Member_Id INT REFERENCES Members(Member_Id),
Borrow_Date DATE,
Return_Date DATE
);

-- To create bookorders table
CREATE TYPE FulFillment_Status AS ENUM('Fulfilled','Pending','Processing');
CREATE TABLE BookOrders(
Order_Id INT PRIMARY KEY,
Order_Date DATE,
Book_Id INT REFERENCES Books(Book_Id),
o_Cost DECIMAL(10,2),
Quantity INT,
Supply_Date DATE,
FulFillment_Status FulFillment_Status,
Supplier_Name VARCHAR(255)
);