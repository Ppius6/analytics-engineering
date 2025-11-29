# SQL Notes

## SQL, Databases, and DBMS.
`Read more`: [More notes](https://www.geeksforgeeks.org/sql-tutorial/?ref=shm)

- A database is a standard language for storing, manipulating, and retrieving data in databases. 

- It is an organized collection of data stored in a computer system and is controlled by a database management system (DBMS). 
- Here, data is organized into tables consisting of rows and columns and is indexed so data can be updated, expanded, and deleted easily. The databases include:
    - `Relational databases` - A database with a set of tables with data that fits into a pre-defined category.
    - `Distributed databases` - A database in which portions of the database are stored in multiple physical locations, and in which processing is dispersed or replicated among different points in a network.
    - `Cloud databases` - A database that runs on a cloud computing platform. It is built in a cloud to optimize for a virtual work setting and distribution. Organizations tend to be charged based on the amount of storage or bandwidth they use.
    - `Object-Oriented Databases`: Similar to object-oriented programming, data in an object-oriented database is represented as objects.
    - `Data Warehouses`: A data warehouse is a sort of database created especially for quick query and analysis. It is a central repository for data.
    - `NoSQL/Non-Relational Databases`: Unlike relational databases, which specify how all data input must be formatted, NoSQL, or nonrelational databases, permit the storing and manipulation of unstructured and semistructured data. The prevalence and complexity of online applications led to the rise in popularity of NoSQL databases. They include key/value, graph, column, document databases.
    - `Graph database`: A graph database is a type of NoSQL database. It stores, queries, and maps relationships according to the graph theory. Graph databases are used to analyze interactions and connections. They consist of nodes and edges, and use a declarative programming language called SPARQL.
    - `Open-source database`: These databases are open-source, meaning anyone can contribute or edit the source code. They can be SQL or NoSQL.

### Database Management System

A `DBMS`, also known as a `Database Management System` is a computer program that can store large amounts of data and process them accordingly. 

DBMS include:
- `Relational DBMS`: Organized data into tables.
- `NoSQL DBMS`: It's more flexible and can handle a variety of data types, making it perfect for big data and real-time web apps. Think of it like a giant, flexible storage room where you can keep all sorts of items without needing them to be the same shape or size.
- `NewSQL DBMS`: They provide the scalability and adaptability inherent in NoSQL, while preserving the structured integrity and consistency characteristic of an RDBMS. 
- `Object-Oriented DBMS`: This type stores data in objects, similar to object-oriented programming. It's like having a personal assistant for each type of data, understanding how it behaves and how it relates to other data. 
- `Cloud DBMS`: It is hosted on a cloud platform rather than on-premises servers or personal computers.

It is also the software that interacts with users to process data. The software include:
- PostgreSQL
- Oracle Database
- Microsoft SQL Server
- MySQL
- SQLite

In a typical relational DBMS, data is organized in tables, with relationships. 
It allows the users to:
- Store data physically.
- Process SQL instructions.
- Add, modify, and remove data. 
- Modify database structure.
- Enable concurrent data access.
- Manage constraints.
- Backup capabilities.
- Supply Metadata.

## Data Types in SQL

Databases consist of multiple tables, and a schema illustrates their structure, relationships, and field data types.

SQL (Structured Query Language) uses data types to define the nature of data that can be stored in a table's columns. Data types help ensure data integrity, optimize storage, and enable accurate queries. Here’s a comprehensive overview of the most common SQL data types:

### 1. Numeric Data Types

Numeric data types are used to store numbers, either whole numbers (integers) or numbers with fractional parts (decimals).

- **INT (INTEGER):**
  - Stores whole numbers.
  - Common subtypes: `TINYINT`, `SMALLINT`, `MEDIUMINT`, `BIGINT`.
    - `TINYINT`: A very small integer with a range from -128 to 127 (signed) or 0 to 255 (unsigned).
    - TINYINT is suitable for storing small data ranges such as age, number of items in a limited collection, or similar use cases. Here is an example of how to use TINYINT:

        ```
        CREATE TABLE example_tinyint (
            id INT AUTO_INCREMENT PRIMARY KEY,
            rating TINYINT NOT NULL
        );

        INSERT INTO example_tinyint (rating) VALUES (10), (127), (-128);

        SELECT * FROM example_tinyint;
        ```

    - `SMALLINT`: A small integer with a range of -32768 to 32767 (signed) or 0 to 65535 (unsigned). It’s commonly used for quantities where the maximum number is known not to exceed the limit, such as the number of participants in an event divided into different sessions. Here’s an example:

        ```
        CREATE TABLE example_smallint (
            id INT AUTO_INCREMENT PRIMARY KEY,
            participants SMALLINT NOT NULL
        );

        INSERT INTO example_smallint (participants) VALUES (3000), (32767), (-32768);

        SELECT * FROM example_smallint;
        ```

    - `MEDIUMINT`: A medium-sized integer with a range from -8388608 to 8388607 (signed) or 0 to 16777215 (unsigned).For instance, you can use it to store the population of cities or the number of views of a very popular video. Example:

        ```
        CREATE TABLE example_mediumint (
            id INT AUTO_INCREMENT PRIMARY KEY,
            views MEDIUMINT NOT NULL
        );

        INSERT INTO example_mediumint (views) VALUES (150000), (8388607), (-8388608);

        SELECT * FROM example_mediumint;
        ```

    - `INT` or `INTEGER`: A standard-size integer with a range of -2147483648 to 2147483647 (signed) or 0 to 4294967295 (unsigned). It’s used for identifiers, counters, and other use cases where a large range might be necessary. Here’s how to use INT:

        ```
        CREATE TABLE example_int (
            id INT AUTO_INCREMENT PRIMARY KEY,
            total_orders INT NOT NULL
        );

        INSERT INTO example_int (total_orders) VALUES (1000), (2147483647), (-2147483648);

        SELECT * FROM example_int;
        ```

    - `BIGINT`: A large integer with a range of -9223372036854775808 to 9223372036854775807 (signed) or 0 to 18446744073709551615 (unsigned). BIGINT is used for very large integers and is often seen in databases requiring a vast numerical range, such as for high-volume financial applications or scientific computations. Here’s an example at play:

        ```
        CREATE TABLE example_bigint (
            id INT AUTO_INCREMENT PRIMARY KEY,
            stars_count BIGINT NOT NULL
        );

        INSERT INTO example_bigint (stars_count) VALUES (9000000000), (9223372036854775807), (-9223372036854775808);

        SELECT * FROM example_bigint;
        ```

  - Range depends on subtype and sign (e.g., `INT` ranges from -2,147,483,648 to 2,147,483,647 for signed).

- **DECIMAL (NUMERIC):**
  - Stores exact numeric values with fixed precision and scale.
  - Precision refers to the total number of digits, and scale refers to the number of digits after the decimal point.
  - Example: `DECIMAL(10, 2)` can store values like 12345678.90.

        ```
        CREATE TABLE example_numeric (
            id INT AUTO_INCREMENT PRIMARY KEY,
            price DECIMAL(10, 2) NOT NULL,
            weight NUMERIC (8, 3) NOT NULL
        );

        INSERT INTO example_decimal (price, weight) VALUES

        (1234567.89, 75.250), (9876.54, 100.750), (123.45, 0.500);
        
        SELECT * FROM example_decimal;
        ```

- **FLOAT:**
  - Stores approximate numeric values with floating-point precision.
  - Less precise than `DECIMAL`, but more storage-efficient.
  - Used for scientific calculations.

        ```
        CREATE TABLE example_float (
            id INT AUTO_INCREMENT PRIMARY KEY,
            temperature FLOAT NOT NULL
        );

        INSERT INTO example_float (temperature) VALUES 
        (98.6),
        (-40.5),
        (212.0);

        SELECT * FROM example_float;
        ```

- **DOUBLE:**
  - Similar to `FLOAT`, but with double the precision.
  - Suitable for applications requiring high precision in calculations.

        ```
        CREATE TABLE example_double (
            id INT AUTO_INCREMENT PRIMARY KEY,
            scientific_calculation DOUBLE NOT NULL
        );

        INSERT INTO example_double (scientific_calculation) VALUES 
        (1.7976931348623157E308), (2.2250738585072014E-308), (3.141592653589793);

        SELECT * FROM example_double;
        ```

- **BIT:**
  - Stores binary values (0 or 1).
  - Used for boolean or binary data.

        ```
        CREATE TABLE example_bit (
            id INT AUTO_INCREMENT PRIMARY KEY,
            is_active BIT(1) NOT NULL,
            flags BIT(3) NOT NULL
        );

        INSERT INTO example_bit (is_active, flags) VALUES 
        (b'1', b'101'), (b'0', b'010'), (b'1', b'111');

        SELECT 
            id, 
            is_active, 
            flags,
            BIN(flags) AS flags_binary
        FROM example_bit;
        ```
### 2. Character String Data Types

Character string data types are used to store alphanumeric text.

- **CHAR(n):**
    - Fixed-length string. Always uses the same amount of space, padding with spaces if necessary.
    - Use Case: CHAR is ideal for storing data that has a consistent length, such as country codes, or fixed-length codes like a two-character state abbreviation.

    ```
    CREATE TABLE example_char (
        id INT AUTO_INCREMENT PRIMARY KEY,
        country_code CHAR(2) NOT NULL
    ):

    INSERT INTO example_char (country_code) 
    VALUES ('US'), ('CA'), ('UK');
    ```

- **VARCHAR(n):**
    - Variable-length string. More flexible and space-efficient than CHAR.
    - Use Case: `VARCHAR` is suitable for storing data with varying lengths, such as names, email addresses, or descriptions.

    ```
    CREATE TABLE example_varchar (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL
    );

    INSERT INTO example_varchar (name) 
    VALUES ('Alice'), ('Pius'), ('Bob');
    ```

- **TEXT:**
    - Stores large amounts of text data. Does not require a length to be specified.
    - Use Case: TEXT is useful for storing large texts like articles, comments, or descriptions where the length may be unpredictable.
    - Different subtypes include `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, and `LONGTEXT` based on size.

        - `TINYTEXT` can store number of characters up to 255 ( 2^8 = 256, 1 byte overhead). In practice, you use TINYTEXT for the column that requires less than 255 characters, has inconsistent length, and does not require sorting. For example, you can use the TINYTEXT to store the excerpt of a blog post.

        ```
        CREATE TABLE articles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            summary TINYTEXT
        );
        ```

        - `TEXT` data type can hold up to 64 KB which is equivalent to 65535 (2^16 – 1) characters. The TEXT datatype also requires 2 bytes overhead.

        ```
        ALTER TABLE articles 
        ADD COLUMN body TEXT NOT NULL
        AFTER summary;
        ```
        
        - `MEDIUMTEXT` can hold up to 16MB text data which is equivalent to 16,777,215 characters. It requires 3 bytes overhead. The MEDIUMTEXT is useful for storing quite large text data like the text of a book, white papers, etc. For example:
        
        ```
        CREATE TABLE whitepapers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            body MEDIUMTEXT NOT NULL,
            published_on DATE NOT NULL
        ); 
        ```
        
        - `LONGTEXT` can store text data up to 4GB, which is quite big in common scenarios. It has 4 bytes overhead.

## 3. Binary Data Types

Binary data types are used to store binary data such as images, files, or encrypted data.

- **BINARY(n):**
    - Fixed-length binary data. Similar to CHAR, but stores binary bytes instead of characters. `BINARY` is suitable for storing fixed-length binary data such as encrypted values or hashes.

    ```
    CREATE TABLE example_binary (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hash BINARY(16) NOT NULL
    );

    INSERT INTO example_binary (hash) VALUES (UNHEX('5d41402abc4b2a76b9719d911017c592')), (UNHEX('5f4dcc3b5aa765d61d8327deb882cf99'));
    ```

- **VARBINARY(n):**
    - Variable-length binary data. Similar to VARCHAR, but stores binary bytes instead of characters. It is used for storing variable-length binary data like media files, images, or documents.

    ```
    CREATE TABLE example_varbinary (
        id INT AUTO_INCREMENT PRIMARY KEY,
        file_data VARBINARY(255) NOT NULL
    );

    INSERT INTO example_varbinary (file_data) VALUES 
    (UNHEX('FFD8FFE000104A46494600010101006000600000')),
    (UNHEX('FFD8FFE000104A46494600020101006000600000'));
    ```

- **BLOB (Binary Large Object):**
    - It’s used for storing binary data and for the columns of high-capacity binary storage. You can store any file type including PDF documents, MP3 Files and Video Files.
    - Different subtypes include `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, and `LONGBLOB`.
    
        - `TINYBLOB` is used to store blob files of a maximum length of 255 (2^8 - 1) bytes. Each TINYBLOB value is stored using a one-byte length prefix that indicates the number of bytes in the value.

        ```

        ```
        
        - `BLOB`: Maximum length of 65535 (2^16 - 1) bytes, or 64KB in storage. Each BLOB value is stored using a two-byte length prefix that indicates the number of bytes in the value.
        
        ```

        ```

        - `MEDIUMBLOB`: Maximum length of 16777215 (2^24 - 1) bytes, or 16MB in storage. Each MEDIUMBLOB value is stored using a three-byte length prefix that indicates the number of bytes in the value.
        
        ```

        ```

        - `LONGBLOB`: Maximum length of 4294967295 (2^32 - 1) bytes, or 4GB in storage. Each LONGBLOB value is stored using a four-byte length prefix that indicates the number of bytes in the value.

        ```

        ```

