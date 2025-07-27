![Tool](https://img.shields.io/badge/Power%20BI-SQL%20%2B%20Forecasting-yellowgreen)
![Status](https://img.shields.io/badge/KPI%20Tracking-Complete-brightgreen)
![Forecast](https://img.shields.io/badge/Trends-Monthly-orange)

# Sales KPI Dashboard

This project showcases a data-driven sales performance dashboard designed to track and report key performance indicators (KPIs) across regions and time periods.

## Overview

The dashboard visualizes essential sales metrics, such as revenue trends, product performance, and regional comparisons. This type of dashboard supports data-driven decision making in sales and marketing departments by providing insights into business performance.

## Features

- Regional sales breakdown with filters
- Monthly sales volume and revenue trend charts
- Top-performing products and categories
- Forecasting using historical sales data
- Data-driven visuals with slicers and dynamic charts

## Tools Used

- **Power BI Desktop** for interactive visualizations
- **SQL Server Express** (or SQLite) for structured data source
- **Excel/CSV** used for sample data loading
- **DAX** and **Power Query (M)** for transformations

## Dataset

This project uses fictional sales data generated for demonstration purposes. The dataset includes:
- Sales transactions
- Product catalog
- Regional and store-level hierarchy
- Time dimension (calendar table)

## Project Structure

```
sales-kpi-dashboard/
├── data/                # Sample CSV or SQL backup files
├── dashboard/           # Power BI .pbix file
├── scripts/             # SQL queries for extraction/cleaning
└── README.md            # Project overview and instructions
```

## How to Run

1. Load the sample data into your SQL Server Express or SQLite instance.
2. Open the Power BI file from the `dashboard/` folder.
3. Configure your data source credentials if needed.
4. Interact with slicers and filters to explore KPIs.

## Skills Demonstrated

- Data modeling and relational joins in Power BI
- Writing DAX expressions and measures
- Using Power Query to shape raw data
- Designing executive-friendly dashboards

## Screenshots

_Include screenshots of the Power BI report here once complete._

## License

This project is licensed under the MIT License.
