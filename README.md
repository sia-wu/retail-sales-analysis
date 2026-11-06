# Retail Sales Analysis

**Status:** In progress

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