## 4. Date and Time Data Types

Date and time data types are used to store temporal data.

- **DATE:**
  - Stores date values (year, month, day).
  - Format: `YYYY-MM-DD`.

- **TIME:**
  - Stores time values (hours, minutes, seconds).
  - Format: `HH:MM:SS`.

- **DATETIME:**
  - Stores both date and time values.
  - Format: `YYYY-MM-DD HH:MM:SS`.

- **TIMESTAMP:**
  - Stores both date and time values, typically used to track changes in records.
  - Automatically updates to the current date and time when the record is modified.

- **YEAR:**
  - Stores a year in two or four digits.
  - Example: `YEAR(4)` for years like `2023`.

## 5. Boolean Data Type

- **BOOLEAN (or BOOL):**
  - Stores a boolean value (TRUE or FALSE).
  - Typically implemented as `TINYINT(1)`, where 0 is FALSE and 1 is TRUE.

## 6. Spatial Data Types

Spatial data types are used to store geometric and geographical data.

- **GEOMETRY:**
  - General-purpose type for spatial data.

- **POINT:**
  - Represents a single point in space.

- **LINESTRING:**
  - Represents a sequence of points forming a continuous line.

- **POLYGON:**
  - Represents a closed shape with multiple points.

## 7. JSON Data Type

