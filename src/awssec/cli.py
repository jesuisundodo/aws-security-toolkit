# Disclaimer: AS-IS, no warranty. Read-only security checks. Test in sandbox first.
import argparse
import sys
from typing import List
from .aws import session as mk_session, enabled_regions, list_org_accounts
from .output import to_table, to_json, to_sarif
from .models import Finding, exit_code_from_findings
from .rules import ALL as ALL_RULES

SAFE_ACTIONS_ONLY = True

def main():
    parser = argparse.ArgumentParser(prog="awssec", description="Practical AWS Security Toolkit")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_scan = sub.add_parser("scan", help="Run one or more rules")
    p_scan.add_argument("rule", choices=sorted(ALL_RULES.keys()) + ["all"])
    p_scan.add_argument("--format", choices=["table", "json", "sarif"], default="table")
    p_scan.add_argument("--profile", help="AWS profile name")
    p_scan.add_argument("--role-arn", help="Assume this role before scanning")
    p_scan.add_argument("--external-id", help="Optional ExternalId for STS AssumeRole")
    p_scan.add_argument("--region", help="Scan only this region, else all enabled")
    p_scan.add_argument("--org-scan", action="store_true", help="List accounts via Organizations and scan each by assuming a standard role")
    p_scan.add_argument("--assume-role-name", default="AWSSEC_ReadOnly", help="Role name to assume in each account when using --org-scan")

    args = parser.parse_args()

    if not SAFE_ACTIONS_ONLY:
        print("Unsafe action set detected. Refusing to run.", file=sys.stderr)
        sys.exit(4)

    s = mk_session(profile=args.profile, region=args.region, role_arn=args.role_arn, external_id=args.external_id)
    regions = [args.region] if args.region else enabled_regions(s)

    # Determine targets
    targets = [None]
    if args.org_scan:
        accounts = list_org_accounts(s)
        targets = accounts or []

    rules = list(ALL_RULES.keys()) if args.rule == "all" else [args.rule]
    all_findings: List[Finding] = []
    exit_code = 0

    def run_rules(sess, which_regions: List[str]):
        nonlocal all_findings, exit_code
        for rname in rules:
            mod = ALL_RULES[rname]
            for region in which_regions:
                try:
                    fs = mod.scan(sess, region)
                    all_findings.extend(fs)
                except Exception as e:
                    all_findings.append(Finding(
                        id=f"{rname}-error-{region}",
                        title=f"Rule {rname} failed in {region}",
                        rule=rname,
                        severity="LOW",
                        resource="n/a",
                        region=region,
                        rationale=str(e),
                        remediation="Check permissions and network connectivity.",
                        metadata={}
                    ))
                    exit_code = 4

    if targets == [None]:
        run_rules(s, regions)
    else:
        for acc in targets:
            role_arn = f"arn:aws:iam::{acc}:role/{args.assume_role_name}"
            sess = mk_session(profile=args.profile, region=args.region, role_arn=role_arn, external_id=args.external_id)
            run_rules(sess, regions)

    if args.format == "table":
        print(to_table(all_findings))
    elif args.format == "json":
        print(to_json(all_findings))
    elif args.format == "sarif":
        print(to_sarif(all_findings))
    else:
        print("Unknown output format", file=sys.stderr)
        sys.exit(4)

    if exit_code == 4:
        sys.exit(4)
    sys.exit(exit_code_from_findings(all_findings))
