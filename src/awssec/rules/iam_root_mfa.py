# Disclaimer: AS-IS, no warranty. Read-only security checks. Test in sandbox first.
from typing import List
import botocore
from ..models import Finding

RULE_ID = "IAM.ROOT.MFA"
TITLE = "Root account must have MFA enabled"
REMEDIATION = "Enable MFA for the root user and avoid using root for daily operations."

def scan(session, region: str) -> List[Finding]:
    iam = session.client("iam", region_name=region)
    try:
        summary = iam.get_account_summary()["SummaryMap"]
        mfa_enabled = summary.get("AccountMFAEnabled", 0) == 1
        if mfa_enabled:
            return []
        return [Finding(
            id="root-mfa-missing",
            title=TITLE,
            rule=RULE_ID,
            severity="HIGH",
            resource="arn:aws:iam:::root",
            region=region,
            rationale="Account summary indicates root MFA is disabled.",
            remediation=REMEDIATION,
            metadata={"AccountMFAEnabled": summary.get("AccountMFAEnabled", 0)}
        )]
    except botocore.exceptions.ClientError as e:
        raise
