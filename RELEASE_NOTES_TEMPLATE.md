# Disclaimer
This software is provided **AS-IS**, without any warranty or guarantee of fitness for a particular purpose. 
Use at your own risk. Intended for **read-only security checks** only. 
Always test in a **sandbox AWS account** before any production use.

## AWS Security Toolkit v0.1.0

**Status:** MVP, read-only, safe by default

### Highlights
- CLI with two starter rules
- Multi-region by default, org-scan scaffold
- Outputs: table, json, sarif
- Stable exit codes
- Policies and SECURITY policy

### Quick start
```bash
awssec scan all --format table
```
