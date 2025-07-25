# Security Automation Projects

This section of my portfolio highlights security-focused tools I've built around identity management, audit automation, and compliance workflows.

While I haven't held a formal DevOps or security engineer title yet, many of my projects reflect real-world tasks performed by GRC and DevOps teams — like auditing IAM users, checking for risky permissions, and preparing SOC 2 audit evidence.

These tools are based on problems I’ve personally encountered while working with internal platforms, backend workflows, and access control systems.

## Projects

### [iam_audit_tool](./iam_audit_tool)
A Python tool that connects to AWS IAM and audits users for:
- Missing MFA
- Inactive accounts (90+ days)
- Wildcard or overly permissive policies (`Action: *`, `Resource: *`)
- Exports results to CSV and prints a readable terminal summary table

✅ Useful for IAM reviews, least privilege enforcement, and preparing for SOC 2 or ISO 27001 audits.

---

### [soc2_evidence_collector](./soc2_evidence_collector)
**Coming soon:** A script to automatically collect audit evidence from AWS, including:
- CloudTrail logging status
- Root user activity
- Password policy enforcement
- Security config baselines (like GuardDuty + Config)

✅ Helps automate part of the evidence collection process for SOC 2 compliance.

---

### [aws_compliance_scanner](./aws_compliance_scanner)
**Planned:** A future tool that scans AWS accounts for common misconfigurations, like:
- Public S3 buckets
- Disabled encryption
- Missing logging

✅ Based on CIS-style AWS security benchmarks.

---

## Why I'm Building These

During my internship, I worked with secure data pipelines, backend authentication, and workflow automation. I saw firsthand how slow and manual compliance checks can be — especially around IAM and logging.

These projects are my way of bridging the gap between traditional software development and the kind of security-aware engineering that helps businesses stay audit-ready and protected.
