
# AWS Security Toolkit

A practical, lightweight toolkit to audit AWS accounts for common misconfigurations and baseline security gaps.  
**Safe by default:** all operations are **read-only**, using a least-privilege IAM role.

## Features
- 🚀 Easy CLI: `awssec scan all`
- 🔒 Safe by design: no write actions, least-privilege IAM policy provided
- 📦 Outputs: table, JSON, SARIF (for GitHub Code Scanning)
- 🌍 Multi-region and multi-account scanning with AssumeRole
- 🧩 Modular rules: add new checks easily
- 🛠️ CI-ready: exit codes per severity, coverage reports, security linting

## Installation
```bash
pip install -e .[dev]
```

## Quick Start
```bash
awssec scan all --format table
```

## Example Checks
```bash
awssec scan iam-root-mfa --format table
awssec scan s3-public --format json
awssec scan all --format sarif   --role-arn arn:aws:iam::<ACC>:role/AWSSEC_ReadOnly   --external-id <YourExternalId>
```

## Outputs
| Format  | Use case                               |
|---------|---------------------------------------|
| table   | Local audit, quick inspection         |
| json    | CI/CD pipelines, integrations         |
| sarif   | Upload to GitHub Security Code Scanning |

## Exit Codes
| Code | Meaning                     |
|------|-----------------------------|
| 0    | No findings                 |
| 1    | Only Medium/Low findings    |
| 2    | High findings present       |
| 4    | Internal error / permissions|

## Safe Use
- Provided `policies/read-only-scan-policy.json` defines **List/Get/Describe** only.
- Use a dedicated `AWSSEC_ReadOnly` role in each account with an ExternalId.
- Scanner refuses to run if unsafe actions are detected.

## Development
```bash
pytest -q --cov=src
ruff check .
mypy src
pip-audit
```

## Contributing
Contributions welcome! Add new checks under `src/awssec/rules/`.
