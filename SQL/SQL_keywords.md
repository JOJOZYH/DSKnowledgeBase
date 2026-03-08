## Keywords

> The keywords are group by **what data they work on**, one keyword may appear under multiple subsections, as they serve different purpose when used in different syntax

### Datetime 

#### `INTERVAL`

#### Datetime Value types

##### `DATE`, `DATETIME` and `TIME`  
These three types form the standard date and time storage options in MySQL
- **`DATE`**:
  - **Format**: `'YYYY-MM-DD'`
  - **Example**: `'2025-10-13'`
- **`DATETIME`**:
  - **Format**: `'YYYY-MM-DD HH:MM:SS[.fraction]'`
  - **Example**: `'2025-10-13 14:30:00'` or `'2025-10-13 14:30:00.123456'`
- **`TIME`**:
  - **Format**: `'HH:MM:SS[.fraction]'`
  - **Example**: `'14:30:00'` or `'14:30:00.123456'` or `'-12:30:00'` (negative for durations)

##### `TIMESTAMP`
Can display date, time, or datetime, just like `DATE`, `DATETIME`, and `TIME`. The key difference lies in its time zone sensitivity and how it is stored internally
 - Key Differences
   - **Storage**: Internally, TIMESTAMP stores the value as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).
   - **Time Zone Sensitivity**: When you insert a TIMESTAMP value, MySQL converts it from the session's time zone to UTC for storage. When you retrieve the value, MySQL converts it back to the session's time zone for display.

