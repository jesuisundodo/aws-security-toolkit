
# S3 Block Public Access Enforcer

Pattern to enforce Block Public Access if a bucket policy becomes public.

- Trigger by EventBridge on PutBucketPolicy or PutBucketAcl
- Action: put_public_access_block

This is a sample. Validate in a non production account.
