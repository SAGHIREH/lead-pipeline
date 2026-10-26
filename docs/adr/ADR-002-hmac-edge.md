# ADR-002: HMAC for Edge Security

Status: Accepted

Context: The webhook is public and exposed to the internet. We need to ensure requests are authentic.

Decision: Use HMAC-SHA256 signature verification at the edge (Intake). Requests without a valid signature are rejected with 401.

Consequences: Protects against unauthorized access and payload tampering, but requires clients to share a secret and generate signatures.