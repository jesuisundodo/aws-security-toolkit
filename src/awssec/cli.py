
from __future__ import annotations
import argparse, json
from .common import make_session
from . import check_iam_mfa, check_s3_public, check_cloudtrail_all_regions, check_sg_open_ports

def main(argv=None):
    parser = argparse.ArgumentParser(prog="awssec", description="AWS Security Toolkit CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p1 = sub.add_parser("iam-mfa", help="List IAM users without MFA")
    p1.add_argument("--profile")

    p2 = sub.add_parser("s3-public", help="Detect public S3 buckets")
    p2.add_argument("--profile")

    p3 = sub.add_parser("cloudtrail", help="Verify CloudTrail logging across enabled regions")
    p3.add_argument("--profile")

    p4 = sub.add_parser("sg-open", help="Find SGs open to the world on risky ports")
    p4.add_argument("--profile")
    p4.add_argument("--region")

    args = parser.parse_args(argv)
    session = make_session(args.profile)

    if args.command == "iam-mfa":
        res = check_iam_mfa.run(session)
    elif args.command == "s3-public":
        res = check_s3_public.run(session)
    elif args.command == "cloudtrail":
        res = check_cloudtrail_all_regions.run(session)
    elif args.command == "sg-open":
        res = check_sg_open_ports.run(session, region=args.region)
    else:
        parser.error("Unknown command")

    print(json.dumps(res, indent=2, default=str))

if __name__ == "__main__":
    main()
