# Spreadsheet Data Cleaning Dashboard (Portfolio Case Study)

A small, client-ready analytics case study that cleans messy spreadsheet-style sales data and turns it into business-ready outputs you can share quickly.

## What this solves
Small teams often export sales data from spreadsheets with inconsistent formats, duplicates, and missing values. This project shows a repeatable Python workflow to clean that data and produce reliable reporting artifacts.

## What you get
- Cleaned CSV data for downstream reporting
- Data quality summary
- Data dictionary
- Business summary report
- Local sales visuals

## Synthetic Data & Privacy Note
This repository uses a **synthetic dataset** created for portfolio use. No real customer, financial, or company data is included.

## Tools Used
- Python
- pandas
- matplotlib
- Markdown documentation for project handoff

## Workflow
1. Load raw CSV export.
2. Standardize column names and text fields.
3. Convert dates and numeric columns.
4. Remove duplicates and handle missing discounts.
5. Create a calculated revenue field.
6. Export cleaned dataset, quality summary, client-facing report, and visuals.

## Cleaning Issues Addressed
- Mixed date formats
- Inconsistent capitalization and extra spaces
- Duplicate rows
- Missing discount values
- Numeric fields stored as text/inconsistent format

## Client Deliverables
- `data/cleaned_sales_data.csv` (cleaned CSV output)
- `reports/data_quality_summary.md` (data quality summary)
- `docs/data_dictionary.md` (data dictionary)
- `reports/summary_report.md` (business summary report)
- Local chart files in `visuals/` (sales visuals)
- Reproducible Python cleaning workflow in `src/clean_sales_data.py`

## How to Run
```bash
pip install -r requirements.txt
python src/clean_sales_data.py
```

## Visual Outputs (Generated Locally)
Run `python src/clean_sales_data.py` to generate local visuals (do not commit PNG files or other binaries).

Expected visual files:
- `visuals/monthly_revenue.png` — shows month-by-month revenue trend after cleaning.
- `visuals/revenue_by_category.png` — compares total revenue across product categories.
- `visuals/yearly_revenue.png` — summarizes annual revenue totals for quick year-over-year review.

## Expected Outputs
After running `python src/clean_sales_data.py`, the project generates:
- `data/cleaned_sales_data.csv`
- `reports/data_quality_summary.md`
- `reports/summary_report.md`
- `visuals/monthly_revenue.png`
- `visuals/revenue_by_category.png`
- `visuals/yearly_revenue.png`

## Key Insights (Synthetic Sample)
- Revenue trends can be compared month-to-month after date standardization.
- Category performance becomes reliable once naming is standardized.
- A calculated revenue field enables immediate KPI reporting without manual spreadsheet formulas.

## Repository Structure
```text
spreadsheet-data-cleaning-dashboard/
├── data/
│   ├── raw_sales_data.csv
│   └── cleaned_sales_data.csv
├── docs/
│   ├── data_dictionary.md
│   └── github_metadata_recommendations.md
├── reports/
│   ├── data_quality_summary.md
│   └── summary_report.md
├── src/
│   └── clean_sales_data.py
├── visuals/
│   └── .gitkeep
├── LICENSE
├── README.md
└── requirements.txt
```

## Limitations
- Small synthetic dataset (not suitable for real forecasting).
- No customer segmentation, returns data, or product-level margin analysis.
- Visuals are static PNG charts, not interactive dashboards.

## Future Improvements
- Add a larger synthetic dataset with more months and regions.
- Include returns/cancellations and net sales metrics.
- Add simple validation checks before writing cleaned outputs.

## License
This project is released under the MIT License. See `LICENSE` for details.
