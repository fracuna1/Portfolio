![Tools](https://img.shields.io/badge/Excel%20%7C%20SQL-Dashboards-blueviolet)
![Status](https://img.shields.io/badge/Variance%20Analysis-Complete-brightgreen)
![Automation](https://img.shields.io/badge/Formulas%20%2B%20Macros-Enabled-success)

# Budget Reporting

This project simulates a monthly budget variance reporting system using SQL for data extraction and Excel for visualization. The goal is to replicate how many organizations handle cost monitoring and budget tracking through easily understandable dashboards.

## Features

- SQL-based data source for monthly expense and budget data
- Excel dashboard with:
  - Conditional formatting for budget vs actuals
  - Variance analysis per department
  - Monthly breakdown and yearly summary
- Custom Excel formulas for dynamic variance computation
- Exportable reports for stakeholder review

## Tools & Technologies

- Microsoft Excel
- SQL (SQLite or mock data)
- Python (for optional automation)

## Folder Structure

```
budget-reporting/
├── data/
│   └── budget_data.sql         # Mock budget and actual expense data
├── dashboard/
│   └── budget_dashboard.xlsx   # Excel dashboard with visualizations
├── scripts/
│   └── extract_data.sql        # Sample SQL queries
├── README.md
```

## Setup Instructions

1. Clone this repo.
2. Open `budget_dashboard.xlsx` located in the `dashboard/` folder.
3. Review SQL scripts in the `scripts/` folder to understand how data was extracted.
4. Optionally connect to SQLite or any RDBMS to run the queries from `budget_data.sql`.

## Use Case

This type of dashboard is often used by finance teams, analysts, or department managers to:
- Monitor overspending
- Track cost-saving efforts
- Justify budget changes
- Communicate financial health to leadership

## Author

Felicia Acuna  
Software Engineer | Data Enthusiast  
[LinkedIn](https://www.linkedin.com/in/felicia-acuna) | [GitHub](https://github.com/fracuna1)
