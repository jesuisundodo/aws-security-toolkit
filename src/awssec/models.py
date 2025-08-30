# Disclaimer: AS-IS, no warranty. Read-only security checks. Test in sandbox first.
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any, List

@dataclass
class Finding:
    id: str
    title: str
    rule: str
    severity: str  # LOW | MEDIUM | HIGH | INFO
    resource: str  # ARN or name
    region: str
    rationale: str
    remediation: str
    metadata: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["metadata"] = d.get("metadata") or {}
        return d

def exit_code_from_findings(findings: List['Finding']) -> int:
    severities = {f.severity.upper() for f in findings}
    if "HIGH" in severities:
        return 2
    if "MEDIUM" in severities:
        return 1
    return 0
