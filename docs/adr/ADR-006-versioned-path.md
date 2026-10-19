# ADR-006: Versioned Path /webhook/v1/leads
Status: Accepted
Context: Future changes should not break existing clients.
Decision: The version is placed in the URL (/v1/).
Consequences: Gradual migration to v2 is possible; cost: maintaining multiple versions.