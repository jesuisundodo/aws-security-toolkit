# Disclaimer: Provided AS IS without warranty. Read only security checks. Test in sandbox first.
import json
from typing import List
from tabulate import tabulate
from .models import Finding

def to_table(findings: List[Finding]) -> str:
    rows = [[f.severity, f.rule, f.resource, f.region, f.title] for f in findings]
    return tabulate(rows, headers=["Severity", "Rule", "Resource", "Region", "Title"])

def to_json(findings: List[Finding]) -> str:
    return json.dumps([f.to_dict() for f in findings], indent=2, sort_keys=True)

def to_sarif(findings: List[Finding]) -> str:
    rules = {}
    for f in findings:
        if f.rule not in rules:
            rules[f.rule] = {
                "id": f.rule,
                "shortDescription": {"text": f.title},
                "help": {"text": f.rationale + " Remediation: " + f.remediation}
            }
    results = []
    for f in findings:
        results.append({
            "ruleId": f.rule,
            "level": sev_to_level(f.severity),
            "message": {"text": f.title},
            "locations": [{
                "physicalLocation": {
                    "artifactLocation": {"uri": f.resource},
                    "region": {"startLine": 1}
                }
            }],
            "properties": {"region": f.region, **(f.metadata or {})}
        })
    sarif = {
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {"name": "awssec", "rules": list(rules.values())}},
            "results": results
        }]
    }
    return json.dumps(sarif, indent=2, sort_keys=True)

def sev_to_level(sev: str) -> str:
    s = sev.upper()
    if s == "HIGH":
        return "error"
    if s == "MEDIUM":
        return "warning"
    if s == "LOW":
        return "note"
    return "none"
