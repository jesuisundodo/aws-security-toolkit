
from __future__ import annotations
from .common import client

def enabled_regions(session):
    ec2 = client(session, "ec2")
    regions = ec2.describe_regions(AllRegions=False)["Regions"]
    return [r["RegionName"] for r in regions]

def run(session):
    missing = []
    for r in enabled_regions(session):
        ct = client(session, "cloudtrail", region=r)
        trails = ct.describe_trails(includeShadowTrails=False).get("trailList", [])
        has_logging = False
        for t in trails:
            status = ct.get_trail_status(Name=t["Name"])
            if status.get("IsLogging"):
                has_logging = True
                break
        if not has_logging:
            missing.append(r)
    return missing
