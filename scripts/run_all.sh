
#!/usr/bin/env bash
set -euo pipefail
PROFILE="${1:-default}"
REGION="${2:-}"
awssec iam-mfa --profile "$PROFILE" || true
awssec s3-public --profile "$PROFILE" || true
awssec cloudtrail --profile "$PROFILE" || true
if [ -n "$REGION" ]; then
  awssec sg-open --profile "$PROFILE" --region "$REGION" || true
else
  awssec sg-open --profile "$PROFILE" || true
fi
