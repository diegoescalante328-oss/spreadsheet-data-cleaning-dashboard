# Client-Facing Summary Report

## Executive Summary
This project turns a messy synthetic spreadsheet export into clean, analysis-ready sales data and a basic dashboard package that a small business owner can review quickly.

## Business Question
How can we standardize raw sales data so monthly revenue trends, category performance, and regional performance can be reported accurately?

## Dataset Description and Caveats
- Source file: `data/raw_sales_data.csv`
- Time period covered: **2026-01-03 to 2026-03-04**
- Final cleaned records used: **14**
- Caveat: The dataset is synthetic and small, so insights are for demonstration only and not for real-world forecasting.

## Data Cleaning Performed
- Standardized column names
- Trimmed extra whitespace
- Standardized text fields (`customer_name`, `product_category`, `product_name`, `payment_method`, `region`)
- Converted date field to a consistent format
- Converted numeric fields for accurate math
- Removed duplicate rows
- Filled missing discounts with `0`
- Created calculated `revenue` field

## KPI Snapshot
- Total revenue: **$887.70**
- Number of cleaned orders: **14**
- Average revenue per order: **$63.41**
- Top category by revenue: **Electronics** ($293.74)
- Top region by revenue: **North** ($254.27)

## Key Findings
- Monthly revenue fluctuated across the sample period, from **$332.08** in 2026-01 to **$309.68** in 2026-03.
- **Electronics** contributed the highest category revenue in this sample.
- Revenue is concentrated in a few categories, indicating where promotions or inventory planning can start.

## Business Recommendations
- Keep a standardized input template for spreadsheet uploads to reduce cleanup time.
- Prioritize top-performing categories for stock planning and featured promotions.
- Review lower-revenue categories to confirm whether pricing, assortment, or marketing changes are needed.

## Limitations and Next Steps
- Because this is synthetic sample data, results should not be treated as real market performance.
- Next steps: add a larger sample dataset, include return/cancellation fields, and track customer segments for deeper analysis.
