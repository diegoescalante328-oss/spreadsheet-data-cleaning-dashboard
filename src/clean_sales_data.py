from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = BASE_DIR / "data" / "raw_sales_data.csv"
CLEAN_DATA_PATH = BASE_DIR / "data" / "cleaned_sales_data.csv"
VISUALS_DIR = BASE_DIR / "visuals"


def main() -> None:
    df = pd.read_csv(RAW_DATA_PATH)

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
    df["discount"] = pd.to_numeric(df["discount"], errors="coerce").fillna(0)

    # Date standardization
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce", format="mixed")

    # Remove duplicates and invalid rows
    dedupe_cols = [col for col in df.columns if col != "order_id"]
    df = df.drop_duplicates(subset=dedupe_cols)
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

    print("Data cleaning complete. Cleaned file and visuals created successfully.")


if __name__ == "__main__":
    main()
