# Shipping Insights

This project simulates an ETL (Extract, Transform, Load) pipeline for logistics and supply chain operations. The focus is on extracting shipment and warehouse CSV data, transforming it using Python and Pandas, and loading it into a structured SQLite database. The final output includes summary tables used for analytical reporting and operations tracking.

## Features

- Extracts shipment and warehouse data from CSV files
- Cleans and transforms raw logistics data
- Stores processed data in a relational SQLite database
- Generates summary tables with key shipping metrics

## Tools & Technologies

- Python
- Pandas
- SQLite
- CSV

## Folder Structure

```
shipping-insights/
├── data/               # Sample CSV shipment data
├── etl/                # ETL scripts (extract, transform, load)
├── db/                 # SQLite database files
├── reports/            # Output summary reports
└── README.md
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/shipping-insights.git
cd shipping-insights
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the ETL pipeline:
```bash
python etl/run_etl.py
```

5. Explore the generated reports in the `reports/` folder.

## Use Cases

- Logistics departments needing to streamline shipment data ingestion and reporting
- Data engineers demonstrating transformation logic for supply chain datasets
- Educational reference for building ETL pipelines with Python and SQLite
