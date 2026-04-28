class RemediationEngine:
    def remediate(self, action: str) -> str:
        actions = {
            "schema_remap": "Applied schema remapping workflow",
            "backfill_partition": "Triggered partition backfill",
            "quarantine_bad_records": "Moved bad records to quarantine zone",
            "retry_with_scaled_compute": "Retried job with additional compute",
            "switch_to_fallback_source": "Switched to fallback data source"
        }
        return actions.get(action, "No remediation action available")
