# Public Data Importer

This project automates the extraction and ingestion of publicly available data via APIs into a structured relational database format. It’s designed to simulate a common data engineering workflow where external data sources are regularly queried, transformed, and stored for analysis.

## Features

- Fetches data from a public API (e.g., OpenWeatherMap, transport, or COVID statistics)
- Normalizes raw JSON into structured tabular format
- Stores transformed records into a local SQLite or MySQL database
- Includes basic error handling and logging
- Supports scheduled data pulls via script automation

## Tools & Technologies

- Python
- Requests (for API calls)
- Pandas (for transformation)
- SQLite or MySQL (for storage)
- Logging library

## Folder Structure

```
public-data-importer/
├── data_fetcher.py          # Script to call the API
├── transform_store.py       # Normalization and DB logic
├── config.json              # API keys and parameters
├── logs/                    # Log files
└── README.md
```

## Setup Instructions

1. Clone the repository.
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `config.json` with your API key and parameters.
4. Run:
   ```
   python data_fetcher.py
   ```
5. Optionally schedule with cron or Task Scheduler.

## Use Case Example

Used to regularly pull and archive weather data for city trend analysis. Can be adapted for finance, traffic, or other domains.

## License

MIT License.
