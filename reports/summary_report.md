# Sales Data Cleaning & Dashboard Summary Report

## Project Objective
This project demonstrates a clear, practical workflow for cleaning a small sales dataset and creating a simple visual summary for business reporting.

## Issues Found in Raw Data
The synthetic raw data intentionally includes common spreadsheet issues:
- inconsistent capitalization
- extra spaces in text and numeric fields
- duplicate transactions
- missing discount values
- mixed date formats (for example `2026/01/03`, `01-04-2026`, `07 Jan 2026`)
- numeric fields stored inconsistently

## Cleaning Steps Performed
1. Standardized column names to lowercase with underscores.
2. Trimmed extra whitespace.
3. Standardized capitalization using title case.
4. Converted `quantity`, `unit_price`, and `discount` to numeric types.
5. Filled missing discount values with `0`.
6. Parsed and standardized `order_date`.
7. Removed duplicate records.
8. Removed rows with invalid required date/numeric values.
9. Calculated `revenue` using:
   `revenue = quantity * unit_price * (1 - discount)`

## Key Business Insights (Sample Data)
- Home & Kitchen generated the highest category-level revenue in this sample.
- Revenue increases from January to March in the sample period.
- 2026 revenue is supported mainly by Home & Kitchen and Electronics.

## Dashboard / Visual Summary
Expected generated visuals:
- `visuals/monthly_revenue.png` (monthly trend)
- `visuals/revenue_by_category.png` (category comparison)
- `visuals/yearly_revenue.png` (yearly total)

Note: these PNG files are generated locally by running `python src/clean_sales_data.py`.

## What This Demonstrates to a Client
This project shows capability to:
- clean messy spreadsheet exports,
- apply reliable data-quality steps,
- create clear business visuals,
- and deliver organized, reproducible project files.
