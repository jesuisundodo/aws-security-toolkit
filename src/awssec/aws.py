# Disclaimer: Provided AS IS without warranty. Read only security checks. Test in sandbox first.
import boto3
import botocore
import os
from typing import List, Optional

def session(profile: Optional[str] = None, region: Optional[str] = None, role_arn: Optional[str] = None, external_id: Optional[str] = None) -> boto3.Session:
    base = boto3.Session(profile_name=profile, region_name=region)
    if role_arn:
        sts = base.client("sts")
        kwargs = {"RoleArn": role_arn, "RoleSessionName": "awssec-scan"}
        if external_id:
            kwargs["ExternalId"] = external_id
        creds = sts.assume_role(**kwargs)["Credentials"]
        return boto3.Session(
            aws_access_key_id=creds["AccessKeyId"],
            aws_secret_access_key=creds["SecretAccessKey"],
            aws_session_token=creds["SessionToken"],
            region_name=region,
        )
    return base

def enabled_regions(s: boto3.Session) -> List[str]:
    try:
        ec2 = s.client("ec2")
        resp = ec2.describe_regions(AllRegions=False)
        return sorted([r["RegionName"] for r in resp.get("Regions", [])])
    except botocore.exceptions.BotoCoreError:
        return [s.region_name or os.environ.get("AWS_REGION") or "us-east-1"]

def list_org_accounts(s: boto3.Session) -> List[str]:
    try:
        org = s.client("organizations")
        accs = []
        token = None
        while True:
            kwargs = {"NextToken": token} if token else {}
            resp = org.list_accounts(**kwargs)
            accs.extend([a["Id"] for a in resp.get("Accounts", []) if a.get("Status") == "ACTIVE"])
            token = resp.get("NextToken")
            if not token:
                break
        return accs
    except Exception:
        return []
