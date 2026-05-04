from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = BASE_DIR / "data" / "raw_sales_data.csv"
CLEAN_DATA_PATH = BASE_DIR / "data" / "cleaned_sales_data.csv"
VISUALS_DIR = BASE_DIR / "visuals"
REPORTS_DIR = BASE_DIR / "reports"
DATA_QUALITY_SUMMARY_PATH = REPORTS_DIR / "data_quality_summary.md"
SUMMARY_REPORT_PATH = REPORTS_DIR / "summary_report.md"


def write_data_quality_summary(metrics: dict[str, int]) -> None:
    content = f"""# Data Quality Summary

## Raw vs Cleaned Record Counts
- Raw row count: **{metrics['raw_row_count']}**
- Cleaned row count: **{metrics['cleaned_row_count']}**
- Duplicate rows removed: **{metrics['duplicate_rows_removed']}**

## Cleaning Actions Completed
- Missing discount values filled: **{metrics['missing_discount_filled']}** (filled with `0`)
- Date formatting standardized: **Yes** (`YYYY-MM-DD`)
- Text/category fields standardized: **Yes** (trimmed whitespace + title case)
- Numeric fields converted: **Yes** (`quantity`, `unit_price`, `discount`)
- Revenue field created: **Yes** (`revenue = quantity * unit_price * (1 - discount)`)

## Why These Steps Matter for Business Reporting
These steps make reporting more reliable and easier to trust. Removing duplicates avoids overstating sales, standardized dates allow accurate trend analysis, and clean text categories prevent split groupings (for example, `credit card` vs `Credit Card`). Converting numeric columns ensures calculations are correct, and adding `revenue` gives a direct KPI that supports dashboards and decision-making.
"""
    DATA_QUALITY_SUMMARY_PATH.write_text(content, encoding="utf-8")


