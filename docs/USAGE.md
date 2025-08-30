# Usage

> Disclaimer  
> Provided AS IS without warranty. Use at your own risk. Read only checks. Test in sandbox first.

## Quick start
```bash
pip install -e .[dev]
awssec scan all --format table
```

## Multi account
```bash
# list accounts via Organizations and scan each by assuming AWSSEC_ReadOnly
awssec scan all --org-scan --assume-role-name AWSSEC_ReadOnly --external-id <ID> --format json
```

## Outputs
table for humans, json for pipelines, sarif for GitHub Code Scanning

## Exit codes
0 no findings, 1 medium or low only, 2 high findings, 4 internal errors
