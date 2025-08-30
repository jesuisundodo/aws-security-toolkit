
# Usage

Use an AWS profile locally. For CI use OIDC and a role to assume.

Examples:
```bash
awssec iam-mfa --profile default
awssec s3-public --profile default
awssec cloudtrail --profile default
awssec sg-open --profile default --region eu-central-1
```
