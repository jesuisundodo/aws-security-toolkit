import boto3
from moto import mock_aws
from awssec.rules import iam_root_mfa

@mock_aws
def test_root_mfa_missing_flags_high(monkeypatch):
    s = boto3.Session(region_name="us-east-1")
    iam = s.client("iam")

    def fake_get_account_summary():
        return {"SummaryMap": {"AccountMFAEnabled": 0}}
    monkeypatch.setattr(iam, "get_account_summary", fake_get_account_summary)

    findings = iam_root_mfa.scan(s, "us-east-1")
    assert len(findings) == 1
    assert findings[0].severity == "HIGH"
    assert findings[0].rule == "IAM.ROOT.MFA"
