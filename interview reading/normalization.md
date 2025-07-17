# Database Normalization Guide

Database normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It involves decomposing tables into smaller, related tables and defining relationships between them.

## Why Normalize?

**Benefits:**
- **Eliminates data redundancy** - No duplicate information
- **Improves data integrity** - Consistent data across tables
- **Reduces storage space** - Less duplicate data
- **Easier maintenance** - Update data in one place
- **Prevents anomalies** - Insert, update, delete anomalies

**Drawbacks:**
- **More complex queries** - Requires JOINs
- **Potential performance impact** - More tables to query

## Normal Forms

### **Unnormalized Form (0NF)**
**Example - Student Course System:**
```sql
-- Bad: Unnormalized table
CREATE TABLE student_courses (
    student_id INTEGER,
    student_name VARCHAR(100),
    student_email VARCHAR(100),
    courses VARCHAR(500),  -- "Math,Physics,Chemistry"
    instructors VARCHAR(500)  -- "Dr.Smith,Dr.Jones,Dr.Brown"
);

INSERT INTO student_courses VALUES 
(1, 'John Doe', 'john@email.com', 'Math,Physics', 'Dr.Smith,Dr.Jones'),
(2, 'Jane Smith', 'jane@email.com', 'Math,Chemistry', 'Dr.Smith,Dr.Brown');
```

**Problems:**
- Multiple values in single fields
- Difficult to query specific courses
- Hard to add/remove courses

---

### **First Normal Form (1NF)**

**Rules:**
- Each column contains **atomic values** (indivisible)
- No **repeating groups** or arrays
- Each row is **unique**
- Order of rows/columns doesn't matter

**Example:**
```sql
-- 1NF: Atomic values, no repeating groups
CREATE TABLE student_courses_1nf (
    student_id INTEGER,
    student_name VARCHAR(100),
    student_email VARCHAR(100),
    course VARCHAR(100),
    instructor VARCHAR(100)
);

INSERT INTO student_courses_1nf VALUES 
(1, 'John Doe', 'john@email.com', 'Math', 'Dr.Smith'),
(1, 'John Doe', 'john@email.com', 'Physics', 'Dr.Jones'),
(2, 'Jane Smith', 'jane@email.com', 'Math', 'Dr.Smith'),
(2, 'Jane Smith', 'jane@email.com', 'Chemistry', 'Dr.Brown');
```

**Issues still present:**
- Student data repeated for each course
- Update anomalies (change student email in multiple places)

---

### **Second Normal Form (2NF)**

**Rules:**
- Must be in **1NF**
- **No partial dependencies** - Non-key attributes must depend on the entire primary key
- Applies only to tables with **composite primary keys**

**Example:**
```sql
-- 2NF: Remove partial dependencies
-- Students table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    student_email VARCHAR(100)
);

-- Courses table  
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name VARCHAR(100),
    instructor VARCHAR(100)
);

-- Enrollment table (many-to-many relationship)
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    grade CHAR(2),
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert data
INSERT INTO students VALUES 
(1, 'John Doe', 'john@email.com'),
(2, 'Jane Smith', 'jane@email.com');

INSERT INTO courses VALUES 
(101, 'Math', 'Dr.Smith'),
(102, 'Physics', 'Dr.Jones'),
(103, 'Chemistry', 'Dr.Brown');

INSERT INTO enrollments VALUES 
(1, 101, 'A', '2024-01-15'),
(1, 102, 'B', '2024-01-15'),
(2, 101, 'A', '2024-01-16'),
(2, 103, 'B+', '2024-01-16');
```

**Benefits achieved:**
- Student data stored once
- Course data stored once
- No update anomalies for student/course info

**Issues still present:**
- Instructor depends only on course, not on student-course combination

---

### **Third Normal Form (3NF)**

**Rules:**
- Must be in **2NF**
- **No transitive dependencies** - Non-key attributes should not depend on other non-key attributes
- Every non-key attribute depends **directly** on the primary key

**Example:**
```sql
-- 3NF: Remove transitive dependencies
-- Students table (unchanged)
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    student_email VARCHAR(100)
);

-- Instructors table (new)
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY,
    instructor_name VARCHAR(100),
    department VARCHAR(100),
    email VARCHAR(100)
);

-- Courses table (modified)
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name VARCHAR(100),
    instructor_id INTEGER,
    credits INTEGER,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

-- Enrollments table (unchanged)
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    grade CHAR(2),
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert data
INSERT INTO instructors VALUES 
(1, 'Dr.Smith', 'Mathematics', 'smith@university.edu'),
(2, 'Dr.Jones', 'Physics', 'jones@university.edu'),
(3, 'Dr.Brown', 'Chemistry', 'brown@university.edu');

INSERT INTO courses VALUES 
(101, 'Calculus I', 1, 3),
(102, 'Physics I', 2, 4),
(103, 'Organic Chemistry', 3, 4);
```

**Benefits achieved:**
- No transitive dependencies
- Instructor information stored once
- Easy to update instructor details

---

### **Boyce-Codd Normal Form (BCNF)**

**Rules:**
- Must be in **3NF**
- **Every determinant must be a candidate key**
- Stricter version of 3NF

