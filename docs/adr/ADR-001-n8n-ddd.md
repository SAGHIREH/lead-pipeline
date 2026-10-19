# ADR-001: Using n8n with DDD Architecture
Status: Accepted
Context: The project must be professional, but without local coding.
Decision: Use n8n + Docker and divide tasks into Bounded Contexts.
Consequences: Code becomes cleaner and more testable, but requires managing multiple files.