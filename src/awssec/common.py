
from __future__ import annotations
import boto3
from botocore.config import Config

def make_session(profile: str | None = None):
    if profile:
        return boto3.Session(profile_name=profile)
    return boto3.Session()

def client(session, service_name: str, region: str | None = None):
    cfg = Config(retries={'max_attempts': 10, 'mode': 'adaptive'})
    if region:
        return session.client(service_name, region_name=region, config=cfg)
    return session.client(service_name, config=cfg)
