from typing import Any, Dict


def build_patient_context(patient_key: str) -> Dict[str, Any]:
    # Placeholder context. Replace with live FHIR bundle and graph query joins.
    return {
        "patientKey": patient_key,
        "bundle": {"resourceType": "Bundle", "type": "collection", "entry": []},
        "graphSummary": {
            "nodeCount": 0,
            "edgeCount": 0,
            "lastUpdated": "1970-01-01T00:00:00Z",
        },
        "riskSignals": [],
        "consentState": {
            "active": True,
            "scope": ["care", "analytics"],
            "expiresAt": "2099-01-01T00:00:00Z",
        },
    }
