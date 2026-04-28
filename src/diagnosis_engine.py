class DiagnosisEngine:
    def diagnose(self, condition: str) -> str:
        mapping = {
            "schema_version_changed": "schema_drift",
            "expected_partition_missing": "partition_missing",
            "null_percentage_above_threshold": "data_quality_degradation",
            "runtime_exceeds_baseline": "compute_or_dependency_issue",
            "freshness_lag_exceeds_sla": "source_delay"
        }
        return mapping.get(condition, "unknown")
