
# Disclaimer
This project is provided **AS-IS** without any warranty.  
Use at your own risk. It is intended for **read-only security checks**.  
Always test in a **sandbox account** before using in production.



# Changelog

All notable changes to **AWS Security Toolkit** will be documented here.

## [0.1.0] - 2025-08-30
### Added
- **Initial CLI** with subcommands for scanning AWS accounts:
  - `iam-root-mfa` rule checks for root MFA enforcement.
  - `s3-public` rule detects publicly accessible buckets and weak Public Access Block settings.
- **Output formats**: `table`, `json`, and `sarif` for GitHub Code Scanning integration.
- **Exit codes**:
  - `0` no findings, `1` medium/low findings, `2` high findings, `4` internal errors.
- **IAM Policy & Trust Policy** for least-privilege, read-only scanning role (`AWSSEC_ReadOnly`).
- **Multi-account, multi-region scanning** with `--role-arn` and `--external-id` flags.
- **Security-focused CI pipeline**: Ruff, Black, mypy, Bandit, pip-audit, pytest coverage.
- **Pre-commit hooks** for linting and type checking.
- **Tests with Moto** for S3 and IAM rules.

### Documentation
- `README.md` with safe-use guide, quick start, outputs table, and contribution notes.
- `docs/USAGE.md` with commands, exit code table, safe-use section, and multi-account setup steps.

### Project Structure
- `src/awssec/` modules for CLI, rules, AWS session utilities, models, and outputs.
- `policies/` directory for IAM JSON policy and trust policy templates.
- `tests/` directory with golden tests.
- `.github/workflows/ci.yml` and `.pre-commit-config.yaml` for modern workflows.

---
This release marks the **first MVP** of the AWS Security Toolkit.  
Focus is **read-only checks**, strong **safety posture**, and **CI/CD readiness**.
