# Disclaimer
This software is provided **AS-IS**, without any warranty or guarantee of fitness for a particular purpose. 
Use at your own risk. Intended for **read-only security checks** only. 
Always test in a **sandbox AWS account** before any production use.

# AWS Security Toolkit


![CI](https://github.com/aleksandarnenov/aws-security-toolkit/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/aleksandarnenov/aws-security-toolkit/actions/workflows/codeql.yml/badge.svg)
[![Coverage](https://codecov.io/gh/aleksandarnenov/aws-security-toolkit/branch/main/graph/badge.svg)](https://codecov.io/gh/aleksandarnenov/aws-security-toolkit)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)


A practical, lightweight toolkit to audit AWS accounts for common misconfigurations and baseline security gaps.

## Features
- Easy CLI: `awssec scan all`
- Safe by design: no write actions, least-privilege IAM policy
- Outputs: table, JSON, SARIF
- Multi-region and optional multi-account with AssumeRole
- Modular rules
- CI-ready exit codes

## Install
```bash
pip install -e .[dev]
```

## Quick start
```bash
awssec scan all --format table
awssec scan iam-root-mfa --format table
awssec scan s3-public --format json
awssec scan all --org-scan --assume-role-name AWSSEC_ReadOnly --external-id <ID> --format sarif
```

## Compare
- **Prowler**: large compliance scanner for frameworks.
- **AWS SRA Verify**: validates alignment with AWS Security Reference Architecture.
- **AWS Security Toolkit**: fast baseline checker for presales, workshops, and CI guardrails.

## Exit codes
0 no findings, 1 medium or low only, 2 any high, 4 internal error

## Safe use
Use policies in `policies/` and a dedicated `AWSSEC_ReadOnly` role. Run from a security account and enable MFA and CloudTrail.
