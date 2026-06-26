from typing import Dict, Any


SUPPORTED_PAYLOAD_TYPES = {"FHIR_RESOURCE", "FHIR_BUNDLE", "HL7V2", "DICOM_META", "CUSTOM"}


def route_to_standard(payload_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    if payload_type not in SUPPORTED_PAYLOAD_TYPES:
        raise ValueError(f"Unsupported payload type: {payload_type}")
    # Placeholder transformation. Replace with actual adapter transforms.
    return {"standardizedType": payload_type, "standardizedPayload": payload}
