# Spreadsheet Data Cleaning Dashboard (Portfolio Case Study)

A beginner-friendly analytics case study that shows how messy spreadsheet sales data can be cleaned into client-ready reporting outputs.

## Business Problem
A small business exports sales data from spreadsheets, but inconsistent formatting, duplicates, and missing values make reporting unreliable. This project demonstrates a repeatable cleanup workflow that improves trust in monthly and category-level KPIs.

## Synthetic Data & Privacy Note
This repository uses a **synthetic dataset** created for practice and portfolio use. No real customer, financial, or company data is included.

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

## How to Run
```bash
pip install -r requirements.txt
python src/clean_sales_data.py
```

## Repository Structure
```text
spreadsheet-data-cleaning-dashboard/
├── data/
│   ├── raw_sales_data.csv
│   └── cleaned_sales_data.csv
├── docs/
│   └── data_dictionary.md
├── reports/
│   ├── data_quality_summary.md
│   └── summary_report.md
├── src/
│   └── clean_sales_data.py
├── visuals/
│   └── .gitkeep
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

## License Note
This project is intended for portfolio and educational use. Add a license file (for example MIT) if you plan to distribute or reuse it publicly.
