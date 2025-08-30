
from __future__ import annotations
from .common import client

RISKY_PORTS = [22, 3389, 3306, 5432]

def run(session, region: str | None = None):
    findings = []
    regions = [region] if region else [r["RegionName"] for r in client(session, "ec2").describe_regions()["Regions"]]
    for r in regions:
        ec2 = client(session, "ec2", region=r)
        sgs = ec2.describe_security_groups()["SecurityGroups"]
        for sg in sgs:
            for perm in sg.get("IpPermissions", []):
                from_p = perm.get("FromPort")
                to_p = perm.get("ToPort")
                if from_p is None or to_p is None:
                    continue
                ip_ranges = [ip.get("CidrIp") for ip in perm.get("IpRanges", [])]
                if "0.0.0.0/0" in ip_ranges:
                    for port in RISKY_PORTS:
                        if from_p <= port <= to_p:
                            findings.append({"region": r, "group_id": sg["GroupId"], "port": port})
    return findings
