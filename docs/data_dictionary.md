# Data Dictionary

This dictionary describes the cleaned analytics dataset used in this project (`data/cleaned_sales_data.csv`).

| Column Name | Plain-English Description | Data Type | Field Type | Cleaning Notes |
|---|---|---|---|---|
| `order_id` | Unique identifier for each order record. | Integer | Raw | Kept as-is from source; duplicates handled by comparing all other business fields. |
| `order_date` | Date when the order was placed. | Date (`YYYY-MM-DD`) | Cleaned | Mixed raw formats were parsed and standardized into one format for timeline reporting. |
| `customer_name` | Name of the customer who placed the order. | Text | Cleaned | Extra spaces removed and capitalization standardized to title case. |
| `product_category` | Product group (for example Electronics, Fashion). | Text | Cleaned | Whitespace trimmed and category naming standardized to title case. |
| `product_name` | Specific purchased product name. | Text | Cleaned | Whitespace trimmed and capitalization standardized to title case. |
| `quantity` | Number of units purchased in the order line. | Integer | Cleaned | Converted to numeric so totals and revenue can be calculated accurately. |
| `unit_price` | Price per unit before discount. | Float (USD) | Cleaned | Converted to numeric; invalid values would be coerced and removed if required. |
| `discount` | Discount rate applied to the order line (0 to 1). | Float | Cleaned | Converted to numeric; missing values filled with `0`. |
| `payment_method` | Payment type used by the customer. | Text | Cleaned | Standardized to title case to avoid split categories (`paypal` vs `Paypal`). |
| `region` | Sales region associated with the order. | Text | Cleaned | Whitespace and capitalization standardized. |
| `revenue` | Net revenue for the order line after discount. | Float (USD) | Calculated | Created with formula: `quantity * unit_price * (1 - discount)`. |
| `order_month` | Month bucket used for trend charts. | Text (`YYYY-MM`) | Calculated | Derived from cleaned `order_date` for monthly aggregation. |
| `order_year` | Year of the order for yearly summaries. | Integer | Calculated | Derived from cleaned `order_date`. |
