![Tool](https://img.shields.io/badge/Airflow-ETL-blue)
![Status](https://img.shields.io/badge/Scheduled%20Jobs-Working-brightgreen)
![Retry](https://img.shields.io/badge/Failure%20Handling-Retry%20Enabled-yellow)

# Data Refresh Scheduler

This project demonstrates an automated data refresh system that simulates updating datasets from external sources on a scheduled basis. It mimics how data engineers automate refresh tasks using scheduling tools such as cron or Airflow.

## Project Overview

Many businesses rely on periodic data updates—whether it's daily sales, user activity, or stock levels. This project simulates pulling new CSV data from a source, updating the database, and refreshing output reports.

### Key Features

- Pulls raw data files from a simulated external folder
- Cleans and merges them into an existing SQLite database
- Appends logs of each refresh cycle for audit purposes
- Generates updated summary tables and reports

## Tools Used

- Python (Pandas, os, sqlite3)
- SQLite database
- Scheduled execution using cron/Task Scheduler (or simulated runs)
- CSV as mock external data source

## Folder Structure

```
data-refresh-scheduler/
│
├── data/
│   ├── raw/                # New incoming data (simulated)
│   └── archive/            # Moved after ingestion
│
├── db/
│   └── sales_data.db       # SQLite database
│
├── scripts/
│   ├── refresh_data.py     # Main ETL script
│   └── log_updater.py      # Maintains update logs
│
└── reports/
    └── summary_report.csv  # Output from latest refresh
```

## How to Run

1. Place new `.csv` files in `data/raw/`
2. Run the `refresh_data.py` script:
```bash
python scripts/refresh_data.py
```
3. Updated database and summary will be saved.
4. Logs are stored with timestamps.

## Use Cases

- Retail: Pulling daily product feed updates
- Finance: Periodic reconciliation runs
- BI: Syncing data warehouse staging tables

## Author

Felicia Acuna  
GitHub: [fracuna1](https://github.com/fracuna1)
