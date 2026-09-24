# Data Analysis Practice Projects

Beginner projects where I practice querying and summarizing data with Python.
The same dataset is analyzed three ways to compare the tools.

**Dataset:** `supermarket_sales.csv`, a public supermarket sales dataset
(1,000 rows, 17 columns). This is practice data, not client data.

## Scripts

| File | Tool | What it does |
|---|---|---|
| `sales_analysis.py` | pandas | Summaries and groupby analysis |
| `sales_sql_analysis.py` | SQLite + pandas | Loads the CSV into a database, then answers the same questions with SQL |
| `duckdb_analysis.py` | DuckDB + pandas | Runs SQL directly on the CSV file |

Each script prints: dataset shape, total sales by product line,
average rating by branch, revenue by payment method, and missing values per column.

## How to run

1. Put `supermarket_sales.csv` in the same folder as the scripts.
2. `pip install pandas duckdb`
3. `python sales_analysis.py` (or either of the other two)

## Limits

These are exercises. They produce descriptive summaries only, with no charts
and no business conclusions. Next, I plan to build a project that answers a
real business question using e-commerce data.
