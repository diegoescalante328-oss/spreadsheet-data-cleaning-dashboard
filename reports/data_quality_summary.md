# Data Quality Summary

## Raw vs Cleaned Record Counts
- Raw row count: **15**
- Cleaned row count: **14**
- Duplicate rows removed: **1**

## Cleaning Actions Completed
- Missing discount values filled: **4** (filled with `0`)
- Date formatting standardized: **Yes** (`YYYY-MM-DD`)
- Text/category fields standardized: **Yes** (trimmed whitespace + title case)
- Numeric fields converted: **Yes** (`quantity`, `unit_price`, `discount`)
- Revenue field created: **Yes** (`revenue = quantity * unit_price * (1 - discount)`)

## Why These Steps Matter for Business Reporting
These steps make reporting more reliable and easier to trust. Removing duplicates avoids overstating sales, standardized dates allow accurate trend analysis, and clean text categories prevent split groupings (for example, `credit card` vs `Credit Card`). Converting numeric columns ensures calculations are correct, and adding `revenue` gives a direct KPI that supports dashboards and decision-making.