- **JSON:**
  - Stores JSON (JavaScript Object Notation) formatted data.
  - Allows storage of semi-structured data in a text format that can be easily queried.

## 8. XML Data Type

- **XML:**
  - Stores XML (Extensible Markup Language) formatted data.
  - Suitable for storing and querying hierarchical data.

## 9. ENUM and SET Data Types

These data types are used to store predefined lists of values.

- **ENUM:**
  - Stores a single value from a predefined list of possible values.
  - Example: `ENUM('small', 'medium', 'large')`.

- **SET:**
  - Stores multiple values from a predefined list of possible values.
  - Example: `SET('red', 'green', 'blue')`.

## 10. UUID Data Type

- **UUID:**
  - Stores Universally Unique Identifier values.
  - Used for generating unique keys across databases and systems.



Using the Spotflix example, a table can be created as shown below:
```
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    role VARCHAR(255),
    team VARCHAR (255),
    full_time BOOLEAN,
    office VARCHAR(255)
);
```
The next phase will be for data scientists. i.e, to get first and last name of employees with job title with key word 'Data',

```
SELECT
    first_name, 
    last_name
FROM employees
WHERE role LIKE '%Data%'
```
The database schema governs how tables are related as shown below

```
![Relationships Diagram](https://github.com/Ppius6/Data-Engineering/blob/master/SQL/Relationships.png)
```

