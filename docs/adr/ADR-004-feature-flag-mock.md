# ADR-004: Feature Flag for Mock Fallback
Status: Accepted
Context: We need to test the system without consuming API quotas and handle external service failures gracefully.
Decision: Use `ENRICHMENT_MODE` env variable. Default is `live`. If an error occurs, fallback to `mock` with `enrichment_status="mock_fallback"`.
Consequences: System remains fail-open (always processes leads), but downstream systems must handle mock data.