def write_summary_report(df: pd.DataFrame) -> None:
    total_revenue = round(df["revenue"].sum(), 2)
    order_count = len(df)
    avg_order_revenue = round(total_revenue / order_count, 2)

    top_category = (
        df.groupby("product_category", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
        .iloc[0]
    )

    top_region = (
        df.groupby("region", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
        .iloc[0]
    )

    monthly = (
        df.groupby("order_month", as_index=False)["revenue"]
        .sum()
        .sort_values("order_month")
    )

    content = f"""# Client-Facing Summary Report

## Executive Summary
This project turns a messy synthetic spreadsheet export into clean, analysis-ready sales data and a basic dashboard package that a small business owner can review quickly.

## Business Question
How can we standardize raw sales data so monthly revenue trends, category performance, and regional performance can be reported accurately?

## Dataset Description and Caveats
- Source file: `data/raw_sales_data.csv`
- Time period covered: **{df['order_date'].min().date()} to {df['order_date'].max().date()}**
- Final cleaned records used: **{order_count}**
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
- Total revenue: **${total_revenue:,.2f}**
- Number of cleaned orders: **{order_count}**
- Average revenue per order: **${avg_order_revenue:,.2f}**
- Top category by revenue: **{top_category['product_category']}** (${top_category['revenue']:,.2f})
- Top region by revenue: **{top_region['region']}** (${top_region['revenue']:,.2f})

## Key Findings
- Monthly revenue fluctuated across the sample period, from **${monthly.iloc[0]['revenue']:,.2f}** in {monthly.iloc[0]['order_month']} to **${monthly.iloc[-1]['revenue']:,.2f}** in {monthly.iloc[-1]['order_month']}.
- **{top_category['product_category']}** contributed the highest category revenue in this sample.
- Revenue is concentrated in a few categories, indicating where promotions or inventory planning can start.

## Business Recommendations
- Keep a standardized input template for spreadsheet uploads to reduce cleanup time.
- Prioritize top-performing categories for stock planning and featured promotions.
- Review lower-revenue categories to confirm whether pricing, assortment, or marketing changes are needed.

## Limitations and Next Steps
- Because this is synthetic sample data, results should not be treated as real market performance.
- Next steps: add a larger sample dataset, include return/cancellation fields, and track customer segments for deeper analysis.
"""
    SUMMARY_REPORT_PATH.write_text(content, encoding="utf-8")


def main() -> None:
    df = pd.read_csv(RAW_DATA_PATH)
    raw_row_count = len(df)

    # Clean column names
    df.columns = (
        df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    )

    # Trim whitespace from string columns
    object_cols = df.select_dtypes(include=["object", "string"]).columns
    df[object_cols] = df[object_cols].apply(lambda col: col.astype(str).str.strip())

    # Standardize text capitalization
    df["customer_name"] = df["customer_name"].str.title()
    df["product_category"] = df["product_category"].str.title()
    df["product_name"] = df["product_name"].str.title()
    df["payment_method"] = df["payment_method"].str.title()
    df["region"] = df["region"].str.title()

    # Numeric cleanup
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    discount_series = pd.to_numeric(df["discount"], errors="coerce")
    missing_discount_filled = int(discount_series.isna().sum())
    df["discount"] = discount_series.fillna(0)

    # Date standardization
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce", format="mixed")

    # Remove duplicates and invalid rows
    before_dedup_row_count = len(df)
    dedupe_cols = [col for col in df.columns if col != "order_id"]
    df = df.drop_duplicates(subset=dedupe_cols)
    duplicate_rows_removed = before_dedup_row_count - len(df)
    df = df.dropna(subset=["order_date", "quantity", "unit_price"])

    # Revenue calculation
    df["revenue"] = (df["quantity"] * df["unit_price"] * (1 - df["discount"]))
    df["revenue"] = df["revenue"].round(2)

    # Add time helper columns for plotting
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)
    df["order_year"] = df["order_date"].dt.year

    # Save cleaned dataset
    df = df.sort_values("order_date")
    df.to_csv(CLEAN_DATA_PATH, index=False, date_format="%Y-%m-%d")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    metrics = {
        "raw_row_count": raw_row_count,
        "cleaned_row_count": len(df),
        "duplicate_rows_removed": duplicate_rows_removed,
        "missing_discount_filled": missing_discount_filled,
    }
    write_data_quality_summary(metrics)
    write_summary_report(df)

    VISUALS_DIR.mkdir(parents=True, exist_ok=True)

    # Monthly revenue chart
    monthly_revenue = df.groupby("order_month", as_index=False)["revenue"].sum()
    plt.figure(figsize=(8, 4.5))
    plt.plot(monthly_revenue["order_month"], monthly_revenue["revenue"], marker="o")
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(VISUALS_DIR / "monthly_revenue.png", dpi=150)
    plt.close()

    # Revenue by category chart
    category_revenue = df.groupby("product_category", as_index=False)["revenue"].sum()
    category_revenue = category_revenue.sort_values("revenue", ascending=False)
    plt.figure(figsize=(8, 4.5))
    plt.bar(category_revenue["product_category"], category_revenue["revenue"])
    plt.title("Revenue by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Revenue (USD)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(VISUALS_DIR / "revenue_by_category.png", dpi=150)
    plt.close()

    # Yearly revenue chart
    yearly_revenue = df.groupby("order_year", as_index=False)["revenue"].sum()
    plt.figure(figsize=(6, 4.5))
    plt.bar(yearly_revenue["order_year"].astype(str), yearly_revenue["revenue"])
    plt.title("Yearly Revenue")
    plt.xlabel("Year")
    plt.ylabel("Revenue (USD)")
    plt.tight_layout()
    plt.savefig(VISUALS_DIR / "yearly_revenue.png", dpi=150)
    plt.close()

    print("Data cleaning complete. Cleaned file, reports, and visuals created successfully.")


if __name__ == "__main__":
    main()