The SQL platforms include
- SQLite
- MySQL
- PostgreSQL
- Oracle SQL
- SQL Server



Example queries

```
-- Getting the names in patrons table
SELECT name
FROM patrons;

-- Getting multiple fields
SELECT card_num, name
FROM patrons;

-- Selecting all
SELECT *
FROM patrons;

-- Aliasing columns for clarity
SELECT name as first_name, year_hired
FROM employees;

-- Getting distinct records
-- Getting unique years employees were hired
SELECT DISTINCT year_hired
FROM employees
```

A `view` is a virtual table that is the result of a saved SQL SELECT statement. 

When accessed, views automatically update in response to updates in the underlying data.

```
-- Creating a view
CREATE VIEW employee_hire_years AS
SELECT id, name, year_hired
FROM employees;

-- Using the view
SELECT id, name
FROM employee_hire_years
```

`SQL flavors` are free and paid, used with relational databases, with vast majority of the keywords being the same. They must follow universal standards amd only the additions on top of these standards make flavors different. 

Two popular SQL flavors;
1. `PostgreSQL`
    - It is free and open-source relational database system created at the University of California, Berkeley. 
    - PostgreSQL refers to both the PostgreSQL database system and its associated SQL flavor.
2. `SQL Server`
    - It is free and paid, created by Microsoft. T-SQL is Microsoft's SQL flavor, used with SQL Server databases.

