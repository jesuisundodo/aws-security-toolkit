
from __future__ import annotations
from .common import client

def run(session):
    iam = client(session, "iam")
    paginator = iam.get_paginator('list_users')
    no_mfa = []
    for page in paginator.paginate():
        for user in page.get('Users', []):
            mfas = iam.list_mfa_devices(UserName=user['UserName']).get('MFADevices', [])
            if not mfas:
                no_mfa.append(user['UserName'])
    return no_mfa
