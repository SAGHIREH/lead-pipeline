# ADR-005: Repository Pattern and DLQ

Status: Accepted

Context: We need a reliable way to store leads without losing data on failure, and without coupling our logic to a specific database.

Decision: Use Google Sheets as a Repository and implement a DLQ (Dead Letter Queue) for failed write operations.

Consequences: Data is safe even if Google Sheets is down, but we need to manually process the DLQ later.
