![Database](https://img.shields.io/badge/SQL-MySQL%20%7C%20PostgreSQL-blue)
![Diagram](https://img.shields.io/badge/ERD-Included-yellow)
![Status](https://img.shields.io/badge/Schema-Designed-success)

# Logistics Database Model

This project presents a relational database schema tailored for a logistics company. The schema supports the management of shipments, warehouses, customers, inventory, and delivery routes. It is designed to be scalable and serve as the backbone of data analysis for supply chain performance.

## Features

- Entity-relationship model (ERD) covering logistics operations
- SQL schema including table creation scripts
- Sample SQL queries for reporting and analysis
- Clear documentation of relationships and normalization

## Technologies Used

- MySQL / PostgreSQL (schema design and queries)
- Draw.io / dbdiagram.io (ERD diagrams)
- SQL (DDL + DML scripts)

## Folder Structure

```
logistics-database-model/
├── schema/
│   ├── create_tables.sql
│   ├── sample_queries.sql
├── diagrams/
│   └── erd_logistics.png
└── README.md
```

## Key Tables

- `shipments`: Tracks outgoing and incoming shipments
- `warehouses`: Contains info on warehouse locations and capacities
- `inventory`: Links SKUs to warehouses and quantity levels
- `routes`: Defines shipping paths and transit times
- `customers`: Customer info and delivery addresses

## ERD Overview

The ERD defines the core logistics model with normalized relationships between shipments, inventory, warehouses, and customers. It allows analysts to run complex joins for shipping times, stock levels, and customer service performance.

## Use Cases

- Enable KPI dashboards like order-to-delivery time or stock turnover
- Simplify reporting on warehouse utilization and customer delivery accuracy
- Serve as the backend schema for apps or data ingestion pipelines

## How to Use

1. Load the schema from `schema/create_tables.sql` into your local MySQL or PostgreSQL database.
2. Run `schema/sample_queries.sql` to explore data analytics queries.
3. Refer to the ERD image under `diagrams/` for visualizing the table relationships.

## Author

Felicia Acuna  
GitHub: [fracuna1](https://github.com/fracuna1)
