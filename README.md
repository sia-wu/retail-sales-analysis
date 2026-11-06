# Retail Sales Analysis

**Key finding:** Among full months, sales peaked in November 2011 at £1,509,496.33, up 30.7% from October.

## Business Question
How did monthly sales change for a UK-based online retailer?

## Data
[UCI Online Retail](https://doi.org/10.24432/C5BW33) provides transaction records from December 2010 to December 9, 2011.

## Approach
- Use Python and pandas to filter out cancelled invoices and keep records with positive quantities and prices.
- Calculate sales in GBP by multiplying quantity by unit price.
- Summarize sales by month and export the results to `monthly_sales.csv`.

## Limitation
December 2011 includes only the first nine days of the month.

## How to Run
1. Download the UCI Online Retail dataset linked above and extract `Online Retail.xlsx`.
2. Place the Excel file in the same folder as `sales_analysis.py`.
3. From that folder, run `python3 -m pip install pandas openpyxl`, then `python3 sales_analysis.py`.

The script generates `monthly_sales.csv`.
