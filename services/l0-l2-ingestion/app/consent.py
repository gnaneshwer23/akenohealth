from datetime import datetime, timezone


def validate_consent_token(consent_token: str) -> bool:
    # Placeholder token format: consent:<unix_expiry_ts>
    if not consent_token or not consent_token.startswith("consent:"):
        return False
    try:
        expiry = int(consent_token.split(":", 1)[1])
    except (ValueError, IndexError):
        return False
    now_ts = int(datetime.now(timezone.utc).timestamp())
    return expiry > now_ts