#### Time Interval Units
Used in [date arithemetics](#date-arithmetics)
 - `MICROSECOND`
 - `SECOND`
 - `SECOND_MICROSECOND`
 - `MINUTE`
 - `MINUTE_MICROSECOND`
 - `MINUTE_SECOND`
 - `HOUR`
 - `HOUR_MICROSECOND`
 - `HOUR_SECOND`
 - `HOUR_MINUTE`
 - `DAY`
 - `DAY_MICROSECOND`
 - `DAY_SECOND`
 - `DAY_MINUTE`
 - `DAY_HOUR`
 - `WEEK`
 - `MONTH`
 - `QUARTER`
 - `YEAR`
 - `YEAR_MONTH`

> NOTE: TIMESTAMPDIFF() only accepts the single-unit names. Valid unit values (MySQL 8.x) are:
`
MICROSECOND
SECOND
MINUTE
HOUR
DAY
WEEK
MONTH
QUARTER
YEAR
`
> 
> The compound interval units are valid for `INTERVAL` and values in this form can also be inputs to `DATE_SUB(), DATE_ADD()`, etc. But are not valid as the first argument to `TIMESTAMPDIFF()`.

#### Code Example
```sql
SELECT 
    DATE_ADD('2025-01-01', INTERVAL 5 DAY) AS add_days,
    DATE_SUB('2025-01-01', INTERVAL 2 MONTH) AS sub_months,
    DATE_ADD('2025-01-01 10:00:00', INTERVAL '1:30' HOUR_MINUTE) AS add_time,
    DATE_ADD('2025-01-01', INTERVAL '2-3' YEAR_MONTH) AS add_year_month;
``` 

---

### Data retrieval & composition

#### `SELECT` 

Return rows/expressions from tables. Example: `SELECT col1, col2 FROM t`. See **[`SELECT`](#select)**.

#### `FROM` 

Specify data sources. Example: `FROM t1 JOIN t2 ON ...`. See **[`FROM`](#from)**.

#### `WHERE` 

Row filter before grouping. Example: `WHERE col > 0`. See **[`WHERE`](#where)**.

#### `GROUP BY` 

Create groups for aggregates. Example: `GROUP BY dept`. See **[`GROUP BY`](#group-by-1)**.

#### `HAVING` 

Filter groups after aggregation. Example: `HAVING COUNT(*)>1`. See **[`HAVING`](#having)**.

#### `ORDER BY` 

Sort rows. Example: `ORDER BY created_at DESC`.

#### `LIMIT` / `OFFSET` 

Restrict/skip rows. Example: `LIMIT 10 OFFSET 20`. See **[SQL Execution Orders](#sql-execution-orders)**.

#### `DISTINCT` 

Deduplicate rows in the projection. Example: `SELECT DISTINCT col FROM t`.

#### `UNION` 

Combine result sets (dedupe). Example: `SELECT ... UNION SELECT ...`. See **[`UNION`](#union)**.

#### `ALL` 

With `UNION`, keep duplicates. Example: `UNION ALL`. See **[`ALL`](#all)**.

#### `WITH` (CTE) 

Define common table expressions. Example: `WITH c AS (SELECT ...) SELECT ... FROM c`.

#### `WINDOW` 

Name a window for reuse. Example: `WINDOW w AS (PARTITION BY k ORDER BY t)`.

---

### Joins & predicates

#### `JOIN`

Join tables. Example: `JOIN t2 ON t1.k=t2.k`. See **[`JOIN`](#join)**.

#### `INNER` / `LEFT` / `RIGHT` / `CROSS`

Join types. Example: `LEFT JOIN t2 USING (k)`. See **[`FROM`](#from)**.

#### `NATURAL`

Join on same-named columns automatically. Example: `NATURAL JOIN t2`.

#### `ON` / `USING`

Join predicates. Example: `ON t1.k=t2.k` / `USING(k)`.

#### `CROSS JOIN` 

Cartesian product. Example: `CROSS JOIN t2`. See **[Cartesian Product](#cartesian-product)**.

---

### Predicates & Comparison operators

#### `ANY` / `SOME` / `ALL` 
- `ANY`
   - Scalar comparison `OR`
      ```sql 
      SELECT col FROM t WHERE col = ANY (subquery)
      ```
      is the same as check for each row from t if row == subquery.row `OR` row == subquery.row2 `OR` ...
- `ALL` 
   - Scalar comparison `AND`
      ```sql 
      SELECT col FROM t WHERE col <> ALL (subquery)
      ```
      is the same as check for each row from t if row <> subquery.row1 `AND` row <> subquery.row2 `AND` ...
- `SOME`
   - exactly the same as `ALL` just more logcally sound

#### `IN` / `NOT IN` 
- `IN`
   ```sql
   SELECT col FROM x WHERE col IN (subquery) 
   ```
   is exactly equivalent to 
   ```sql
   SELECT col FROM x WHERE col = ANY (subquery) 
   ```
- `NOT IN`
- Membership predicate. `WHERE col IN (...)`.
- **Tuple comparison**: `WHERE (col1, col2) IN (SELECT col3, col4 FROM ...)`

#### `EXISTS` / `NOT EXISTS` 
- Predicate for subquery existence. Example: `WHERE EXISTS (SELECT 1 ...)`.

> **NOTE**: `NOT IN` and `NOT EXIST` 
> 
> When using `NOT IN` with subqueries, be cautious of `NULL` values in the subquery result, as they can lead to unexpected results. If the subquery returns any `NULL` values, the entire `NOT IN` condition will evaluate to `UNKNOWN`, resulting in no rows being returned. To avoid this, using `IFNULL()` to handle null values in the subquery or use `NOT IN`.

#### `BETWEEN` / `NOT BETWEEN` 

Range predicate (inclusive). Example: `WHERE x BETWEEN 1 AND 10`.

#### `LIKE` / `NOT LIKE` 

 - `%` any sequence
 - `_` single character

Simple wildcard match. Example: `WHERE name LIKE 'A%'`.

#### `REGEXP` / `RLIKE` 

Regex match operator. Example: `WHERE name REGEXP '^[A-Z]+'`. See **[Regular Expression functions](#regular-expression-functions)**.

#### `IS NULL` / `IS NOT NULL` 

Null tests. Example: `WHERE col IS NOT NULL`.

Quantified comparison with subqueries. Example: `x > ALL (SELECT ...)`.

---

### Logical & arithmetic operators
> **NOTE**: MySQL has officially deprecated the non-standard logical operators: `!`, `&&`, and `||`, use the standard ones instead.

#### `AND` / `OR` / `NOT` / `XOR` 
- Boolean connectors. Example: `WHERE a AND (b OR NOT c)`.

#### `DIV` / `MOD` 
- Integer division and modulo. Example: `a DIV 2`, `a MOD 2`.

#### `||` (pipes) 
- Synonym in SQL mode `PIPES_AS_CONCAT` for concatenation. Example: `a || b`. Deprecated in standard SQL when used as `OR`.

#### `+`, `-`, `*`, `/`, `%`
- Arithmetic operators. Example: `a + b * c`.

#### `=`, `<`, `<=`, `>`, `>=`
- Comparison operators. Example: `a >= b`.



---

### Aliasing & naming

#### `AS` 

Rename columns/tables. Example: `SELECT col AS alias`.

---

### Sorting & null handling

#### `IS TRUE` / `IS FALSE` / `IS UNKNOWN` 

Three-valued logic tests. Example: `WHERE flag IS TRUE`.

#### `NULLS FIRST` / `NULLS LAST` 

Optional null sort modifiers (supported in window `ORDER BY`). Example: `ORDER BY x NULLS LAST`.

---

### Expressions & conditional logic 

#### `CASE` 

Conditional branching expression. Syntax: `CASE WHEN condition THEN expr [WHEN ...] [ELSE expr] END`.

#### `CAST` 

Convert a value to a specific data type. Syntax: `CAST(expr AS type)`.

#### `CONVERT` 

Convert a value (type or charset). Syntax: `CONVERT(expr, type)` or `CONVERT(expr USING charset)`.

#### `COALESCE` 

Return first non-`NULL` value. Syntax: `COALESCE(expr1, expr2, ...)`.

#### `NULLIF` 

Return `NULL` if two expressions are equal. Syntax: `NULLIF(expr1, expr2)`.

---

### Windowing-specific clauses

#### `OVER` 

 - Introduce a window specification for a window-capable function. Syntax: `fn(...) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

#### `PARTITION BY` 

 - Divide rows into partitions for window calculations. Syntax: `OVER (PARTITION BY key [ORDER BY ...])`.

#### Window Frame Units
See also [Keywords in Window Functions](#keywords-in-window-functions)
 - `ROWS`
   - Defines the window frame based on physical row positions. Counts a specific number of rows before and/or after the current row, regardless of their values.
   - ```sql
      SELECT SUM(amount) OVER (
        ORDER BY id
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS rows_sum
      FROM sales;
     ```
 - `RANGE`
   - Defines the window frame based on value ranges in the ORDER BY column. Includes all rows with values within a specified range of the current row's value.
   - ```sql
      SELECT SUM(amount) OVER (
        ORDER BY date
        RANGE BETWEEN INTERVAL 3 DAY PRECEDING AND CURRENT
        ) AS range_sum
      FROM sales;
     ```
 - `GROUPS`
   - Defines the window frame based on peer groups (rows with identical ORDER BY values). Operates on groups of rows that have the same ordering value rather than individual rows.
   - ```sql
      SELECT SUM(amount) OVER (
        ORDER BY category
        GROUPS BETWEEN 1 PRECEDING AND CURRENT ROW
        ) AS groups_sum
      FROM sales;
     ```

#### `PRECEDING`/`CURRENT`/`FOLLOWING`/`ROW`

#### `UNBOUNDED`

#### `NULLS FIRST` / `NULLS LAST` (window `ORDER BY`) 
 - Control null ordering within window `ORDER BY`. Syntax: `OVER (... ORDER BY expr NULLS LAST)`.

---

### Pattern matching & predicates (additions)

#### `ESCAPE` (with `LIKE`) 

Define an escape character for wildcard matches. Syntax: `col LIKE 'x!_%' ESCAPE '!'`.

#### `SOUNDS LIKE` 

Phonetic comparison using SOUNDEX. Syntax: `name SOUNDS LIKE 'smith'`.

---

### Set aggregation extensions

#### `WITH ROLLUP` 

Produce super-aggregate rows for `GROUP BY` hierarchies. Syntax: `GROUP BY c1, c2 WITH ROLLUP`. See **[`GROUP BY`](#group-by-1)**.

---

### Transactions & session (query-adjacent)

#### `START TRANSACTION` / `COMMIT` / `ROLLBACK` 

Transactional control. Example: `START TRANSACTION` ... `COMMIT`.

#### `SAVEPOINT` / `RELEASE SAVEPOINT` / `ROLLBACK TO SAVEPOINT` 

Partial transaction control. Example: `SAVEPOINT s1`.

#### `SET` 

Set variables/modes. Example: `SET sql_mode='ONLY_FULL_GROUP_BY'`.

#### `USE` 

Change default database. Example: `USE dbname`.

#### `EXPLAIN` 

Show execution plan. Example: `EXPLAIN SELECT ...`.

#### `SHOW` 

Inspect metadata. Example: `SHOW TABLES`.

---
Note: this documentation applies to MySQL 8.x
