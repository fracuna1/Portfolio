# IAM Audit Automation Tool

A Python-based automation script I created to audit AWS IAM configurations for common security and compliance risks.

## Features
- Checks whether MFA is enabled for each IAM user
- Flags users that haven’t logged in for 90+ days
- Detects overly permissive IAM policies (like `*` in Action or Resource)
- Saves results to a CSV file for reporting
- Prints a clean summary table in the terminal using `tabulate`

## Tools & Tech Used
- Python 3.12
- Boto3 (AWS SDK)
- AWS CLI (profile-based authentication)
- tabulate (for formatting terminal output)
- Virtualenv

## Folder Structure

```
iam_audit_tool/
├── audit_iam.py            # Main script
├── utils/
│   └── report_generator.py # CSV export function
├── output/
│   └── iam_report.csv      # Generated audit report
├── venv/                   # Virtual environment
├── README.md               # Project description
└── requirements.txt        # Package list
```

## How to Run It

### 1. Clone this repo and open the folder
```bash
git clone https://github.com/your-username/iam_audit_tool.git
cd iam_audit_tool
```

### 2. Set up your Python environment
```bash
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up your AWS CLI profile
```bash
aws configure --profile grc-audit
```

### 4. Run the script
```bash
py audit_iam.py
```

### Output:
- `output/iam_report.csv` – contains the audit results
- Terminal displays a table with all users and findings

---

## Why I Made This

While working on cloud automation and GRC tooling, I found that IAM reviews were tedious and often done manually. This tool helps automate the most common checks you'd perform when preparing for an audit or reviewing access across an AWS environment. It ties into SOC 2 and ISO 27001 practices like enforcing MFA and least privilege.

---

## Sample Output (Terminal)

```
+------------------+--------------+-------------+------------------------+------------------------+------------------------+
| Username         | MFA Enabled  | Last Login  | Days Since Last Login  | Inactive Over 90 Days  | Has Dangerous Policy   |
+------------------+--------------+-------------+------------------------+------------------------+------------------------+
| grc-audit-user   | No           | Never       | -                      | No                     | No                     |
+------------------+--------------+-------------+------------------------+------------------------+------------------------+
```

---

## Permissions Tip

The IAM user you run this with should have the `IAMReadOnlyAccess` policy or similar so it can fetch user and policy details without modifying anything.