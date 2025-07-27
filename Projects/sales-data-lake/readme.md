![Language](https://img.shields.io/badge/PySpark-Databricks-red)
![Status](https://img.shields.io/badge/Data%20Lake-Bronze%20%7C%20Silver%20%7C%20Gold-green)
![Streaming](https://img.shields.io/badge/Simulation-On%20Interval-yellow)

# Sales Data Lake

This project simulates a cloud-based data lake pipeline designed for processing sales transaction data. It showcases how to ingest raw files, transform and enrich the data, and promote it through bronze, silver, and gold layers using PySpark.

## Features

- Ingests raw CSV sales data
- Cleans and transforms using PySpark
- Implements a Bronze → Silver → Gold layered approach
- Tracks data lineage and versioning with Delta Lake
- Produces a final analytical view of daily sales metrics

## Tools & Technologies

- Databricks Community Edition (PySpark)
- Delta Lake
- CSV / Parquet file formats

## Folder Structure

```
sales-data-lake/
├── notebooks/
│   ├── 01_ingest_bronze.py
│   ├── 02_transform_silver.py
│   └── 03_aggregate_gold.py
├── data/
│   ├── raw/
│   └── reference/
├── output/
└── README.md
```

## Setup Instructions

1. Create a free [Databricks Community Edition](https://community.cloud.databricks.com/) account
2. Upload the provided notebooks and sample data to your workspace
3. Run each notebook step-by-step to promote data from Bronze to Gold
4. Review the Gold layer outputs to verify transformed sales analytics

## Example Use Cases

- Demonstrates ETL layering logic in cloud environments
- Shows how to structure large-scale data pipelines
- Great baseline project for data engineering interviews

## Author

Felicia Acuna
