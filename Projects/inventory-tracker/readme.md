![Language](https://img.shields.io/badge/Python-3.10-blue)
![Database](https://img.shields.io/badge/MongoDB-NoSQL-lightgrey)
![Status](https://img.shields.io/badge/CRUD-Complete-brightgreen)

# Inventory Tracker

A lightweight NoSQL-based inventory tracking system for managing product catalogs with unstructured data.

## Overview

This project simulates a backend inventory tracker using MongoDB. It allows you to store and retrieve product data in flexible JSON format, ideal for businesses needing to manage varying product attributes.

## Features

- Store product details in NoSQL format (MongoDB)
- CRUD operations using Python scripts
- Flexible schema for varying product attributes
- Query inventory by category, name, or availability

## Tech Stack

- MongoDB Atlas (or local MongoDB)
- Python (PyMongo)
- Sample JSON data

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/inventory-tracker.git
   cd inventory-tracker
   ```

2. Create a `.env` file with your MongoDB URI:
   ```
   MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/inventory
   ```

3. Run sample CRUD operations:
   ```bash
   python add_product.py
   python get_products.py
   python update_product.py
   python delete_product.py
   ```

4. View output in terminal or connected MongoDB database.

## Example Use Case

This tool can be adapted to:
- Track warehouse inventory
- Manage product listings for small e-commerce sites
- Store unstructured catalog data for analytics

## Folder Structure

```
inventory-tracker/
├── add_product.py
├── get_products.py
├── update_product.py
├── delete_product.py
├── sample_data/
│   └── products.json
└── README.md
```

## Author

Felicia Acuna