**Example where 3NF ≠ BCNF:**
```sql
-- Problem: Multiple instructors can teach same course
CREATE TABLE course_instructors (
    course_name VARCHAR(100),
    instructor_name VARCHAR(100),
    instructor_office VARCHAR(100),
    PRIMARY KEY (course_name, instructor_name)
);

-- Issue: instructor_name → instructor_office
-- But instructor_name is not a candidate key
```

**BCNF Solution:**
```sql
-- Separate instructor information
CREATE TABLE instructors (
    instructor_name VARCHAR(100) PRIMARY KEY,
    instructor_office VARCHAR(100)
);

CREATE TABLE course_assignments (
    course_name VARCHAR(100),
    instructor_name VARCHAR(100),
    PRIMARY KEY (course_name, instructor_name),
    FOREIGN KEY (instructor_name) REFERENCES instructors(instructor_name)
);
```

---

## Step-by-Step Normalization Process

### **Step 1: Identify the Problem**
```sql
-- Original unnormalized table
CREATE TABLE order_details (
    order_id INTEGER,
    customer_name VARCHAR(100),
    customer_address VARCHAR(200),
    product_name VARCHAR(100),
    product_price DECIMAL(10,2),
    quantity INTEGER,
    supplier_name VARCHAR(100),
    supplier_contact VARCHAR(100)
);
```

### **Step 2: Apply 1NF**
```sql
-- Already in 1NF (atomic values, no repeating groups)
-- Add primary key
ALTER TABLE order_details ADD PRIMARY KEY (order_id, product_name);
```

### **Step 3: Apply 2NF**
```sql
-- Remove partial dependencies
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_address VARCHAR(200),
    order_date DATE
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(100),
    product_price DECIMAL(10,2),
    supplier_name VARCHAR(100),
    supplier_contact VARCHAR(100)
);

CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

### **Step 4: Apply 3NF**
```sql
-- Remove transitive dependencies
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_address VARCHAR(200)
);

CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name VARCHAR(100),
    supplier_contact VARCHAR(100)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(100),
    product_price DECIMAL(10,2),
    supplier_id INTEGER,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price DECIMAL(10,2), -- Price at time of order
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

---

## Practical Examples

### **E-commerce Database**
```sql
-- Customers
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20)
);

-- Addresses (separate for flexibility)
CREATE TABLE addresses (
    address_id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    address_type VARCHAR(20), -- 'billing', 'shipping'
    street VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Categories
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100),
    parent_category_id INTEGER,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id)
);

-- Products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(200),
    description TEXT,
    price DECIMAL(10,2),
    category_id INTEGER,
    stock_quantity INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20),
    total_amount DECIMAL(10,2),
    shipping_address_id INTEGER,
    billing_address_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (shipping_address_id) REFERENCES addresses(address_id),
    FOREIGN KEY (billing_address_id) REFERENCES addresses(address_id)
);

-- Order Items
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

---

## When NOT to Normalize

### **Denormalization Cases**
```sql
-- Reporting table (denormalized for performance)
CREATE TABLE sales_report (
    report_date DATE,
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    category_name VARCHAR(100),
    quantity INTEGER,
    revenue DECIMAL(10,2),
    profit DECIMAL(10,2)
);

-- Data warehouse fact table
CREATE TABLE fact_sales (
    sale_id INTEGER,
    date_key INTEGER,
    customer_key INTEGER,
    product_key INTEGER,
    quantity INTEGER,
    amount DECIMAL(10,2),
    -- Denormalized for fast aggregation
    customer_segment VARCHAR(50),
    product_category VARCHAR(50)
);
```

### **Performance vs. Normalization Trade-offs**

**When to denormalize:**
- Read-heavy applications
- Reporting and analytics
- Data warehouses
- Caching layers
- Real-time dashboards

**When to stay normalized:**
- OLTP systems
- High data integrity requirements
- Frequent updates
- Limited storage
- Multi-user environments

---

## Tools and Techniques

### **Identifying Dependencies**
```sql
-- Find functional dependencies
-- If knowing A always tells you B, then A → B

-- Example analysis
SELECT customer_id, customer_name, COUNT(DISTINCT customer_email)
FROM orders
GROUP BY customer_id, customer_name
HAVING COUNT(DISTINCT customer_email) > 1;
-- Should return 0 rows if customer_id → customer_email
```

### **Normalization Checklist**

**1NF Checklist:**
- [ ] All attributes contain atomic values
- [ ] No repeating groups
- [ ] Each row is unique
- [ ] Primary key defined

**2NF Checklist:**
- [ ] Table is in 1NF
- [ ] No partial dependencies
- [ ] All non-key attributes depend on entire primary key

**3NF Checklist:**
- [ ] Table is in 2NF
- [ ] No transitive dependencies
- [ ] Non-key attributes depend only on primary key

**BCNF Checklist:**
- [ ] Table is in 3NF
- [ ] Every determinant is a candidate key

---

## Best Practices

1. **Start with business requirements** - Understand the data relationships
2. **Identify entities and relationships** - Draw ER diagrams
3. **Apply normalization gradually** - Don't skip steps
4. **Consider performance implications** - Balance normalization with query performance
5. **Document decisions** - Explain denormalization choices
6. **Test with real data** - Verify the design works with actual data volumes
7. **Plan for growth** - Consider how the schema will evolve

Database normalization is a fundamental skill for database design. Start with understanding the business requirements, apply normalization rules systematically, and always consider the trade-offs between data integrity and performance.