
import boto3
s3 = boto3.client("s3")
def handler(event, context):
    bucket = event.get("bucket")
    if not bucket:
        return {"status": "no-bucket"}
    s3.put_public_access_block(
        Bucket=bucket,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": True,
            "IgnorePublicAcls": True,
            "BlockPublicPolicy": True,
            "RestrictPublicBuckets": True
        }
    )
    return {"status": "ok", "bucket": bucket}
