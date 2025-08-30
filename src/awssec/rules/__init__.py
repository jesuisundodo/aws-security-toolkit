# Disclaimer: Provided AS IS without warranty. Read only security checks. Test in sandbox first.
from . import iam_root_mfa, s3_public
ALL = {
    "iam-root-mfa": iam_root_mfa,
    "s3-public": s3_public,
}
