# Library Database Management System
## Database Programming Assignment

## **Assignment Overview**

This group assignment will guide you through the complete process of database creation, data loading, SQL querying, database connectivity, and data analysis using Python. You will work with a Library Management System database containing multiple related tables.

---

## **Learning Objectives**

By the end of this assignment, students will be able to:
- Create and structure a relational database in PostgreSQL
- Load data into multiple related tables
- Write complex SQL queries to extract insights
- Connect to PostgreSQL from VSCode
- Translate SQL queries into Pandas equivalents
- Create meaningful visualizations from database data

---

## **Part 1: Database Setup (20 points)**

### Task 1.1: Create Database
Create a PostgreSQL database named `library_db`

```sql
CREATE DATABASE library_db;
```

### Task 1.2: Create Tables
Using the provided schema diagram, create the following tables with appropriate:
- Primary keys
- Foreign keys
- Data types
- Constraints

**Tables to create:**
1. Authors
2. Books
3. Members
4. Departments
5. LibraryStaff
6. BorrowHistory
7. BookOrders

**Deliverable:** Screenshot of successful table creation commands

---

## **Part 2: Data Loading (15 points)**

### Task 2.1: Load Sample Data
Insert at least 15 records into each table ensuring:
- Referential integrity is maintained
- Data is realistic and diverse
- All foreign key relationships are valid

### Task 2.2: Verify Data Load
Write and execute SELECT statements to verify data in each table.

**Deliverable:** Screenshots showing data successfully loaded into all tables

---

## **Part 3: SQL Query Analysis (35 points)** -This part should be done individually

Write SQL queries to answer the following questions. For each query, provide:
- The SQL code
- Screenshot of the query execution
- Screenshot of the output/results

### **Basic Queries (5 points each)**

**Q1.** List all books published after 2015 along with their authors' names.

**Q2.** Find all members who joined in the last 2 years and have a 'Premium' membership.

**Q3.** Display the total number of books written by each author, ordered by count (descending).

**Q4.** Show all currently borrowed books (books with no return date) along with the member's name and borrow date.

**Q5.** List all library staff members working in the 'Circulation' department.

### **Intermediate Queries (7 points each)**

**Q6.** Calculate the total cost of all book orders placed in 2024, grouped by fulfillment status.

**Q7.** Find the top 5 most borrowed books along with the number of times each has been borrowed.

**Q8.** Identify members who have never borrowed a book.

**Q9.** Show the average number of available copies per genre.

**Q10.** List all books that are currently overdue (borrowed more than 30 days ago with no return date).

### **Advanced Queries (10 points each)**

**Q11.** Create a query that shows each department's staff count and the average tenure (years) of staff in that department.

**Q12.** Generate a report showing monthly borrowing trends for the past year (count of books borrowed per month).

**Q13.** Find authors whose books have been borrowed more than 10 times in total, along with their most popular book.

**Q14.** Calculate the total revenue from book orders per supplier, showing only suppliers with orders exceeding $5,000.

**Q15.** Create a complex query that identifies "inactive" members (those who haven't borrowed a book in the last 6 months) who have a Premium membership.

---

## **Part 4: VSCode Database Connection (10 points)**

### Task 4.1: Setup Connection
1. Install the PostgreSQL extension in VSCode
2. Configure connection to your `library_db` database
3. Test the connection

### Task 4.2: Execute Queries from VSCode
Run at least 5 queries from Part 3 directly in VSCode.

**Deliverable:** Screenshots showing:
- Connection configuration
- Query execution in VSCode
- Results displayed in VSCode

---

## **Part 5: Python/Pandas Implementation (15 points)**

### Task 5.1: Database Connection
Write Python code to connect to the PostgreSQL database using `psycopg2` or `SQLAlchemy`.

### Task 5.2: Query Translation
Translate the following SQL queries into Pandas equivalents:

1. Query from Q3 (Book count per author)
2. Query from Q7 (Top 5 most borrowed books)
3. Query from Q9 (Average available copies per genre)
4. Query from Q12 (Monthly borrowing trends)
5. One advanced query of your choice from Q11-Q15

**Code Template:**
```python
import pandas as pd
from sqlalchemy import create_engine

# Create database connection
engine = create_engine('postgresql://username:password@localhost:5432/library_db')

# Example: Load data
df_books = pd.read_sql("SELECT * FROM Books", engine)
df_authors = pd.read_sql("SELECT * FROM Authors", engine)

# Your Pandas queries here
```

**Deliverable:** 
- Python script with all Pandas queries
- Output screenshots showing results match SQL queries

---

## **Part 6: Data Visualization (15 points)**

Create meaningful visualizations for the following:

### Required Visualizations

**V1.** Bar chart showing the top 10 authors by number of books written

**V2.** Pie chart displaying the distribution of members by membership type

**V3.** Line graph showing monthly borrowing trends over time

**V4.** Horizontal bar chart of book genres by total available copies

**V5.** Heatmap or stacked bar chart showing book orders by fulfillment status and supplier

### Visualization Requirements
- Use matplotlib, seaborn etc
- Include proper titles, labels, and legends
- Use appropriate color schemes
- Ensure charts are clear and readable

**Deliverable:** 
- Python script with all visualization code
- Screenshots or saved images of all 5 visualizations
- Brief interpretation (2-3 sentences) for each visualization

---

## **Submission Requirements**

Submit a single ZIP file containing:

1. **SQL Scripts Folder:**
   - `01_create_tables.sql`
   - `02_load_data.sql`
   - `03_queries.sql`

2. **Screenshots Folder:**
   - Organized subfolders for each part
   - Clearly named files (e.g., `Q7_query.png`, `Q7_output.png`)

3. **Python Scripts Folder:**
   - `database_connection.py`
   - `pandas_queries.py`
   - `visualizations.py`

4. **Documentation:**
   - `README.md` with setup instructions
   - `REPORT.pdf` containing:
     - Brief description of your database
     - Summary of insights discovered
     - Challenges faced and solutions
     - Comparison between SQL and Pandas approaches

## **Additional Resources**

- PostgreSQL Documentation: https://www.postgresql.org/docs/
- Pandas Documentation: https://pandas.pydata.org/docs/
- SQLAlchemy Documentation: https://docs.sqlalchemy.org/
- Matplotlib Gallery: https://matplotlib.org/stable/gallery/