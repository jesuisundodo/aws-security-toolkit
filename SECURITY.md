
# Disclaimer
This project is provided **AS-IS** without any warranty.  
Use at your own risk. It is intended for **read-only security checks**.  
Always test in a **sandbox account** before using in production.



# Security Policy

Thank you for helping keep this project and its users safe.

## Supported Versions
This project is in **v0.1.0 (MVP)**. All versions are supported for security reports.

## Reporting a Vulnerability
If you believe you have found a security vulnerability:

1. **Do NOT create a public GitHub issue.**
2. Email the maintainer privately: **aleksandarnenov [at] gmail.com**
3. Include:
   - A detailed description of the vulnerability
   - Steps to reproduce
   - A proof of concept if possible
4. Expect a reply within **7 days**. We will coordinate on a fix before public disclosure.

## Scope
- The toolkit codebase in this repository
- Packaged releases from this repository

## Out of Scope
- Issues caused by misconfiguration of AWS services or IAM policies outside of this repository
- Incidents in third-party environments not directly related to this code

## Security Best Practices
- Always use the **least-privilege IAM policy** provided in `policies/`
- Run scans from a dedicated **security account** with read-only roles
- Enable **multi-factor authentication (MFA)** and **CloudTrail logging** in all accounts
