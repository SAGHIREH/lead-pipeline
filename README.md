# Lead Intake & Enrichment Pipeline
**Path: FULL PATH**

## Overview
A professional system for receiving, validating, and storing Leads using Domain-Driven Design (DDD) architecture on n8n.

## Architecture
```mermaid
graph LR
  C[Client] -->|POST /v1/leads| I[Intake BC]