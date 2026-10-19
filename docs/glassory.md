# Glossary
- **Lead**: A potential customer or prospect who has submitted their information.
- **Bounded Context**: A specific boundary within the system that has a single responsibility (e.g., the Intake BC).
- **Value Object**: An object that is defined only by its attributes and values, not by identity (e.g., an email address where uppercase and lowercase letters are treated the same).
- **Domain Event**: Something that happens in the system (e.g., the "LeadReceived" event).
- **ACL (Anti-Corruption Layer)**: A translator layer that converts external systems' data into our system's language/model.
- **Webhook**: A URL endpoint where data is sent to trigger an automated workflow.
- **Idempotency**: The property that if a request is sent multiple times, the system processes and records its effect only once.