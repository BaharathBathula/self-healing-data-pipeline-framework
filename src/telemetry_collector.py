class TelemetryCollector:
    def collect(self, pipeline_name: str) -> dict:
        return {
            "pipeline": pipeline_name,
            "runtime_seconds": 420,
            "row_count": 95000,
            "null_percentage": 2.1,
            "freshness_lag_minutes": 15,
            "schema_version": "v2"
        }