The differences are more of dialects, names used are not similar. 

## Querying

### COUNT()
Counts the number of records with a value in a field

```
-- Retrieving number of birth dates
SELECT COUNT(birthdate) AS count_birthdates
FROM people;

-- Counting multiple fields
SELECT COUNT(name) AS count_names, COUNT(birth_date) AS count_birthdates
FROM people;

-- Counting number of records in a table
SELECT COUNT(*) AS total_records
FROM people;
```

### DISTINCT

It removes duplicates to return only unique values

```
-- Languages in the films table, (unique languages)
SELECT DISTINCT language
FROM films;

-- Count with distinct
SELECT COUNT(DISTINCT birthdate) AS count_distinct_birthdates
FROM people;
```
- COUNT() includes duplicates
- DISTINCT excludes duplicates

How does SQL code work?
```
-- order of execution
SELECT name -- 2
FROM people -- 1
LIMIT 10; -- 3
```
### WHERE

It is a filtering clause. The operators include:
- `>` Greater than or after
- `<` Less than or before
- `=` Equal to
- `>=` Greater than or equal to
- `<=` Less than or equal to
- `<>` Not equal to

```
SELECT title
FROM films
WHERE year > 2010;

-- WHERE with strings includes:
SELECT title
FROM films
WHERE country = 'Japan';
```

### Multiple Criteria - OR, AND, BETWEEN
```
-- OR
SELECT *
FROM coats
WHERE color = 'yellow' OR length = 'short';

-- AND
SELECT *
FROM coats
WHERE color = 'yellow' AND 'length = 'short';

-- BETWEEN
SELECT *
FROM coats
WHERE buttons BETWEEN 1 AND 5;
```

The `OR` operator is used when you need to satisfy at least one condition.
```
- Example years 1994 or 2000
SELECT title
FROM films
WHERE release_year = 1994 
    OR release_year = 2000;
```

The `AND` operator is used when we need to satisfy the entire criteria.

```
-- Titles of films released between 1994 and 2000
SELECT title
FROM films
WHERE release_year >= 1994
    AND release_year <= 2000;

-- Alternatively
SELECT title
FROM films
WHERE release_year 
    BETWEEN 1994 AND 2000;
```

`AND` and `OR` can be combined. For example:

```
-- Filter for films released in 1994 or 1995, and certified PG or R.

SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
    AND (certification  = 'PG' OR certification = 'R');
```

Using `BETWEEN`, `AND`, and `OR` together:

```
SELECT title
FROM films
WHERE release_year
BETWEEN 1994 AND 2000 AND country = 'UK';
```

## Filtering Textual data

`LIKE` is used with the `WHERE` clause to search for a pattern in a field. 
- `%` is used to match zero, one, or many characters.

```
-- This query matches people with Ade in their name
SELECT name
FROM people
WHERE name LIKE 'Ade%';
```

- `_` matches a single character

```
-- This query matches a single character
SELECT name
FROM people
WHERE name LIKE 'Ev_';
```

- `NOT LIKE` is used to find records that do not match the specified pattern.

```
SELECT name
FROM people
WHERE name NOT LIKE 'A.%';
```

Finding data position-wise:

```
- Names ending with r
SELECT name
FROM people
WHERE name LIKE '%r';
```

