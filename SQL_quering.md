---
title: SQL Querying Documentation (MySQL)
author: Yuhan Zhou
date: 10-09-2025
purpose: make a comprehensive doc on how to query in SQL
---

# SQL Querying Documentation (MySQL)
Note: the last 2 sections if trivial, don't read
- [SQL Querying Documentation (MySQL)](#sql-querying-documentation-mysql)
  - [SQL Execution Orders](#sql-execution-orders)
  - [Core Clauses](#core-clauses)
    - [`SELECT`](#select)
      - [Scalar Functions](#scalar-functions)
      - [Window Functions](#window-functions)
        - [`RANGE`/`ROWS`/`PRECEDING`/`CURRENT`](#rangerowsprecedingcurrent)
    - [`FROM`](#from)
      - [`JOIN`](#join)
      - [Cartesian Product](#cartesian-product)
    - [`WHERE`](#where)
    - [`GROUP BY`](#group-by)
      - [Aggregate Functions](#aggregate-functions)
        - [Common Aggregate Functions](#common-aggregate-functions)
    - [`HAVING`](#having)
    - [`LIMIT`](#limit)
      - [`OFFSET`](#offset)
  - [SQL data types](#sql-data-types)
  - [Operators](#operators)
    - [Arithmetic](#arithmetic)
    - [Logical](#logical)
  - [Flow Control](#flow-control)
    - [`IF()`](#if)
    - [`IFNULL()`](#ifnull)
    - [`CASE`](#case)
      - [`WHEN` / `ELSE` / `END`](#when--else--end)
    - [`NULLIF()`](#nullif)
    - [`COALESCE()`](#coalesce)
    - [`GREATEST()` / `LEAST()`](#greatest--least)
  - [Date Arithmetics](#date-arithmetics)
    - [Understanding each datetime object types and their connections](#understanding-each-datetime-object-types-and-their-connections)
    - [Date Function Methods](#date-function-methods)
  - [Functions](#functions)
    - [String \& Text](#string--text)
      - [`CONCAT()`](#concat)
      - [`CONCAT_WS()`](#concat_ws)
      - [`SUBSTRING()` / `SUBSTR()`](#substring--substr)
      - [`LEFT()` / `RIGHT()`](#left--right)
      - [`MID()`](#mid)
      - [`LENGTH()` / `CHAR_LENGTH()`](#length--char_length)
      - [`LOWER()` / `UPPER()`](#lower--upper)
      - [`TRIM()` / `LTRIM()` / `RTRIM()`](#trim--ltrim--rtrim)
      - [`REPLACE()`](#replace)
      - [`INSERT()`](#insert)
      - [`INSTR()` / `LOCATE()`](#instr--locate)
      - [`POSITION()`](#position)
      - [`REVERSE()`](#reverse)
      - [`LPAD()` / `RPAD()`](#lpad--rpad)
      - [`REPEAT()`](#repeat)
      - [Regular Expression functions](#regular-expression-functions)
      - [`FORMAT()`](#format)
      - [Code-point \& encoding](#code-point--encoding)
      - [`QUOTE()` / `UNQUOTE()`](#quote--unquote)
      - [`ELT()` / `FIELD()` / `FIND_IN_SET()`](#elt--field--find_in_set)
    - [Numeric \& Math](#numeric--math)
      - [`ABS()`](#abs)
      - [Rounding \& truncation](#rounding--truncation)
      - [Arithmetic \& mod](#arithmetic--mod)
      - [Logs \& exp](#logs--exp)
      - [Trig \& angles](#trig--angles)
      - [Random \& signs](#random--signs)
    - [Date \& Time](#date--time)
      - [Current date/time](#current-datetime)
      - [Construction \& extraction](#construction--extraction)
      - [Formatting \& parsing](#formatting--parsing)
      - [Arithmetic](#arithmetic-1)
      - [Unix epoch](#unix-epoch)
    - [JSON](#json)
      - [Creation \& inspection](#creation--inspection)
      - [Access \& search](#access--search)
      - [Mutation](#mutation)
      - [Validation \& utilities](#validation--utilities)
    - [Aggregate Functions](#aggregate-functions-1)
      - [`COUNT()`](#count)
      - [`SUM()`](#sum)
      - [`AVG()`](#avg)
      - [`MIN()`](#min)
      - [`MAX()`](#max)
      - [`STD()`](#std)
      - [`STDDEV()`](#stddev)
      - [`STDDEV_POP()`](#stddev_pop)
      - [`STDDEV_SAMP()`](#stddev_samp)
      - [`VAR_POP()`](#var_pop)
      - [`VAR_SAMP()`](#var_samp)
      - [`VARIANCE()`](#variance)
      - [`BIT_AND()`](#bit_and)
      - [`BIT_OR()`](#bit_or)
      - [`BIT_XOR()`](#bit_xor)
      - [`GROUP_CONCAT()`](#group_concat)
      - [`JSON_ARRAYAGG()`](#json_arrayagg)
      - [`JSON_OBJECTAGG()`](#json_objectagg)
    - [Window Functions](#window-functions-1)
      - [`COUNT()`](#count-1)
      - [`SUM()`](#sum-1)
      - [`AVG()`](#avg-1)
      - [`MIN()`](#min-1)
      - [`MAX()`](#max-1)
      - [`STD()`](#std-1)
      - [`STDDEV()`](#stddev-1)
      - [`STDDEV_POP()`](#stddev_pop-1)
      - [`STDDEV_SAMP()`](#stddev_samp-1)
      - [`VAR_POP()`](#var_pop-1)
      - [`VAR_SAMP()`](#var_samp-1)
      - [`VARIANCE()`](#variance-1)
      - [`BIT_AND()`](#bit_and-1)
      - [`BIT_OR()`](#bit_or-1)
      - [`BIT_XOR()`](#bit_xor-1)
      - [`ROW_NUMBER()`](#row_number)
      - [`RANK()`](#rank)
      - [`DENSE_RANK()`](#dense_rank)
      - [`NTILE(n)`](#ntilen)
      - [`LAG()`](#lag)
      - [`LEAD()`](#lead)
      - [`FIRST_VALUE()`](#first_value)
      - [`LAST_VALUE()`](#last_value)
      - [`NTH_VALUE()`](#nth_value)
      - [`CUME_DIST()`](#cume_dist)
      - [`PERCENT_RANK()`](#percent_rank)
    - [Information](#information)
      - [Metadata \& session](#metadata--session)
      - [Utility](#utility)
      - [Cryptographic \& hash](#cryptographic--hash)
  - [Keywords](#keywords)
    - [Datetime](#datetime)
      - [`INTERVAL`](#interval)
      - [Datetime Object types](#datetime-object-types)
        - [`DATE`, `DATETIME` and `TIME`](#date-datetime-and-time)
        - [`TIMESTAMP`](#timestamp)
      - [Time Interval Units](#time-interval-units)
      - [Code Example](#code-example)
    - [Data retrieval \& composition](#data-retrieval--composition)
      - [`SELECT`](#select-1)
      - [`FROM`](#from-1)
      - [`WHERE`](#where-1)
      - [`GROUP BY`](#group-by-1)
      - [`HAVING`](#having-1)
      - [`ORDER BY`](#order-by)
      - [`LIMIT` / `OFFSET`](#limit--offset)
      - [`DISTINCT`](#distinct)
      - [`UNION`](#union)
      - [`ALL`](#all)
      - [`WITH` (CTE)](#with-cte)
      - [`WINDOW`](#window)
    - [Joins \& predicates](#joins--predicates)
      - [`JOIN`](#join-1)
      - [`INNER` / `LEFT` / `RIGHT` / `CROSS`](#inner--left--right--cross)
      - [`NATURAL`](#natural)
      - [`ON` / `USING`](#on--using)
      - [`CROSS JOIN`](#cross-join)
      - [`EXISTS` / `NOT EXISTS`](#exists--not-exists)
      - [`IN` / `NOT IN`](#in--not-in)
      - [`BETWEEN` / `NOT BETWEEN`](#between--not-between)
      - [`LIKE` / `NOT LIKE`](#like--not-like)
      - [`REGEXP` / `RLIKE`](#regexp--rlike)
      - [`IS NULL` / `IS NOT NULL`](#is-null--is-not-null)
      - [`ANY` / `SOME` / `ALL`](#any--some--all)
    - [Logical \& arithmetic operators](#logical--arithmetic-operators)
      - [`AND` / `OR` / `NOT` / `XOR`](#and--or--not--xor)
      - [`DIV` / `MOD`](#div--mod)
      - [`||` / `OR` (pipes)](#--or-pipes)
    - [Aliasing \& naming](#aliasing--naming)
      - [`AS`](#as)
    - [Sorting \& null handling](#sorting--null-handling)
      - [`IS TRUE` / `IS FALSE` / `IS UNKNOWN`](#is-true--is-false--is-unknown)
      - [`NULLS FIRST` / `NULLS LAST`](#nulls-first--nulls-last)
    - [Expressions \& conditional logic](#expressions--conditional-logic)
      - [`CASE`](#case-1)
      - [`CAST`](#cast)
      - [`CONVERT`](#convert)
      - [`COALESCE`](#coalesce-1)
      - [`NULLIF`](#nullif-1)
    - [Windowing-specific clauses](#windowing-specific-clauses)
      - [`OVER`](#over)
      - [`PARTITION BY`](#partition-by)
      - [`ROWS` / `RANGE` / `GROUPS`](#rows--range--groups)
      - [`NULLS FIRST` / `NULLS LAST` (window `ORDER BY`)](#nulls-first--nulls-last-window-order-by)
    - [Pattern matching \& predicates (additions)](#pattern-matching--predicates-additions)
      - [`ESCAPE` (with `LIKE`)](#escape-with-like)
      - [`SOUNDS LIKE`](#sounds-like)
    - [Set aggregation extensions](#set-aggregation-extensions)
      - [`WITH ROLLUP`](#with-rollup)
    - [Transactions \& session (query-adjacent)](#transactions--session-query-adjacent)
      - [`START TRANSACTION` / `COMMIT` / `ROLLBACK`](#start-transaction--commit--rollback)
      - [`SAVEPOINT` / `RELEASE SAVEPOINT` / `ROLLBACK TO SAVEPOINT`](#savepoint--release-savepoint--rollback-to-savepoint)
      - [`SET`](#set)
      - [`USE`](#use)
      - [`EXPLAIN`](#explain)
      - [`SHOW`](#show)

---

## SQL Execution Orders

SQL statements in MySQL follow a **logical execution order** that explains why some expressions are (or are not) legal in certain clauses:

1. **`FROM` / `JOIN`** – Determine source tables/views; apply joins, subqueries, derived tables. See **[`FROM`](#from)**.
2. **`WHERE`** – Row filtering (no aggregates/window allowed). See **[`WHERE`](#where)**.
3. **`GROUP BY`** – Form groups for aggregation. See **[`GROUP BY`](#group-by)**.
4. **Aggregate functions** (per-group): evaluated after `GROUP BY`, before output. See **[Aggregate Functions](#aggregate-functions)**.
5. **`HAVING`** – Group filtering (post-aggregation conditions). See **[`HAVING`](#having)**.
6. **`SELECT`** – Projection:
   1. **Scalar functions** (per-row): computed *after grouping*. [Functions](#functions)
   2. **Window functions** (per-row over a window): computed *after* the entire SELECT list is built (but before ORDER BY for final output). See **[Window Functions ](#window-functions)**.
7. **`ORDER BY`** – Sort result; may reference aliases, aggregates, window results. See **[`ORDER BY`](#order-by)**.
8. **`LIMIT` / `OFFSET`** – Return subset of sorted rows. See **[`LIMIT` / `OFFSET`](#limit--offset)** and **[`OFFSET`](#offset)**.

---

## Core Clauses

### `SELECT`

Defines which columns/expressions to return. Can include scalar, aggregate, and window functions.

#### Scalar Functions

Operate on single values per row. see more at [Functions](#functions)

#### Window Functions 

Compute values over a related set of rows without collapsing them. (Full list under **[Window Functions](#window-functions-1)**).

Common: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()`, `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()`, `NTH_VALUE()`, `CUME_DIST()`, `PERCENT_RANK()`.

##### `RANGE`/`ROWS`/`PRECEDING`/`CURRENT`
```sql
SELECT AVG(value) OVER (
    RANGE BETWEEN INTERVAL 7 DAY PRECEDING AND CURRENT ROW
);

```

### `FROM`

Declares data sources; supports joins, subqueries, derived tables, CTEs. See **[`FROM`](#from-1)** and join entries under **[Keywords](#keywords)**.

#### `JOIN`

Combine rows across tables by condition. See **[`JOIN` ](#join-1)** and specific join types.

#### Cartesian Product

Occurs when joining without a predicate; see **[`CROSS JOIN` ](#cross-join)**.

### `WHERE`

Row-level filtering before grouping; see **[`WHERE`](#where-1)**.

### `GROUP BY`

#### Aggregate Functions

Perform calculations across multiple rows per group; return one value per group. See **[Aggregate Functions ](#aggregate-functions-1)**.

##### Common Aggregate Functions

* `SUM()` – Sum of numeric expression. See **[`SUM()` ](#sum)**.
* `COUNT()` – Row/non-NULL count. See **[`COUNT()` ](#count)**.
* `AVG()` – Mean of values. See **[`AVG()` ](#avg)**.
* `MIN()` / `MAX()` – Extremes. See **[`MIN()` ](#min)**, **[`MAX()` ](#max)**.
* `STDDEV_POP()` / `STDDEV_SAMP()` – Standard deviation. See **[`STDDEV_POP()` ](#stddev_pop)**, **[`STDDEV_SAMP()` ](#stddev_samp)**.
* `VAR_POP()` / `VAR_SAMP()` – Variance. See **[`VAR_POP()` ](#var_pop)**, **[`VAR_SAMP()` ](#var_samp)**.
* `GROUP_CONCAT()` – Concatenate values per group. See **[`GROUP_CONCAT()` ](#group_concat)**.

> Note: When using `GROUP BY`, all columns in the `SELECT` clause must either be:
  1. Listed in the `GROUP BY` clause, OR
  2. Used within an aggregate function (like `COUNT()`, `SUM()`, `AVG()`, etc.)

Code Examples:

```sql
-- Valid: dept is in GROUP BY, COUNT(*) is an aggregate function
SELECT dept, COUNT(*) as employee_count
FROM employees
GROUP BY dept;

-- Invalid: name is neither in GROUP BY nor an aggregate function
SELECT dept, name, COUNT(*)
FROM employees
GROUP BY dept;

-- Valid: All non-grouped columns use aggregate functions
SELECT dept, AVG(salary), MAX(hire_date)
FROM employees
GROUP BY dept;
``` 

### `HAVING`
**[Aggregate Functions](#aggregate-functions-1)** and **[`HAVING`](#having-1)**.
Filter used on column after aggregation

### `LIMIT`

Return at most N rows; see **[`LIMIT` / `OFFSET`](#limit--offset)**.

#### `OFFSET`

Skip N rows before returning results; see **[`OFFSET`](#limit--offset)**.

---

## SQL data types
blank

---
## Operators

### Arithmetic

`+`, `-`, `*`, `/`, `%` (modulo). See also **[Numeric \& Math](#numeric--math)**.

### Logical

`AND`, `OR`, `NOT`, `XOR`. See **[`AND` / `OR` / `NOT` / `XOR`](#and--or--not--xor)**.

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
### Understanding each datetime object types and their connections
### Date Function Methods 
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

  
---


## Functions

> Each function is titled, explained, given a **one-line syntax example**, tagged by **Type** (Aggregate / Scalar / Window), and grouped by **what data it works on**.

### String & Text

#### `CONCAT()`

join strings

Syntax: `CONCAT(a,b,...)` → concatenated string. Type: **Scalar**. See also **[`GROUP_CONCAT()`](#group_concat)**.

#### `CONCAT_WS()`

join with separator

Syntax: `CONCAT_WS(sep,a,b,...)`. Type: **Scalar**.

#### `SUBSTRING()` / `SUBSTR()`

extract substring

Syntax: `SUBSTRING(str, pos[, len])`. Type: **Scalar**.

#### `LEFT()` / `RIGHT()`

leading/trailing substring

Syntax: `LEFT(str,n)` / `RIGHT(str,n)`. Type: **Scalar**.

#### `MID()`

substring alias

Syntax: `MID(str,pos,len)`. Type: **Scalar**.

#### `LENGTH()` / `CHAR_LENGTH()`

byte vs character length

Syntax: `LENGTH(str)` / `CHAR_LENGTH(str)`. Type: **Scalar**.

#### `LOWER()` / `UPPER()`

case change

Syntax: `LOWER(str)` / `UPPER(str)`. Type: **Scalar**.

#### `TRIM()` / `LTRIM()` / `RTRIM()`

remove spaces (or chars)

Syntax: `TRIM([[BOTH|LEADING|TRAILING] rem FROM] str)`. Type: **Scalar**.

#### `REPLACE()`

replace substrings

Syntax: `REPLACE(str, from, to)`. Type: **Scalar**.

#### `INSERT()`

replace by position

Syntax: `INSERT(str,pos,len,newstr)`. Type: **Scalar**.

#### `INSTR()` / `LOCATE()`

find substring position

Syntax: `INSTR(str,substr)` / `LOCATE(substr,str[,pos])`. Type: **Scalar**.

#### `POSITION()`

ANSI position

Syntax: `POSITION(substr IN str)`. Type: **Scalar**.

#### `REVERSE()`

reverse string

Syntax: `REVERSE(str)`. Type: **Scalar**.

#### `LPAD()` / `RPAD()`

pad string

Syntax: `LPAD(str,len,pad)` / `RPAD(str,len,pad)`. Type: **Scalar**.

#### `REPEAT()`

repeat string

Syntax: `REPEAT(str,count)`. Type: **Scalar**.

#### Regular Expression functions

* **`REGEXP_LIKE()`** — Syntax: `REGEXP_LIKE(str, pattern[, flags])`. Type: **Scalar**.
* **`REGEXP_REPLACE()`** — Syntax: `REGEXP_REPLACE(str, pat, repl[, pos[, occ[, flags]]])`. Type: **Scalar**.
* **`REGEXP_SUBSTR()`** — Syntax: `REGEXP_SUBSTR(str, pat[, pos[, occ[, flags]]])`. Type: **Scalar**.
* **`RLIKE`** keyword also matches regex; see **[`REGEXP` / `RLIKE` ](#regexp--rlike)**.

#### `FORMAT()`

locale formatting for numbers

Syntax: `FORMAT(num, decimals[, locale])`. Type: **Scalar**.

#### Code-point & encoding

* **`ASCII(str)`** – first char code. Example: `ASCII('A')`. Type: **Scalar**.
* **`CHAR(N[, ... USING charset])`** – code(s) to string. Example: `CHAR(65)`. Type: **Scalar**.
* **`HEX(str|num)` / `UNHEX(hex)`** – hex encode/decode. Type: **Scalar**.
* **`BIN(n)` / `OCT(n)` / `CONV(n,from,to)`** – base conversions. Type: **Scalar**.

#### `QUOTE()` / `UNQUOTE()`

add/remove quotes/escapes

Syntax: `QUOTE(str)` / `UNQUOTE(json_str)`. Type: **Scalar**.

#### `ELT()` / `FIELD()` / `FIND_IN_SET()`

Syntax: `ELT(n,str1,...)`, `FIELD(val, str1,...)`, `FIND_IN_SET(str, set_csv)`. Type: **Scalar**.

---

### Numeric & Math

#### `ABS()`

absolute value

Syntax: `ABS(x)`. Type: **Scalar**.

#### Rounding & truncation

* **`CEIL()` / `CEILING()`** – `CEIL(x)`.
* **`FLOOR()`** – `FLOOR(x)`.
* **`ROUND()`** – `ROUND(x[, d])`.
* **`TRUNCATE()`** – `TRUNCATE(x,d)`.
  Type: **Scalar**.

#### Arithmetic & mod

* **`MOD()`** / `%` – `MOD(n,m)`.
* **`POW()` / `POWER()`** – `POWER(x,y)`.
* **`SQRT()`** – `SQRT(x)`.
  Type: **Scalar**.

#### Logs & exp

* **`EXP()`** – `EXP(x)`.
* **`LN()` / `LOG()`** – `LN(x)` or `LOG(b,x)`.
* **`LOG10()` / `LOG2()`** – `LOG10(x)` / `LOG2(x)`.
  Type: **Scalar**.

#### Trig & angles

* **`SIN()` `COS()` `TAN()` `ASIN()` `ACOS()` `ATAN()` `ATAN2()`** – e.g., `SIN(x)`.
* **`RADIANS()` / `DEGREES()`** – `RADIANS(x)`.
  Type: **Scalar**.

#### Random & signs

* **`RAND([seed])`** – `RAND()`.
* **`SIGN(x)`** – `SIGN(x)`.
* **`GREATEST()` / `LEAST()`** – `GREATEST(a,b,...)` / `LEAST(a,b,...)`. Type: **Scalar**.

---

### Date & Time

#### Current date/time

* **`NOW()` / `CURRENT_TIMESTAMP`** – `NOW()`.
* **`CURDATE()` / `CURRENT_DATE`** – `CURDATE()`.
* **`CURTIME()` / `CURRENT_TIME`** – `CURTIME()`.
  Type: **Scalar**.

#### Construction & extraction

* **`DATE()` / `TIME()` / `TIMESTAMP()`** – `DATE(expr)`.
* **`YEAR()` `MONTH()` `DAY()` `HOUR()` `MINUTE()` `SECOND()`** – `YEAR(dt)`.
* **`DAYNAME()` `MONTHNAME()` `WEEK()` `QUARTER()` `LAST_DAY()`** – `WEEK(dt)`.
  Type: **Scalar**.

#### Formatting & parsing

* **`DATE_FORMAT()`** – `DATE_FORMAT(dt, fmt)`.
* **`STR_TO_DATE()`** – `STR_TO_DATE(str, fmt)`.
  Type: **Scalar**.

#### Arithmetic 
see also [Date Arithmetics](#date-arithmetics)
* **`DATEDIFF()`** – `DATEDIFF(d1,d2)`.
* **`TIMESTAMPDIFF()`** – `TIMESTAMPDIFF(unit,dt1,dt2)`.
* **`TIMESTAMPADD()`** – `TIMESTAMPADD(unit,interval,dt)`.
* **`ADDDATE()` / `DATE_ADD()`** – `DATE_ADD(dt, INTERVAL n unit)`.
* **`SUBDATE()` / `DATE_SUB()`** – `DATE_SUB(dt, INTERVAL n unit)`.
  Type: **Scalar**.

#### Unix epoch

* **`UNIX_TIMESTAMP([dt])`** – `UNIX_TIMESTAMP()`.
* **`FROM_UNIXTIME(ts)`** – `FROM_UNIXTIME(ts)`.
  Type: **Scalar**.

---

### JSON

#### Creation & inspection

* **`JSON_OBJECT(k,v,...)`** – `JSON_OBJECT('a',1)`.
* **`JSON_ARRAY(v,...)`** – `JSON_ARRAY(1,2)`.
* **`JSON_TYPE(doc)`** – `JSON_TYPE(doc)`.
* **`JSON_KEYS(doc[, path])`** – `JSON_KEYS(doc)`.
* **`JSON_LENGTH(doc[, path])`** – `JSON_LENGTH(doc)`.
  Type: **Scalar**.

#### Access & search

* **`JSON_EXTRACT(doc, path[, ...])`** (`->` / `->>` operators) – `JSON_EXTRACT(doc,'$.a')`.
* **`JSON_SEARCH(doc, 'one'|'all', search[, esc[, path ...]])`** – `JSON_SEARCH(doc,'one','foo')`.
  Type: **Scalar**.

#### Mutation

* **`JSON_SET(doc, path, val[, ...])`** – `JSON_SET(doc,'$.a',1)`.
* **`JSON_REPLACE(doc, path, val[, ...])`** – `JSON_REPLACE(doc,'$.a',1)`.
* **`JSON_INSERT(doc, path, val[, ...])`** – `JSON_INSERT(doc,'$.a',1)`.
* **`JSON_REMOVE(doc, path[, ...])`** – `JSON_REMOVE(doc,'$.a')`.
* **`JSON_MERGE_PATCH()` / `JSON_MERGE_PRESERVE()`** – `JSON_MERGE_PATCH(j1,j2)`.
  Type: **Scalar**.

#### Validation & utilities

* **`JSON_VALID(doc)`** – `JSON_VALID(doc)`.
* **`JSON_QUOTE(str)`** – `JSON_QUOTE(str)`.
* **`JSON_UNQUOTE(json_str)`** – `JSON_UNQUOTE(json_str)`.
  Type: **Scalar**.

---

### Aggregate Functions
See [Aggregate Functions](#aggregate-functions)

#### `COUNT()`

Count total number of rows; `COUNT(expr)` counts non-`NULL` values; `COUNT(DISTINCT expr)` counts distinct non-`NULL` values.

Syntax: `COUNT(*)` or `COUNT(expr)` or `COUNT(DISTINCT expr)`.

Also see [`COUNT()` ](#count-1).

#### `SUM()`

Sum of non-`NULL` numeric values; `DISTINCT` sums unique values only.

Syntax: `SUM(expr)` or `SUM(DISTINCT expr)`.

Also see [`SUM()` ](#sum-1).

#### `AVG()`

Arithmetic mean of non-`NULL` values; `DISTINCT` averages unique values only.

Syntax: `AVG(expr)` or `AVG(DISTINCT expr)`.

Also see [`AVG()` ](#avg-1).

#### `MIN()`

Smallest (minimum) non-`NULL` value.

Syntax: `MIN(expr)`.

Also see [`MIN()` ](#min-1).

#### `MAX()`

Largest (maximum) non-`NULL` value.

Syntax: `MAX(expr)`.

Also see [`MAX()` ](#max-1).

#### `STD()`

Synonym for population standard deviation.

Syntax: `STD(expr)`.

Also see [`STD()` ](#std-1).

#### `STDDEV()`

Synonym for population standard deviation.

Syntax: `STDDEV(expr)`.

Also see [`STDDEV()` ](#stddev-1).

#### `STDDEV_POP()`

Population standard deviation of non-`NULL` values.

Syntax: `STDDEV_POP(expr)`.

Also see [`STDDEV_POP()` ](#stddev_pop-1).

#### `STDDEV_SAMP()`

Sample standard deviation (Bessel’s correction).

Syntax: `STDDEV_SAMP(expr)`.

Also see [`STDDEV_SAMP()` ](#stddev_samp-1).

#### `VAR_POP()`

Population variance of non-`NULL` values.

Syntax: `VAR_POP(expr)`.

Also see [`VAR_POP()` ](#var_pop-1).

#### `VAR_SAMP()`

Sample variance (with sample adjustment).

Syntax: `VAR_SAMP(expr)`.

Also see [`VAR_SAMP()` ](#var_samp-1).

#### `VARIANCE()`

Synonym for `VAR_POP()` (population variance).

Syntax: `VARIANCE(expr)`.

Also see [`VARIANCE()` ](#variance-1).

#### `BIT_AND()`

Bitwise AND across integer/binary arguments.

Syntax: `BIT_AND(expr)`.

Also see [`BIT_AND()` ](#bit_and-1).

#### `BIT_OR()`

Bitwise OR across integer/binary arguments.

Syntax: `BIT_OR(expr)`.

Also see [`BIT_OR()` ](#bit_or-1).

#### `BIT_XOR()`

Bitwise XOR across integer/binary arguments.

Syntax: `BIT_XOR(expr)`.

Also see [`BIT_XOR()` ](#bit_xor-1).

#### `GROUP_CONCAT()`

Concatenate non-`NULL` values from multiple rows into a single string; supports ordering, distinct, and custom separator.

Syntax: `GROUP_CONCAT([DISTINCT] expr [ORDER BY expr ...] [SEPARATOR str])`.

(No window counterpart.)

#### `JSON_ARRAYAGG()`

Aggregate rows as a single JSON array.

Syntax: `JSON_ARRAYAGG(expr [ORDER BY expr ...] [LIMIT n])`.

(No window counterpart.)

#### `JSON_OBJECTAGG()`

Aggregate rows as a single JSON object mapping key→value pairs.

Syntax: `JSON_OBJECTAGG(key_expr, value_expr [ORDER BY expr ...] [LIMIT n])`.

(No window counterpart.)

---

### Window Functions
[Window Functions](#window-functions)
#### `COUNT()`

Count rows within the window partition; `COUNT(expr)` counts non-`NULL` values. `DISTINCT` is **not** permitted in window form.

Syntax: `COUNT(*) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])` or `COUNT(expr) OVER (...)`.

Also see [`COUNT()` ](#count).

#### `SUM()`

Sum of values within the window partition; frame/ordering controls running totals.

Syntax: `SUM(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`SUM()` ](#sum).

#### `AVG()`

Average of values within the window partition.

Syntax: `AVG(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`AVG()` ](#avg).

#### `MIN()`

Minimum value within the window partition.

Syntax: `MIN(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`MIN()` ](#min).

#### `MAX()`

Maximum value within the window partition.

Syntax: `MAX(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`MAX()` ](#max).

#### `STD()`

Population standard deviation within the window partition (synonym of `STDDEV_POP`).

Syntax: `STD(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`STD()` ](#std) and [`STDDEV_POP()` ](#stddev_pop).

#### `STDDEV()`

Population standard deviation within the window partition (synonym of `STDDEV_POP`).

Syntax: `STDDEV(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`STDDEV()` ](#stddev) and [`STDDEV_POP()` ](#stddev_pop).

#### `STDDEV_POP()`

Population standard deviation within the window partition.

Syntax: `STDDEV_POP(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`STDDEV_POP()` ](#stddev_pop).

#### `STDDEV_SAMP()`

Sample standard deviation within the window partition.

Syntax: `STDDEV_SAMP(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`STDDEV_SAMP()` ](#stddev_samp).

#### `VAR_POP()`

Population variance within the window partition.

Syntax: `VAR_POP(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`VAR_POP()` ](#var_pop).

#### `VAR_SAMP()`

Sample variance within the window partition.

Syntax: `VAR_SAMP(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`VAR_SAMP()` ](#var_samp).

#### `VARIANCE()`

Population variance within the window partition (synonym of `VAR_POP`).

Syntax: `VARIANCE(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`VARIANCE()` ](#variance) and [`VAR_POP()` ](#var_pop).

#### `BIT_AND()`

Bitwise AND within the window partition.

Syntax: `BIT_AND(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`BIT_AND()` ](#bit_and).

#### `BIT_OR()`

Bitwise OR within the window partition.

Syntax: `BIT_OR(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`BIT_OR()` ](#bit_or).

#### `BIT_XOR()`

Bitwise XOR within the window partition.

Syntax: `BIT_XOR(expr) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

Also see [`BIT_XOR()` ](#bit_xor).

#### `ROW_NUMBER()`

Rank each row in order without duplicates (1, 2, 3, …) per partition.

Syntax: `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`.

#### `RANK()`

Assign rank with gaps for ties.

Syntax: `RANK() OVER (PARTITION BY ... ORDER BY ...)`.

#### `DENSE_RANK()`

Assign rank without gaps for ties.

Syntax: `DENSE_RANK() OVER (PARTITION BY ... ORDER BY ...)`.

#### `NTILE(n)`

Distribute rows into `n` buckets as evenly as possible.

Syntax: `NTILE(n) OVER (PARTITION BY ... ORDER BY ...)`.

#### `LAG()`

Return value from a preceding row within the partition.

Syntax: `LAG(expr[, offset[, default]]) OVER (PARTITION BY ... ORDER BY ...)`.

#### `LEAD()`

Return value from a following row within the partition.

Syntax: `LEAD(expr[, offset[, default]]) OVER (PARTITION BY ... ORDER BY ...)`.

#### `FIRST_VALUE()`

Return the first value in the ordered window frame.

Syntax: `FIRST_VALUE(expr) OVER (PARTITION BY ... ORDER BY ... [frame])`.

#### `LAST_VALUE()`

Return the last value in the ordered window frame.

Syntax: `LAST_VALUE(expr) OVER (PARTITION BY ... ORDER BY ... [frame])`.

#### `NTH_VALUE()`

Return the nth value in the ordered window frame.

Syntax: `NTH_VALUE(expr, n) OVER (PARTITION BY ... ORDER BY ... [frame])`.

#### `CUME_DIST()`

Cumulative distribution (proportion of rows ≤ current) within partition.

Syntax: `CUME_DIST() OVER (PARTITION BY ... ORDER BY ...)`.

#### `PERCENT_RANK()`

Percent rank: `(rank - 1) / (rows_in_partition - 1)`.

Syntax: `PERCENT_RANK() OVER (PARTITION BY ... ORDER BY ...)`.


> Note:
> - `COUNT(DISTINCT ...)` is not permitted with `OVER(...)` in MySQL.
> - `GROUP_CONCAT`, `JSON_ARRAYAGG`, and `JSON_OBJECTAGG` are **aggregate-only** (no window form).
> - Synonyms: `STD` and `STDDEV` ≡ `STDDEV_POP`; `VARIANCE` ≡ `VAR_POP`.

---

### Information

#### Metadata & session

* **`VERSION()`** – `VERSION()`.
* **`DATABASE()`** / **`SCHEMA()`** – `DATABASE()`.
* **`USER()`** / **`CURRENT_USER()`** – `CURRENT_USER()`.
* **`CONNECTION_ID()`** – `CONNECTION_ID()`.
* **`LAST_INSERT_ID([expr])`** – `LAST_INSERT_ID()`.
  Type: **Scalar**.

#### Utility

* **`UUID()` / `UUID_TO_BIN()` / `BIN_TO_UUID()`** – `UUID()`.
* **`SLEEP(n)`** – `SLEEP(1)`.
* **`INET_ATON()` / `INET_NTOA()` / `INET6_ATON()` / `INET6_NTOA()`** – `INET_ATON('127.0.0.1')`.
  Type: **Scalar**.

#### Cryptographic & hash

* **`MD5(str)`** – `MD5('x')`.
* **`SHA1(str)` / `SHA2(str, 224|256|384|512)`** – `SHA2('x',256)`.
* **`AES_ENCRYPT(str,key)` / `AES_DECRYPT(crypt,key)`** – `AES_ENCRYPT('x','k')`.
  Type: **Scalar**.

## Keywords

> The keywords are group by **what data they work on**, one keyword may appear under multiple subsections, as they serve different purpose when used in different syntax

### Datetime 

#### `INTERVAL`

#### Datetime Object types

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
Used in date arithemetics
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

#### `EXISTS` / `NOT EXISTS` 

Predicate for subquery existence. Example: `WHERE EXISTS (SELECT 1 ...)`.

#### `IN` / `NOT IN` 

Membership predicate. Example: `WHERE col IN (1,2,3)`.

#### `BETWEEN` / `NOT BETWEEN` 

Range predicate (inclusive). Example: `WHERE x BETWEEN 1 AND 10`.

#### `LIKE` / `NOT LIKE` 

Simple wildcard match. Example: `WHERE name LIKE 'A%'`.

#### `REGEXP` / `RLIKE` 

Regex match operator. Example: `WHERE name REGEXP '^[A-Z]+'`. See **[Regular Expression functions](#regular-expression-functions)**.

#### `IS NULL` / `IS NOT NULL` 

Null tests. Example: `WHERE col IS NOT NULL`.

#### `ANY` / `SOME` / `ALL` 

Quantified comparison with subqueries. Example: `x > ALL (SELECT ...)`.

---

### Logical & arithmetic operators

#### `AND` / `OR` / `NOT` / `XOR` 

Boolean connectors. Example: `WHERE a AND (b OR NOT c)`.

#### `DIV` / `MOD` 

Integer division and modulo. Example: `a DIV 2`, `a MOD 2`.

#### `||` / `OR` (pipes) 

Synonym in SQL mode `PIPES_AS_CONCAT` for concatenation. Example: `a || b`.

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

Introduce a window specification for a window-capable function. Syntax: `fn(...) OVER ([PARTITION BY ...] [ORDER BY ...] [frame])`.

#### `PARTITION BY` 

Divide rows into partitions for window calculations. Syntax: `OVER (PARTITION BY key [ORDER BY ...])`.

#### `ROWS` / `RANGE` / `GROUPS` 

Define the window frame relative to current row/order. Syntax: `OVER (... ROWS|RANGE|GROUPS BETWEEN <start> AND <end>)`.

#### `NULLS FIRST` / `NULLS LAST` (window `ORDER BY`) 

Control null ordering within window `ORDER BY`. Syntax: `OVER (... ORDER BY expr NULLS LAST)`.

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
Note: this documentation applys to MySQL 8.x
