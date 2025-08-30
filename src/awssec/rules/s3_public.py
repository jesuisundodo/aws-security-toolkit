# Disclaimer: Provided AS IS without warranty. Read only security checks. Test in sandbox first.
from typing import List
import botocore
from ..models import Finding

RULE_ID = "S3.PUBLIC.ACCESS"
TITLE = "S3 buckets should not be publicly accessible"
REMEDIATION = "Block public access at the account and bucket levels, and remove public ACLs and policies."

def scan(session, region: str) -> List[Finding]:
    s3 = session.client("s3", region_name=region)
    findings: List[Finding] = []
    resp = s3.list_buckets()
    buckets = [b["Name"] for b in resp.get("Buckets", [])]

    for b in buckets:
        public = False
        rationale_bits = []

        try:
            acl = s3.get_bucket_acl(Bucket=b)
            for grant in acl.get("Grants", []):
                grantee = grant.get("Grantee", {})
                uri = grantee.get("URI", "")
                if "AllUsers" in uri or "AuthenticatedUsers" in uri:
                    public = True
                    rationale_bits.append("Public ACL grant present")
                    break
        except botocore.exceptions.ClientError:
            pass

        try:
            pol = s3.get_bucket_policy(Bucket=b)
            if pol and pol.get("Policy"):
                try:
                    status = s3.get_bucket_policy_status(Bucket=b)
                    if status["PolicyStatus"]["IsPublic"]:
                        public = True
                        rationale_bits.append("Bucket policy allows public access")
                except botocore.exceptions.ClientError:
                    pass
        except botocore.exceptions.ClientError:
            pass

        try:
            pab = s3.get_bucket_public_access_block(Bucket=b)
            cfg = pab.get("PublicAccessBlockConfiguration", {})
            wanted = ["BlockPublicAcls", "IgnorePublicAcls", "BlockPublicPolicy", "RestrictPublicBuckets"]
            if not all(cfg.get(k, False) for k in wanted):
                if not public:
                    findings.append(Finding(
                        id=f"{b}-weak-public-access-block",
                        title="S3 Public Access Block not fully enabled",
                        rule=RULE_ID,
                        severity="MEDIUM",
                        resource=b,
                        region=region,
                        rationale="One or more Public Access Block settings are disabled.",
                        remediation="Enable all four Public Access Block settings for the bucket and at the account level.",
                        metadata={"pab": cfg}
                    ))
                continue
        except botocore.exceptions.ClientError:
            pass

        if public:
            findings.append(Finding(
                id=f"{b}-public",
                title=TITLE,
                rule=RULE_ID,
                severity="HIGH",
                resource=b,
                region=region,
                rationale="; ".join(rationale_bits) or "Heuristic public access detected.",
                remediation=REMEDIATION,
                metadata={}
            ))
    return findings
