
from __future__ import annotations
import json
from .common import client

def is_public_policy(doc: dict) -> bool:
    for stmt in doc.get("Statement", []):
        effect = stmt.get("Effect")
        principal = stmt.get("Principal")
        if effect != "Allow":
            continue
        if principal == "*" or principal == {"AWS": "*"}:
            return True
    return False

def run(session):
    s3 = client(session, "s3")
    buckets = [b["Name"] for b in s3.list_buckets().get("Buckets", [])]
    findings = []
    for b in buckets:
        item = {"bucket": b, "public_access_block": None, "policy_public": None, "acl_public": None}

        try:
            pab = s3.get_public_access_block(Bucket=b)["PublicAccessBlockConfiguration"]
            item["public_access_block"] = pab
        except s3.exceptions.NoSuchPublicAccessBlockConfiguration:
            item["public_access_block"] = "MISSING"
        except Exception:
            item["public_access_block"] = "UNKNOWN"

        try:
            pol = s3.get_bucket_policy(Bucket=b)
            doc = json.loads(pol["Policy"])
            item["policy_public"] = is_public_policy(doc)
        except Exception:
            item["policy_public"] = False

        try:
            acl = s3.get_bucket_acl(Bucket=b)
            grants = acl.get("Grants", [])
            item["acl_public"] = any(
                g.get("Grantee", {}).get("URI", "").endswith("AllUsers")
                or g.get("Grantee", {}).get("URI", "").endswith("AuthenticatedUsers")
                for g in grants
            )
        except Exception:
            item["acl_public"] = "UNKNOWN"

        if item["policy_public"] is True or item["acl_public"] is True or item["public_access_block"] == "MISSING":
            findings.append(item)
    return findings
