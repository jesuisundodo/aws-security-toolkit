
# AWS Security Toolkit

[![CI](https://github.com/aleksandarnenov/aws-security-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/aleksandarnenov/aws-security-toolkit/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![AWS](https://img.shields.io/badge/AWS-Security-orange.svg)](https://aws.amazon.com/security/)

Practical AWS security checks with a single CLI. Covers IAM MFA, S3 public exposure, CloudTrail coverage, and Security Group open ports. Includes AWS Config rule samples, a remediation Lambda pattern, and CI workflows.

## Features

- CLI `awssec` with subcommands:
  - `iam-mfa` list IAM users without MFA
  - `s3-public` detect public S3 buckets or missing Block Public Access
  - `cloudtrail` verify CloudTrail logging across enabled regions
  - `sg-open` list security groups open to the world on risky ports
- Python package layout with tests
- GitHub Actions for CI and an optional scheduled scan
- AWS Config rule samples
- Minimal remediation Lambda for S3 Block Public Access

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .[dev]
awssec --help

awssec iam-mfa --profile default
awssec s3-public --profile default
awssec cloudtrail --profile default
awssec sg-open --profile default --region eu-central-1
```

## Usage and docs

See [docs/USAGE.md](docs/USAGE.md).

---

## Disclaimers

- Educational use only. Use in controlled environments first. Review and adapt before production.
- No warranty. Provided "as is" and used at your own risk.
- Security reporting. Please open a private security advisory rather than a public issue. See [SECURITY.md](SECURITY.md).
- Not affiliated with AWS. Community project only.
