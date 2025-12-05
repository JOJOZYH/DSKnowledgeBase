## Functions

### Cast
* **`CAST(expr AS type)`** – `CAST('123' AS UNSIGNED)`. Type: **Scalar**.
* **`CONVERT(expr, type)`** – `CONVERT('123', UNSIGNED)`. Type: **Scalar**.
* **`CONVERT(expr USING charset)`** – `CONVERT(str USING utf8)`. Type: **Scalar**.

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

Syntax: `ABS(x)`.

#### Rounding & truncation

* **`CEIL()` / `CEILING()`** – `CEIL(x)`.
* **`FLOOR()`** – `FLOOR(x)`.
* **`ROUND()`** – `ROUND(x[, d])`.
* **`TRUNCATE()`** – `TRUNCATE(x,d)`.

#### Arithmetic & mod

* **`MOD()`** / `%` – `MOD(n,m)`.
* **`POW()` / `POWER()`** – `POWER(x,y)`.
* **`SQRT()`** – `SQRT(x)`.

#### Logs & exp

* **`EXP()`** – `EXP(x)`.
* **`LN()` / `LOG()`** – `LN(x)` or `LOG(b,x)`.
* **`LOG10()` / `LOG2()`** – `LOG10(x)` / `LOG2(x)`.

#### Trig & angles

* **`SIN()` `COS()` `TAN()` `ASIN()` `ACOS()` `ATAN()` `ATAN2()`** – e.g., `SIN(x)`.
* **`RADIANS()` / `DEGREES()`** – `RADIANS(x)`.

#### Random & signs

* **`RAND([seed])`** – `RAND()`.
* **`SIGN(x)`** – `SIGN(x)`.
* **`GREATEST()` / `LEAST()`** – `GREATEST(a,b,...)` / `LEAST(a,b,...)`.

---

### Date & Time

#### Current date/time

 - **`NOW()`, `CURRENT_TIMESTAMP()`** 
 - **`CURDATE()` / `CURRENT_DATE()`**
 - **`CURTIME()` / `CURRENT_TIME()`**

#### Construction & extraction

 - **`DATE(expr)`**: Takes a date or datetime string or value as input, returns the date part as a **DATE** value (format: 'YYYY-MM-DD').

 - **`TIME(expr)`**: Takes a time or datetime string or value as input, returns the time part as a **TIME** value (format: 'HH:MM:SS[.fraction]').

 - **`TIMESTAMP(expr [, time_expr])`**: Takes one or two arguments (date and/or time), returns a **DATETIME** value (format: 'YYYY-MM-DD HH:MM:SS[.fraction]').

 - **`YEAR(dt)`, `MONTH(dt)`, `DAY(dt)`, `HOUR(dt)`, `MINUTE(dt)`, `SECOND(dt)`**: Take a date, time, or datetime value as input. Return an **integer**. 
   - `YEAR()` returns a 4-digit year, 
   - `MONTH()` returns a 2-digit month (1-12),
   - `DAY()` returns a 2-digit day (1-31),
   - `HOUR()`/`MINUTE()`/`SECOND()` return the respective time part as **integer**.

 - **`DAYNAME(dt)`, `MONTHNAME(dt)`**: Take a date or datetime value as input. Return a **string**.

 - **`WEEK(dt)`, `QUARTER(dt)`**: Take a date or datetime value as input. Return a **integer** as the week/quarter number of the year.

 - **`LAST_DAY(dt)`**: Take a date or datetime value as input, returns the last day of the month as a **DATE** type.

#### Formatting & parsing

 - **`DATE_FORMAT(dt, fmt)`**: Takes a date or datetime value and a format string as input, returns a formatted string representation of the date/time.
 - **`STR_TO_DATE(str, fmt)`**: Takes a string and a format string as input, returns a DATE or DATETIME value parsed from the string.
 - **`EXTRACT(unit FROM date_expr)`**: Takes a [unit](#time-interval-units) (e.g., YEAR, MONTH) and a date/datetime value as input, returns the specified part as an **integer**. 

#### Arithmetic

see also [Date Arithmetics](#date-arithmetics)
 - **`DATEDIFF()`** – `DATEDIFF(d1,d2)`.
 - **`TIMESTAMPDIFF()`** – `TIMESTAMPDIFF(unit,dt1,dt2)`.
 - **`TIMESTAMPADD()`** – `TIMESTAMPADD(unit,interval,dt)`.
 - **`ADDDATE()` / `DATE_ADD()`** – `DATE_ADD(dt, INTERVAL n unit)`.
 - **`SUBDATE()` / `DATE_SUB()`** – `DATE_SUB(dt, INTERVAL n unit)`.

#### Unix epoch

* **`UNIX_TIMESTAMP([dt])`** – `UNIX_TIMESTAMP()`.
* **`FROM_UNIXTIME(ts)`** – `FROM_UNIXTIME(ts)`.

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

---
Note: this documentation applies to MySQL 8.x
