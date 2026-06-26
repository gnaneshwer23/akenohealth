from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional
from uuid import uuid4

import psycopg


def register_patient(dsn: str, patient_key: str, display_name: str) -> Dict[str, Any]:
    with psycopg.connect(dsn) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO patients (patient_key, display_name)
                VALUES (%s, %s)
                ON CONFLICT (patient_key) DO UPDATE SET display_name = EXCLUDED.display_name
                RETURNING patient_key, display_name, created_at
                """,
                (patient_key, display_name),
            )
            row = cur.fetchone()
    return {"patientKey": row[0], "displayName": row[1], "createdAt": row[2].isoformat()}


def grant_consent(
    dsn: str,
    patient_key: str,
    scopes: List[str],
    hours_valid: int = 24,
    proxy_key: Optional[str] = None,
) -> Dict[str, Any]:
    token = f"consent:{uuid4().hex}"
    expires_at = datetime.now(timezone.utc) + timedelta(hours=hours_valid)
    with psycopg.connect(dsn) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM patients WHERE patient_key = %s", (patient_key,))
            if not cur.fetchone():
                raise ValueError(f"Unknown patient_key: {patient_key}")
            cur.execute(
                """
                INSERT INTO consent_grants (token, patient_key, scopes, proxy_key, expires_at)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING token, patient_key, scopes, proxy_key, expires_at
                """,
                (token, patient_key, scopes, proxy_key, expires_at),
            )
            row = cur.fetchone()
    return {
        "token": row[0],
        "patientKey": row[1],
        "scopes": row[2],
        "proxyKey": row[3],
        "expiresAt": row[4].isoformat(),
    }


def revoke_consent(dsn: str, token: str) -> Dict[str, Any]:
    with psycopg.connect(dsn) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE consent_grants
                SET revoked_at = NOW()
                WHERE token = %s AND revoked_at IS NULL
                RETURNING token, patient_key
                """,
                (token,),
            )
            row = cur.fetchone()
    if not row:
        raise ValueError("Consent token not found or already revoked")
    return {"token": row[0], "patientKey": row[1], "revoked": True}


def validate_consent(dsn: str, token: str) -> Dict[str, Any]:
    with psycopg.connect(dsn) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT token, patient_key, scopes, proxy_key, expires_at, revoked_at
                FROM consent_grants
                WHERE token = %s
                """,
                (token,),
            )
            row = cur.fetchone()
    if not row:
        return {"valid": False, "reason": "token_not_found"}
    if row[5] is not None:
        return {"valid": False, "reason": "revoked"}
    if row[4] < datetime.now(timezone.utc):
        return {"valid": False, "reason": "expired"}
    return {
        "valid": True,
        "token": row[0],
        "patientKey": row[1],
        "scopes": row[2],
        "proxyKey": row[3],
        "expiresAt": row[4].isoformat(),
    }
