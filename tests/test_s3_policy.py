
from awssec.check_s3_public import is_public_policy

def test_is_public_policy():
    pub = {
        "Version": "2012-10-17",
        "Statement": [
            {"Effect": "Allow", "Principal": "*", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::b/*"}
        ]
    }
    assert is_public_policy(pub) is True

    not_pub = {
        "Version": "2012-10-17",
        "Statement": [
            {"Effect": "Deny", "Principal": "*", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::b/*"}
        ]
    }
    assert is_public_policy(not_pub) is False
