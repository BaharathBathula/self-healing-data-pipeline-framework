# Architecture Diagram

```text
                ┌──────────────────────┐
                │   Source Systems     │
                │ APIs / DB / Files    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Ingestion Layer    │
                │ Batch / Streaming    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Pipeline Execution   │
                │ Spark / ETL / DAGs   │
                └──────────┬───────────┘
                           │
                           ▼
              ┌────────────────────────────┐
              │ Self-Healing Control Plane │
              │ Detection / Diagnosis /    │
              │ Recovery / Learning        │
              └──────────┬─────────────────┘
                         │
                         ▼
                ┌──────────────────────┐
                │ Warehouse/Lakehouse  │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Audit / Metrics      │
                └──────────────────────┘
```
