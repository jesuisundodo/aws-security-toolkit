# AWS Security Toolkit

> Disclaimer  
> Provided AS IS without warranty. Use at your own risk. Read only checks. Test in sandbox first.

A practical, lightweight toolkit to audit AWS accounts for common misconfigurations and baseline security gaps.

## Features
- Easy CLI: `awssec scan all`
- Safe by design: no write actions, least privilege IAM policy
- Outputs: table, JSON, SARIF
- Multi region and multi account with AssumeRole
- Modular rules
- CI ready exit codes

## Install
```bash
pip install -e .[dev]
```

## Quick start
```bash
awssec scan all --format table
```

## Examples
```bash
awssec scan iam-root-mfa --format table
awssec scan s3-public --format json
awssec scan all --format sarif --role-arn arn:aws:iam::<ACC>:role/AWSSEC_ReadOnly --external-id <ID>
```

## Exit codes
0 clean, 1 medium or low only, 2 any high, 4 internal error

## Safe use
Use policies in policies/ and a dedicated AWSSEC_ReadOnly role. Run from a security account and enable MFA and CloudTrail.

## Contributing
Add new checks under src/awssec/rules/