```
- Names where third character is t
SELECT name
FROM people
WHERE name LIKE '%__t';
```

### WHERE IN
Used to find data in specific years:

```
-- Years
SELECT title
FROM films
WHERE release_year IN (1920, 1930, 1940);

-- Country
SELECT title
FROM films
WHERE country IN ('Germany', 'France');
```

## Working with NULL Values

Null represents a missing or unknown value. 

`IS NULL` is used to get the null values.

```
-- Returning null birthdates
SELECT name
FROM people
WHERE birthdate IS NULL;
```

`IS NOT NULL` is used to get results that are not null.

```
-- Returns people whose birth dates are not missing
SELECT COUNT(name) AS count_birthdates
FROM people
WHERE birthdate IS NOT NULL;
```

`NOTE`: `COUNT()` returns non-missing values too. 

## Summarizing Data

It is done using SQL aggregate functions which performs calculations on many values return a single value.

They include, `AVG(), SUM(), MIN(), MAX(), COUNT()`

It is recommend to use aliases. 

```
-- Average
SELECT AVG(budget) AS average_budget
FROM films;

-- Sum
SELECT SUM(budget) AS total_budget
FROM films;

-- Minimum
SELECT MIN(budget) AS Min_budget
FROM films;

-- Maximum
SELECT MAX(budget) AS max_budget
FROM films;

-- Count
SELECT COUNT(budget) AS count_budget
FROM films;

-- Selecting also non-numerical data
-- This would output country at the top of alphabet
SELECT MIN(country)
FROM films;

-- Last country in the list based on alphabet
SELECT MAX(country)
FROM films;
```

`WHERE` can also be used in aggregates

```
SELECT MAX(budget) AS max_budget
FROM films
WHERE release_year = 2010;
```

`ROUND` rounds a number to a specified decimal

```
-- To two decimals
SELECT ROUND(AVG(budget), 2) AS average_budget
FROM films
WHERE release_year >= 2010;

-- To zero
SELECT ROUND(AVG(budget), 0) AS average_budget
FROM films
WHERE release_year >= 2010;

-- Using a negative parameter
SELECT ROUND(AVG(budget), -4) AS average_budget
FROM films
WHERE release_year >= 2010;
```

## Sorting results

### ORDER BY

`ORDER BY` sorts results the results of one or more fields. It sorts from lowest to highest by default

```
SELECT title, budget
FROM films
ORDER BY budget;

-- Sorting ascending
SELECT title, budget
FROM films
ORDER BY budget ASC;

-- Sorting descending
SELECT title, budget
FROM films
ORDER BY budget DESC;

-- In case of missing values...
SELECT title, budget
FROM films
WHERE budget IS NOT NULL
ORDER BY budget DESC;
```

`NOTE`: It is important to include the field we are sorting on in the `SELECT` statement for clarity.

We can also sort by multiple fields considering field_two as a tie-breaker.

```
ORDER BY field_one, field_two

-- Example
SELECT title, wins, imdb_score
FROM best_movies
ORDER BY wins DESC, imdb_score DESC

-- Ordering in different orders
SELECT birthdate, name
FROM people
ORDER BY birthdate, name DESC;

-- SQL Query Execution Order
SELECT item - 3
FROM coats - 1
WHERE color = 'yellow' - 2
ORDER BY length - 4
LIMIT 3; - 5
```
### GROUP BY
Data can also be grouped by a field.

```
-- Grouping by a single field
SELECT certification, COUNT(title) AS title_count
FROM films
GROUP BY certification;
```
`NOTE`: An error appears if a field is selected that is not in the `GROUP BY` clause.

It can also be used on multiple fields

```
SELECT certification, language, COUNT(title) AS title_count
FROM films
GROUP BY certification, language;
```

`GROUP BY` and `ORDER BY` can be combined. `ORDER BY` is always written after `GROUP BY`.

```
SELECT
    certification,
    COUNT(title) AS title_count
FROM films
GROUP BY certification
ORDER BY title_count DESC
LIMIT 3;
```
### Filtering grouped data - HAVING

When using the `GROUP BY` clause, `HAVING` is used to filter the data. This is due to the order of execution which is;


