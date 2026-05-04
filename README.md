# Spreadsheet Data Cleaning Dashboard (Portfolio Project)

## Project Overview
This is a beginner-friendly portfolio project that simulates a common freelance analytics task: clean messy spreadsheet sales data and create a simple report with visuals.

The dataset is fully **synthetic** (not real company data) and intentionally includes typical data-quality issues.

## Business Problem
A small business exported sales records from spreadsheets, but the data is inconsistent and hard to report on. They need:
- clean, analysis-ready data
- quick revenue summaries
- simple visuals for monthly and category performance

## Tools Used
- Python
- pandas
- matplotlib

## Project Structure

```text
spreadsheet-data-cleaning-dashboard/
├── data/
│   ├── raw_sales_data.csv
│   └── cleaned_sales_data.csv
├── reports/
│   └── summary_report.md
├── src/
│   └── clean_sales_data.py
├── visuals/
│   ├── monthly_revenue.png
│   ├── revenue_by_category.png
│   └── yearly_revenue.png
├── .gitignore
├── README.md
└── requirements.txt
```

## Data Cleaning Process
The script in `src/clean_sales_data.py` performs:
1. Column name standardization
2. Whitespace trimming
3. Text capitalization standardization
4. Duplicate removal
5. Missing discount handling (fills with `0`)
6. Date parsing and standard formatting
7. Numeric conversion for quantity, unit price, and discount
8. Revenue calculation:
   `revenue = quantity * unit_price * (1 - discount)`

## Dashboard / Visual Outputs
After running the script, these charts are created:
- `monthly_revenue.png`: monthly revenue trend
- `revenue_by_category.png`: revenue by product category
- `yearly_revenue.png`: yearly revenue summary

> Note: Visual PNG files are generated locally when you run `python src/clean_sales_data.py`.

## Key Insights (Sample Data)
- Home & Kitchen is the top revenue category in this sample.
- Revenue rises from January to March in the sample period.
- Electronics and Fashion are also meaningful revenue contributors.

## How to Run
1. (Optional) Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python src/clean_sales_data.py
   ```
4. Check outputs:
   - Cleaned data: `data/cleaned_sales_data.csv`
   - Visuals (generated locally): `visuals/monthly_revenue.png`, `visuals/revenue_by_category.png`, `visuals/yearly_revenue.png`

## What This Demonstrates for Freelance Clients
- Ability to clean messy spreadsheet exports
- Ability to build a reproducible Python workflow
- Ability to turn raw data into simple decision-support visuals
- Clear documentation for project handoff
