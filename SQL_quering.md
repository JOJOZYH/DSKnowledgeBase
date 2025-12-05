---
title: SQL Querying Documentation (MySQL)
author: Yuhan Zhou
date: 10-09-2025
purpose: make a comprehensive doc on how to query in SQL
---

# SQL Querying Documentation (MySQL)
Note: the last 2 sections are trivial, don't read
- [SQL Querying Documentation (MySQL)](#sql-querying-documentation-mysql)
   - [SQL Execution Orders](#sql-execution-orders)
   - [Aggregation](#aggregation)
   - [joins](#joins)
      - [`JOIN`](#join)
      - [`LEFT JOIN` \& `RIGHT JOIN`](#left-join--right-join)
      - [semi-joins (半连接)](#semi-joins-半连接)
         - [anti-join (反连接) (anti-semi-join)](#anti-join-反连接-anti-semi-join)
         - [semi-joins using `EXIST` \& `NOT EXIST`](#semi-joins-using-exist--not-exist)
      - [cartesian product](#cartesian-product)
   - [CTEs (Common Table Expressions)](#ctes-common-table-expressions)
      - [naming column aliases for CTEs](#naming-column-aliases-for-ctes)
      - [`RECURSIVE` in CTEs](#recursive-in-ctes)
         - [Recursive by group](#recursive-by-group)
   - [Keywords](#keywords)
      - [Core Clauses](#core-clauses)
         - [1. `SELECT`](#1-select)
         - [2. `FROM`](#2-from)
         - [3. `JOIN`](#3-join)
         - [4. `WHERE`](#4-where)
         - [5. `GROUP BY`](#5-group-by)
         - [6. `HAVING`](#6-having)
         - [7. `LIMIT`](#7-limit)
         - [8. `OFFSET`](#8-offset)
   - [Functions](#functions)
      - [1. Scalar Functions](#1-scalar-functions)
      - [2. Aggregate Functions](#2-aggregate-functions)
         - [Common Aggregate Functions](#common-aggregate-functions)
      - [3. Window Functions](#3-window-functions)
         - [Bounding / Frame selection](#bounding--frame-selection)
   - [SQL data types](#sql-data-types)
   - [Operators](#operators)
      - [Arithmetic](#arithmetic)
      - [Logical](#logical)
      - [Comparison](#comparison)
   - [Flow Control](#flow-control)
      - [`IF()`](#if)
      - [`IFNULL()`](#ifnull)
      - [`CASE`](#case)
         - [`WHEN` / `ELSE` / `END`](#when--else--end)
      - [`NULLIF()`](#nullif)
      - [`COALESCE()`](#coalesce)
      - [`GREATEST()` / `LEAST()`](#greatest--least)
   - [Date Arithmetics](#date-arithmetics)
      - [datetime value types and their connections](#datetime-value-types-and-their-connections)
      - [Two Approaches](#two-approaches)
         - [1. Date Function Methods](#1-date-function-methods)
         - [2. Using Arithmetic Operators and `INTERVAL`](#2-using-arithmetic-operators-and-interval)
   - [Additional techniques](#additional-techniques)
      - [selecting scalar](#selecting-scalar)
         - [no table in query](#no-table-in-query)
      - [dummy agg\_funcs](#dummy-agg_funcs)
      - [pivoting using `IF()` or `CASE` and dummy agg\_funcs](#pivoting-using-if-or-case-and-dummy-agg_funcs)

---

## SQL Execution Orders

SQL statements in MySQL follow a **logical execution order** that explains why some expressions are (or are not) legal in certain clauses:

1. **`FROM` / `JOIN`** – Determine source tables/views; apply joins, subqueries, derived tables. See **[`FROM`](./SQL_keywords.md#from)**.
   1. *Alias of tables*: SQL has the alias of **tables** by `AS` in memory
2. **`WHERE`** – Row filtering (no aggregates/window allowed). See **[`WHERE`](./SQL_keywords.md#where)**.
3. **`GROUP BY`** – SQL builts the column list given for grouping. See **[`GROUP BY`](#group-by)**.
   - referencing columns using ordinal position or aliases:
      - SQL allows you to refer to columns from `SELECT` using aliases or ordinal position. When you reference a column from the `SELECT` list in `GROUP BY` it becomes part of the `GROUP BY` column list; the MySQL parser finds whatever you referred to from the `SELECT` list (by position or alias) and adds them to the `GROUP BY` list.
      - example:
         ```sql
         SELECT LEAST(from_id, to_id), GREATEST(from_id, to_id), ...
         FROM ... GROUP BY 1, 2;
         ```
         or
         ```sql
         SELECT LEAST(from_id, to_id) AS l, GREATEST(from_id, to_id) AS g, ...
         FROM ... GROUP BY l, g;
         ```
         becomes
         ```sql
         SELECT LEAST(from_id, to_id), GREATEST(from_id, to_id), ...
         FROM ...
         GROUP BY LEAST(from_id, to_id), GREATEST(from_id, to_id);
         ```
         where parser find whatever is refered by the position or aliases from the `SELECT` list and just put it under GROUP BY
         - Other systems (e.g., SQL Server, PostgreSQL, Oracle) do not allow that;
4. ***Aggregate functions*** (per-group): evaluated after `GROUP BY`, before output. See **[Aggregate Functions](#aggregate-functions)**.
5. **`HAVING`** – Group filtering (post-aggregation conditions). See **[`HAVING`](#having)**.
6. **`SELECT`** – Projection:
   1. **Window functions** (per-row over a window): computed during the construction of the SELECT list. See **[Window Functions](#window-functions)**.
   2. *Alias of columns*: SQL has the alias of **columns** by `AS` in memory
   > NOTE: window functions **doesn't have access** to column aliases!!!

7. **`DISTINCT`**: remove duplicates after the entire SELECT list is built. see [DISTINCT]
8. **`UNION`/`UNION ALL`** - Vertically concatenate 2 table with same number of columns. see [here]
9.  **`ORDER BY`** – Sort result; may reference aliases, aggregates, window results. See **[`ORDER BY`](#order-by-1)**.
10. **`LIMIT` / `OFFSET`** – Return subset of sorted rows. See **[`LIMIT` / `OFFSET`](#limit--offset)** and **[`OFFSET`](#offset)**.
    
> **NOTE**: **Scalar functions** are being computed **per row**, and can be applied almost every where. But it is only being applied to the **current state** of the query execution, so be careful about how you design your query. [Functions](./SQL_functions.md#functions)
> **NOTE**: **`CASE WHEN ELSE END`** has the same behavior/execution logic as **scalar functions**


For a quick example, the following query:
```sql
SELECT id, g.name, AVG(grade) AS grade
FROM grades AS g
WHERE school_year = '2024'
GROUP BY id, g.name
HAVING MAX(grade) >= 80
ORDER BY grade DESC, id
LIMIT 5
OFFSET 1
```
Means:

- From the table named 'grades', aliased as 'g'
- Filter to only the 2024 school year
- Aggregate using column {id, g.name}, compute the average of the grade column (find mean grade)
- Filter to only the students who have their best grade above 80
- Order by mean grade in descending order, then by id in ascending order
- Limit the result to 5 rows, omitting the first row

Which shows the top 5 student with the highest grade averaged across all courses, ignoring the valedictorian, with the condition that only students who's best grade above 80 can join the rank latter

---
## Aggregation
- How it works:
   - rows are grouped based on the columns specified in the `GROUP BY` clause
   - each group becomes a single unit (one row) after aggregation, this means that the table is **collapsed** into fewer rows, and all upcoming operations are performed on **this state (collapsed)** of the table 
> **NOTE**: If you aggregate the table, the best practice is to include **only** columns that:
> 1. are being **aggregated** (using aggregate functions like `SUM()`, `COUNT()`, etc.), or
> 2. your **aggregation depends on** 
> as the list of columns under the **`SELECT`** clause, since other columns will either **cause an error** or have **arbitrary values**!
> 
> **Code Examples**:
> ```sql
> -- Valid: dept is in GROUP BY, COUNT(*) is an aggregate function
> SELECT dept, COUNT(*) as employee_count
> FROM employees
> GROUP BY dept;
>
> -- Invalid: name is neither in GROUP BY nor an aggregate function
> SELECT dept, name, COUNT(*)
> FROM employees
> GROUP BY dept;
> ``` 

---
## joins
### `JOIN`
- Returns one row per matching pair (A-row, B-row).
- If one row in A matches multiple rows in B, that A row will appear multiple times
### `LEFT JOIN` & `RIGHT JOIN`
### semi-joins (半连接)
- The set of rows from A for which **at least one matching row exists** in B, based on a join condition, but WITHOUT returning any columns from B.
- pattern
   ```sql
   SELECT DISTINCT A.*
   FROM A
   JOIN B ON B.key = A.key;
   ```
#### anti-join (反连接) (anti-semi-join)
- The set of rows from A for which **has no matching rows** exist in B, based on a join condition, but WITHOUT returning any columns from B.
- pattern
   ```sql
   SELECT A.*
   FROM A
   LEFT JOIN B
      ON B.key = A.key
   WHERE B.key IS NULL;
   ```
   `LEFT JOIN` produces NULL rows when the join condition matches zero B rows, and NULLs in B.key cause match failures.
#### semi-joins using `EXIST` & `NOT EXIST`
- `EXIST` for semi-join
   ```sql
   SELECT A.*
   FROM A
   WHERE EXISTS (
      SELECT 1 FROM B WHERE B.id = A.id
   );
   ```
- `NOT EXIST` for anti-join (anti semi-join)
   ```sql
   SELECT A.*
   FROM A
   WHERE NOT EXISTS (
      SELECT 1 FROM B WHERE B.id = A.id
   );
   ```

### cartesian product


## CTEs (Common Table Expressions)
- CTEs are temporary result sets defined within the execution scope of a single `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. They can be thought of as named subqueries that can be referenced multiple times within the main query.

### naming column aliases for CTEs
- You can name the column aliases of a CTE by specifying them in parentheses right after the CTE name. For example:
```sql
WITH cte_name (col1_alias, col2_alias) AS (
   SELECT col1, col2
   FROM some_table
)
SELECT col1_alias, col2_alias
FROM cte_name;
```

### `RECURSIVE` in CTEs
- You can create recursive CTEs by adding the `RECURSIVE` keyword after `WITH`. Recursive CTEs are useful for hierarchical or tree-structured data. 
- anchor
   - the row serve as the anchor to the recursive table, can have multiple columns in the anchor to make each group a independent recursion stream
- Syntax:
   ```sql
   WITH RECURSIVE cte_name AS (
      -- 1️⃣ Base query (anchor member)
      SELECT ... FROM ...

      UNION ALL

      -- 2️⃣ Recursive query (recursive member)
      SELECT ...
      FROM cte_name
      WHERE <stopping condition>
   )
   ```
- Example:
   ```sql

   WITH RECURSIVE EmployeeHierarchy AS (
      -- Anchor member: select top-level managers
      SELECT id, name, manager_id, 0 AS level
      FROM employees
      WHERE manager_id IS NULL
      
      UNION ALL
      
      -- Recursive member: select employees under the current level
      SELECT e.id, e.name, e.manager_id, eh.level + 1
      FROM employees e
      JOIN EmployeeHierarchy eh ON e.manager_id = eh.id
   )
   ```
#### Recursive by group


---

## Keywords
see all keywords in [SQL Keywords](./SQL_keywords.md#sql-keywords)
### Core Clauses

#### 1. `SELECT`
- Defines which columns/expressions to return. 
- selecting all columns: `SELECT * FROM ...`
- selecting all columns from a table: `SELECT t.* FROM t JOIN t2 USING (...)`

#### 2. `FROM`
- Declares data sources; supports joins, subqueries, derived tables, CTEs.
- Selecting multiple table forms a **Cartesian Product** of the tables, which is also equivalent to [`CROSS JOIN`](./SQL_keywords.md#cross-join)

#### 3. `JOIN`
- Combine rows across tables by condition. 
- Types of Join
  - blank

#### 4. `WHERE`
- Row-level filtering before grouping; see **[`WHERE`](./SQL_keywords.md#where)**.

#### 5. `GROUP BY`

#### 6. `HAVING`
**[Aggregate Functions](./SQL_functions.md#aggregate-functions)** and **[`HAVING`](./SQL_keywords.md#having)**.
Filter used on column after aggregation

#### 7. `LIMIT`
- Return at most N rows; see **[`LIMIT`](./SQL_keywords.md#limit--offset)**.

#### 8. `OFFSET`
- Skip N rows before returning results; see **[`OFFSET`](./SQL_keywords.md#limit--offset)**.

---

## Functions
(see **[Functions](./SQL_functions.md#functions)**)

### 1. Scalar Functions
- Operate on single values per row. (see **[Scalar Functions](./SQL_functions.md#scalar-functions)**)
- Common: `CONCAT()`, `SUBSTRING()`, `LENGTH()`, `UPPER()`, `LOWER()`, `ROUND()`, `FLOOR()`, `CEIL()`, `NOW()`, `DATE()`, `TIME()`, `DATEDIFF()`, `IF()`, `COALESCE()`, `CAST()`.

### 2. Aggregate Functions

Perform calculations across multiple rows per group; return one value per group. See **[Aggregate Functions](./SQL_functions.md#aggregate-functions)**.

#### Common Aggregate Functions

* `SUM()` – Sum of numeric expression. See **[`SUM()` ](./SQL_functions.md#sum)**.
* `COUNT()` – Row/non-NULL count. See **[`COUNT()` ](./SQL_functions.md#count)**.
* `AVG()` – Mean of values. See **[`AVG()` ](./SQL_functions.md#avg)**.
* `MIN()` / `MAX()` – Extremes. See **[`MIN()` ](./SQL_functions.md#min)**, **[`MAX()` ](./SQL_functions.md#max)**.
* `STDDEV_POP()` / `STDDEV_SAMP()` – Standard deviation. See **[`STDDEV_POP()` ](#stddev_pop)**, **[`STDDEV_SAMP()` ](./SQL_functions.md#stddev_samp)**.
* `VAR_POP()` / `VAR_SAMP()` – Variance. See **[`VAR_POP()` ](./SQL_functions.md#var_pop)**, **[`VAR_SAMP()` ](./SQL_functions.md#var_samp)**.
* `GROUP_CONCAT()` – Concatenate values per group. See **[`GROUP_CONCAT()` ](./SQL_functions.md#group_concat)**.

### 3. Window Functions
 - Compute values over a related set of rows without collapsing them. (see **[Window Functions](./SQL_functions.md#window-functions)**)
 - Common: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()`, `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()`, `NTH_VALUE()`, `CUME_DIST()`, `PERCENT_RANK()`.
#### Bounding / Frame selection
- **Syntax**
  - `{RANGE | ROWS | GROUPS} BETWEEN <frame_start> AND <frame_end>`
- `RANGE`, `ROWS`, `GROUPS` 
   - Define window frame boundaries
   - `ROWS`: physical row count
   - `RANGE`: value-based range
      - **Use with `INTERVAL`**, see datetime units [here](./SQL_keywords.md#datetime-value-types)
      - **NOTE!!!**: For a `RANGE … INTERVAL` frame, MySQL requires the window’s ORDER BY to be exactly one expression whose type is **numeric** or **temporal**
      - **NO AUTO CASTING FROM STRING TO DATE!!**
   - `GROUPS`: peer groups with same `ORDER BY` values
- `BETWEEN`&`AND`, {`PRECEDING`, `CURRENT`, `FOLLOWING`} & `UNBOUNDED` & `ROW` 
   - Position specifiers for window frames 
   - `PRECEDING`/`FOLLOWING`: relative to current row
   - `UNBOUNDED`: no bound
   - `CURRENT ROW`: current position
   > **NOTE**: `BETWEEN`&`AND` and `CURRENT ROW` can be omitted if no forward frames selected, for example, `RANGE BETWEEN INTERVAL 7 DAY PRECEDING AND CURRENT ROW` is equivalent to `RANGE INTERVAL 7 DAY PRECEDING`

---

## SQL data types
- Numeric
   - `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`/`INTEGER`, `BIGINT`
   - `DECIMAL`/`NUMERIC`
   - `FLOAT`, `DOUBLE`
- Date and Time
   - `DATE`
   - `DATETIME`
   - `TIMESTAMP`
   - `TIME`
   - `YEAR`
- String
   - `CHAR`
   - `VARCHAR`
   - `BINARY`
   - `VARBINARY`
   - `TEXT`
   - `BLOB`
   - `ENUM`
   - `SET`
- casting
   - CAST(expr AS type)
   - CONVERT(expr, type)
   - CONVERT(expr USING charset)

---
## Operators  
- See also **[Logical & arithmetic operators](./SQL_keywords.md#logical--arithmetic-operators)**.
### Arithmetic
- `+`, `-`, `*`, `/`, `%` (modulo).

### Logical
- `AND`, `OR`, `NOT`, `XOR`.
> **note on order of evaluation**: SQL evaluates operators in this order (highest → lowest):
> 1. `NOT`
> 2. `AND`
> 3. `OR`
> 
> This means that:
> - `AND` binds tighter than `OR`; `AND` expressions are grouped first if without parentheses.
> > Example:
> > ```sql
> > WHERE (c.caller_id = p.id OR c.callee_id = p.id)
> >   AND LEFT(p.phone_number, 3) = co.country_code
> > ```
> > IS NOT EQUIVALENT TO:
> > ```sql
> > WHERE c.caller_id = p.id OR c.callee_id = p.id
> >   AND LEFT(p.phone_number, 3) = co.country_code
> > --- equivalent to:
> > WHERE c.caller_id = p.id
> >   OR (c.callee_id = p.id AND LEFT(p.phone_number, 3) = co.country_code)
> >```
> Use parentheses to ensure the intended order of evaluation.

### Comparison 
- `=`, `<`, `<=`, `>`, `>=` 
- `<>` & `!=` - Not equal operator. AS `!` is deprecated in SQL standard, use `<>` .



---

## Flow Control

Conditional expressions for branching in queries.

### `IF()`

Return one of two values based on a condition. Example: `IF(score>=60,'Pass','Fail')`. Type: **Scalar**.

### `IFNULL()`

Return second argument if first is `NULL`. Example: `IFNULL(comment,'No comment')`. Type: **Scalar**. See also **[COALESCE()](#coalesce)**.

### `CASE`

Multi-branch conditional. Example: `CASE WHEN x>0 THEN 'pos' ELSE 'non-pos' END`. Type: **Scalar**. See also **[`CASE` ](#case-1)**.

#### `WHEN` / `ELSE` / `END`

Parts of `CASE`. See **[`CASE` ](#case-1)**.

### `NULLIF()`

Return `NULL` if arguments compare equal, else first argument. Example: `NULLIF(den,0)`. Type: **Scalar**. See also **[COALESCE()](#coalesce)**.

### `COALESCE()`

Return first non-`NULL` among arguments. Example: `COALESCE(nickname,username,'anon')`. Type: **Scalar**. See also **[`COALESCE` ](#coalesce-1)**.

### `GREATEST()` / `LEAST()`

Return max/min across arguments. Example: `LEAST(GREATEST(v,lo),hi)`. Type: **Scalar**.

---

## Date Arithmetics
MySQL provides several ways to perform date arithmetic. Here's a comprehensive overview:
see also [Arithmetic](#arithmetic-1)
### datetime value types and their connections
  1. DATE, DATETIME and TIME type
  2. TIMESTAMP type
  3. Differences
  4. ***Auto-Casting***
     1. date arithmetic allows for auto cast between 'datetime like' string and stricty DATETIME values
### Two Approaches
#### 1. Date Function Methods 
   1. `DATE_ADD()`/`ADDDATE()` and `DATE_SUB()`/`SUBDATE()` vs. `TIMESTAMPADD()`
   ```sql
   -- Add 3 days
   SELECT DATE_ADD('2025-10-13', INTERVAL 3 DAY);
   -- Subtract 3 days
   SELECT DATE_SUB('2025-10-13', INTERVAL 3 DAY);
   -- These are equivalent to DATE_ADD and DATE_SUB
   SELECT ADDDATE('2025-10-13', INTERVAL 3 DAY);
   SELECT SUBDATE('2025-10-13', INTERVAL 3 DAY);
   -- Using column values with DATE_ADD
   SELECT DATE_ADD(start_date, INTERVAL duration DAY) FROM events;
   -- Using column values with DATE_SUB
   SELECT DATE_SUB(end_date, INTERVAL duration DAY) FROM events;
   -- Using variables
   SET @days = 5;
   SELECT DATE_ADD('2025-10-13', INTERVAL @days DAY);
   SELECT DATE_SUB('2025-10-13', INTERVAL @days DAY);
   ```
   2. `DATEDIFF()` vs. `TIMESTAMPDIFF()` 
   3. `NOW()` vs. `CURRENT_TIMESTAMP()`
   > Some `DATE` styled funcitons and `TIMESTAMP` styled functions can work on both types of values and have **completely identical** functionality but **not all** TIMESTAMP functions can be used with `DATETIME`/`DATE`/`TIME` types

   - TIMESTAMP Family Functions

   | Function Signature                | Description                               | DATE | TIME | DATETIME | TIMESTAMP |
   |-----------------------------------|-------------------------------------------|:----:|:----:|:--------:|:---------:|
   | TIMESTAMPADD(unit, int, datetime) | Add interval to date/time                 |      |      |    1     |    1      |
   | TIMESTAMPDIFF(unit, dt1, dt2)     | Difference between two date/times in units|      |      |    1     |    1      |
   | UNIX_TIMESTAMP(datetime)          | Convert to Unix timestamp                 |      |      |    1     |    1      |
   | FROM_UNIXTIME(int)                | Convert Unix timestamp to datetime        |      |      |    1     |    1      |
   | CONVERT_TZ(datetime, from, to)    | Convert datetime between time zones       |      |      |    1     |    1      |
   | CURRENT_TIMESTAMP                 | Current date and time (session time zone) |      |      |    1     |    1      |
   | UTC_TIMESTAMP                     | Current UTC date and time                 |      |      |    1     |    1      |
   | UTC_DATE                          | Current UTC date                          |  1   |      |    1     |    1      |
   | UTC_TIME                          | Current UTC time                          |      |  1   |    1     |    1      |


   - DATE/DATETIME Family Functions

   | Function Signature                 | Description                              | DATE | TIME | DATETIME | TIMESTAMP |
   |------------------------------------|------------------------------------------|:----:|:----:|:--------:|:---------:|
   | DATE_ADD(date, INTERVAL expr unit) | Add interval to date/time                |  1   |  1   |    1     |    1      |
   | DATE_SUB(date, INTERVAL expr unit) | Subtract interval from date/time         |  1   |  1   |    1     |    1      |
   | ADDDATE(date, INTERVAL expr unit)  | Alias for DATE_ADD                       |  1   |  1   |    1     |    1      |
   | SUBDATE(date, INTERVAL expr unit)  | Alias for DATE_SUB                       |  1   |  1   |    1     |    1      |
   | DATEDIFF(later_dt, dt)             | Difference in days between two dates     |  1   |      |    1     |    1      |
   | EXTRACT(unit FROM date)            | Extract part of date/time                |  1   |  1   |    1     |    1      |
   | YEAR(date)                         | Extract year                             |  1   |      |    1     |    1      |
   | MONTH(date)                        | Extract month                            |  1   |      |    1     |    1      |
   | DAY(date)                          | Extract day                              |  1   |      |    1     |    1      |
   | HOUR(time)                         | Extract hour                             |      |  1   |    1     |    1      |
   | MINUTE(time)                       | Extract minute                           |      |  1   |    1     |    1      |
   | SECOND(time)                       | Extract second                           |      |  1   |    1     |    1      |
   | DATE(datetime)                     | Get date part                            |  1   |      |    1     |    1      |
   | TIME(datetime)                     | Get time part                            |      |  1   |    1     |    1      |
   | DAYNAME(date)                      | Name of the day                          |  1   |      |    1     |    1      |
   | MONTHNAME(date)                    | Name of the month                        |  1   |      |    1     |    1      |
   | DAYOFYEAR(date)                    | Day of year                              |  1   |      |    1     |    1      |
   | DAYOFMONTH(date)                   | Day of month                             |  1   |      |    1     |    1      |
   | DAYOFWEEK(date)                    | Day of week                              |  1   |      |    1     |    1      |
   | NOW()                              | Current date and time                    |      |      |    1     |    1      |

#### 2. Using Arithmetic Operators and `INTERVAL`
Code examples:
```sql
SELECT NOW() + INTERVAL 5 DAY;
---
SELECT dt + INTERVAL 6 MONTH 
```
  
---

## Additional techniques

### selecting scalar

#### no table in query

### dummy agg_funcs

### pivoting using `IF()` or `CASE` and dummy agg_funcs
- blank

---
Note: this documentation applies to MySQL 8.x