```
SELECT
    certification,
    COUNT(title) AS title_count     -- 5
FROM films                          -- 1
WHERE certification                 -- 2
    IN ('G', 'PG, 'PG-13')
GROUP BY certification              -- 3
HAVING COUNT(title) > 10            -- 4
ORDER BY title_count DESC           -- 6
LIMIT 3;                            -- 7
```

So, `WHERE` is executed before `GROUP BY` and before aggregation occurs. It is also the reason we cannot use an ALIAS with `HAVING` but can do so with `ORDER BY`.

```
SELECT
    release_year,
    COUNT(title) AS title_count
FROM films
GROUP BY release_year
HAVING COUNT(title) > 10;
```

#### HAVING vs WHERE

`WHERE` filters individual records while `HAVING` filters grouped records.

For instance, in the question what films were released in the year 2000? 

```
SELECT title
FROM films
WHERE release_year = 2000;
```

In what years was the average film duration over two hours?

```
SELECT release_year, AVG(duration) AS average_duration
FROM films
GROUP BY release_year
HAVING average_duration > 2;
```

## INNER JOIN

`INNER JOIN` looks for records in both tables which match on a given field. Here, two tables are joined based on matching values in a specified column, in this case, the id field.

For instance, let us assume we have two tables; `left_table` and `right_table`. left_table contains two columns, `id` and `left_val`. 

The `id` column has values 1, 2, 3, and 4, with corresponding `left_val` values of L1, L2, L3, and L4 respectively. `right_table` contains two columns,`id` and `right_val`. The `id` column has values 1, 4, 5, and 6, with corresponding `right_val` values of R1, R2, R3, and R4 respectively.

The resulting table after performing the INNER JOIN on the id field includes:

- Columns: `id`, `left_val`, and `right_val`.
- Rows: Two rows where the `id` values match in both tables.
- The first row includes `id` value 1 with `left_val` L1 from `left_table` and `right_val` R1 from `right_table`.
- The second row includes `id` value 4 with `left_val` L4 from `left_table` and `right_val` R2 from `right_table`.

```
-- Inner join of presidents and prime_ministers, joining on country

SELECT prime_ministers.country, prime_ministers.continent, prime_minister, president
FROM prime_ministers  -- Left table
INNER JOIN presidents -- Right table
ON prime_ministers.country = presidents.country;
```

`NOTE`: When selecting columns that exist in both tables such as country and continent, the `table.column_name` format must be used to avoid a SQL error.

Aliasing can be used on tables

```
-- Inner join of presidents and prime_ministers, joining on country

SELECT p1.country, p1.continent, prime_minister, president
FROM prime_ministers AS p1  -- Left table
INNER JOIN presidents AS p2 -- Right table
ON p1.country = p2.country;
```

### Using USING

```
-- Inner join of presidents and prime_ministers, joining on country

SELECT p1.country, p1.continent, prime_minister, president
FROM prime_ministers AS p1  -- Left table
INNER JOIN presidents AS p2 -- Right table
USING(country);
```
## Relationships

- One-to-many relationship: Here, a single entity can be associated with many entities i.e, artists and their songs, a teacher and his students, authors and their books.

- One-to-one relationships: An entity can only be associated with a unique pairing i.e, finger and fingerprint.

- Many-to-many: Many entities are associated with many entities. For instance, many languages can be spoken in many countries.

## Multiple Joins

```
SELECT *
FROM left_table
INNER JOIN right_table
ON left_table.id = right_table.id
INNER JOIN another_table
ON left_table.id = another_table.id;
```

`NOTE:` Depending on the use case, `left_table` or `right_table` can be used in the `ON` clause.

For instance, when seeking to find countries with both president and prime_minister, and year each prime_minister came into office:

```
SELECT 
    p1.country, 
    p1.continent, 
    prime_minister, 
    president,
    pm_start
FROM prime_ministers AS p1  -- Left table
INNER JOIN presidents AS p2 -- Right table
USING(country)
INNER JOIN prime_minister_terms AS p3
USING (prime_minister);

```

A second key is always used when there's a need to return results that match on both i.e, id and date

```
SELECT *
FROM left_table
INNER JOIN right_table
ON left_table.id = right_table.id
    AND left_table.date = right_table.date;
```

## LEFT JOINS