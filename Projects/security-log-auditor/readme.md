# Security Log Auditor

This project is a lightweight log auditing tool designed to process and evaluate Identity and Access Management (IAM) logs for anomalies and data quality issues. It simulates a basic compliance check system often used in cybersecurity and IT governance.

## Features

- Parses IAM log files in JSON format
- Detects and flags missing or malformed fields
- Identifies duplicate entries and timestamp inconsistencies
- Generates a simple audit report summarizing issues found
- Supports custom schema rules (via Python)

## Tools Used

- Python 3
- SQLite (optional for structured log storage)
- JSON handling (via `json` module)
- Tabular CLI output (via `tabulate`)
- Optionally deployable as a CLI script or API endpoint (Flask)

## Project Structure

```
security-log-auditor/
├── logs/                  # Sample log files (input)
├── audit/                 # Output reports
├── src/
│   ├── parser.py          # Parses and validates logs
│   ├── reporter.py        # Generates summary reports
│   └── main.py            # Main runner script
└── README.md
```

## How to Run

1. Place your JSON log files in the `logs/` folder.
2. Run the audit with:

```bash
python3 src/main.py
```

3. Review the audit output in the `audit/` directory.

## Use Case

This project simulates real-world log ingestion pipelines used in security operations. It's ideal for showcasing data engineering skills relevant to security compliance, log processing, and automation.

## Sample Output

```
Audit Report - IAM Log Audit
-----------------------------
File: user-access-log-2025-07-01.json
✓ Parsed 320 log entries
⚠ 12 entries with missing timestamps
⚠ 5 entries with malformed user_id
✓ No duplicate session IDs found
```

## Author

Felicia Acuna
