# Lead Intake & Enrichment Pipeline
**Path: FULL PATH : Hunter.io live + Google Sheets OAuth + Slack Webhook (mock fallback only for forced failures via ENRICHMENT_MODE).**



## Overview
A professional system for receiving, validating, and storing Leads using Domain-Driven Design (DDD) architecture on n8n.

## Architecture
```mermaid
graph LR
  C[Client] -->|POST /v1/leads| I[Intake BC]
