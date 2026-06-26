# Akeno Health Platform (Full-Stack Multi-AMC)

This repository is an implementation starter kit for the full L0-L10 architecture:

- L0-L2 data foundation and interoperability
- L3-L4 AI intelligence, explainability, and clinical governance
- L5-L7 care operations and federated learning loops
- L8-L10 strategic expansion for privacy vault, autonomous agents, and ecosystem APIs

## Repository Layout

- `docs/` - architecture, KPIs, governance, execution playbooks
- `contracts/` - canonical data contracts and interoperability mappings
- `infra/` - local infrastructure manifests and platform bootstrapping
- `services/l0-l2-ingestion/` - ingestion, consent, and patient context services
- `services/l3-l4-ai-safety/` - model scoring, XAI, and safety guardrail services
- `services/l7-federated/` - federated training orchestration and evaluation
- `services/l8-l10-expansion/` - ecosystem, autonomous agent, and privacy-vault tracks

## Phase-Aligned Deliverables

### Phase 0
- KPI threshold framework: `docs/kpi-framework.md`
- Service boundaries and architecture: `docs/architecture/service-boundaries.md`
- Governance and compliance controls:
  - `docs/governance/raci.md`
  - `docs/compliance/control-library.md`

### Phase 1 (L0-L2)
- Canonical healthcare data contracts: `contracts/canonical-data-model.md`
- Ingestion and patient context service skeleton:
  - `services/l0-l2-ingestion/app/main.py`
  - `services/l0-l2-ingestion/app/pipeline.py`
  - `services/l0-l2-ingestion/app/patient_context.py`

### Phase 2 (L3-L4)
- Safe AI stack skeleton:
  - `services/l3-l4-ai-safety/app/main.py`
  - `services/l3-l4-ai-safety/app/guardrails.py`
  - `services/l3-l4-ai-safety/app/xai.py`
  - `services/l3-l4-ai-safety/config/validation_policy.yaml`

### Phase 4+ (L7-L10)
- Federated loop skeleton:
  - `services/l7-federated/app/orchestrator.py`
  - `services/l7-federated/app/secure_aggregation.py`
- Expansion tracks roadmap:
  - `services/l8-l10-expansion/roadmap.md`

## Local Infrastructure

See `infra/docker-compose.yml` for baseline local stack:

- Postgres (operational and audit metadata)
- Neo4j (longitudinal patient graph)
- Kafka (streaming ingestion and event transport)

## Quick Start

1. Review the KPI and architecture docs in `docs/`.
2. Bring up local stack:
   - `cd infra && docker compose up --build -d`
3. Run smoke test:
   - `bash scripts/e2e_smoke_test.sh`
4. Run phase gates using checklists in `docs/execution/`.

## Clinical Safety and Compliance

This repo provides engineering scaffolding only. Production use requires:

- Clinical validation and IRB approvals
- Country/region-specific regulatory review
- Security audits and penetration tests
