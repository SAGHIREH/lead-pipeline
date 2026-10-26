# Demo Video Recording Guide (Day 7)

## Scene 1: Intro & Architecture (30s)
- Show the README and the Mermaid Context Map.
- Explain: "This is a Lead Intake & Enrichment Pipeline built with n8n, following DDD principles."

## Scene 2: Valid Lead -> Storage + Notification (60s)
- Use `curl.ps1` to send a valid lead.
- Show the n8n workflow running (Green path).
- Show the Google Sheet with the new row.
- Show the Slack channel receiving the notification.

## Scene 3: Invalid Data -> 422 Error (30s)
- Modify `curl.ps1` to remove the email field.
- Run it, show the terminal returning `422 VALIDATION_FAILED`.

## Scene 4: Bad Signature -> 401 Error (20s)
- Modify `curl.ps1` to use a wrong signature.
- Run it, show the terminal returning `401 INVALID_SIGNATURE`.

## Scene 5: Duplicate Lead (45s)
- Send the same valid lead again.
- Show the n8n workflow (True path - Dedup).
- Show the Google Sheet: `times_seen` increased, no new row added.
- Show that NO Slack notification was sent.

## Scene 6: DLQ (Forced Failure) (30s)
- Break the Google Sheet name in n8n (e.g., `leads_wrong`).
- Send a valid lead.
- Show the n8n Error path triggering and saving to the `dlq` tab in Google Sheets.

## Scene 7: Repo Tour & CI Badge (30s)
- Show the VS Code folder structure.
- Show the GitHub Actions tab with the green CI badge.

## Scene 8: Outro (15s)
- "Thank you for watching. The project is fully documented and available on GitHub."