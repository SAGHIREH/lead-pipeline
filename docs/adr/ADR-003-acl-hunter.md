# ADR-003: Anti-Corruption Layer for Hunter.io
Status: Accepted
Context: Hunter.io output is complex and may change. We don't want its schema to pollute our internal model.
Decision: Use an ACL (Code node) to map Hunter's response to our `Company` value object.
Consequences: Internal logic is isolated from external API changes, but we must maintain the mapping code.