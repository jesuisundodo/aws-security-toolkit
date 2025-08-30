# v0.1.0 Release Notes

Highlights
- Read only CLI with two rules: root MFA and S3 public
- JSON and SARIF outputs, stable exit codes
- CI with lint, type check, tests, Bandit, pip audit
- CodeQL and Dependabot
- Policies and docs for safe setup

Install
```bash
pip install -e .[dev]
```

Quick demo
```bash
awssec scan all --format table
```

Safe use
Run in a sandbox first. Use AWSSEC_ReadOnly role with ExternalId.
