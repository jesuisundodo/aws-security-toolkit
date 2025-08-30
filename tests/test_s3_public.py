import boto3
from moto import mock_aws
from awssec.rules import s3_public

@mock_aws
def test_s3_public_bucket_detected():
    s = boto3.Session(region_name="us-east-1")
    s3 = s.client("s3")
    s3.create_bucket(Bucket="public-bucket")
    s3.put_bucket_acl(
        Bucket="public-bucket",
        AccessControlPolicy={
            "Grants": [{
                "Grantee": {"Type": "Group", "URI": "http://acs.amazonaws.com/groups/global/AllUsers"},
                "Permission": "READ"
            }],
            "Owner": {"DisplayName": "owner", "ID": "ownerid"}
        },
    )
    findings = s3_public.scan(s, "us-east-1")
    assert any(f.resource == "public-bucket" and f.severity == "HIGH" for f in findings)

@mock_aws
def test_s3_private_bucket_clean():
    s = boto3.Session(region_name="us-east-1")
    s3 = s.client("s3")
    s3.create_bucket(Bucket="private-bucket")
    findings = s3_public.scan(s, "us-east-1")
    assert all(f.resource != "private-bucket" for f in findings)
