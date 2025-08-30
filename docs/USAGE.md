# Disclaimer
This software is provided **AS-IS**, without any warranty or guarantee of fitness for a particular purpose. 
Use at your own risk. Intended for **read-only security checks** only. 
Always test in a **sandbox AWS account** before any production use.

## Quick start
```bash
pip install -e .[dev]
awssec scan all --format table
```

## Multi-account scan
```bash
awssec scan all --org-scan --assume-role-name AWSSEC_ReadOnly --external-id <ID> --format json
```

## Outputs
- table: local inspection
- json: pipelines and tooling
- sarif: GitHub Code Scanning ingestion

## Exit codes
0 no findings, 1 medium or low only, 2 high findings, 4 internal errors
