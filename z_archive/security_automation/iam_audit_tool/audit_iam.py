import boto3
from datetime import datetime, timezone
from utils.report_generator import write_csv
from tabulate import tabulate

# Connect to AWS using the profile I configured
session = boto3.Session(profile_name='grc-audit')
iam = session.client('iam')

# This will hold all the data for the final report
report_data = []

# Capture today’s date so we can calculate login inactivity
today = datetime.now(timezone.utc)

# Get a list of all IAM users in the account
users = iam.list_users()['Users']

for user in users:
    username = user['UserName']

    # Check if the user has MFA devices registered
    mfa_devices = iam.list_mfa_devices(UserName=username)['MFADevices']
    mfa_enabled = bool(mfa_devices)

    # Look at the last time the user logged in (via password)
    last_used = user.get('PasswordLastUsed')
    if last_used:
        days_since_used = (today - last_used).days
    else:
        last_used = "Never"
        days_since_used = "N/A"

    # Mark the user as inactive if it’s been 90+ days
    inactive = (
        isinstance(days_since_used, int) and days_since_used >= 90
    )

    # Check the user’s attached policies for dangerous wildcard permissions
    dangerous_policy = False
    policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
    
    for policy in policies:
        policy_version = iam.get_policy(PolicyArn=policy['PolicyArn'])['Policy']['DefaultVersionId']
        policy_doc = iam.get_policy_version(
            PolicyArn=policy['PolicyArn'],
            VersionId=policy_version
        )['PolicyVersion']['Document']

        # Policy "Statement" can be a list or a single dict, normalize it
        statements = policy_doc.get('Statement', [])
        if isinstance(statements, dict):
            statements = [statements]

        for stmt in statements:
            action = stmt.get('Action', "")
            resource = stmt.get('Resource', "")

            # Flag if the policy allows * in actions or resources
            if (
                action == "*" or
                resource == "*" or
                (isinstance(action, list) and "*" in action) or
                (isinstance(resource, list) and "*" in resource)
            ):
                dangerous_policy = True

    # Add everything we collected for this user into the report
    report_data.append({
        'Username': username,
        'MFA Enabled': 'Yes' if mfa_enabled else 'No',
        'Last Login': str(last_used) if last_used != "Never" else "Never",
        'Days Since Last Login': days_since_used if isinstance(days_since_used, int) else "-",
        'Inactive Over 90 Days': 'Yes' if inactive else 'No',
        'Has Dangerous Policy': 'Yes' if dangerous_policy else 'No'
    })

# Save the full report as a CSV
write_csv(report_data, 'output/iam_report.csv')

# Show the results in a readable table format
print("\n📋 IAM Audit Report Summary:\n")
print(tabulate(report_data, headers="keys", tablefmt="grid"))
