class DetectionEngine:
    def detect(self, telemetry: dict) -> dict:
        if telemetry["freshness_lag_minutes"] > 10:
            return {
                "pipeline": telemetry["pipeline"],
                "condition": "freshness_lag_exceeds_sla"
            }

        if telemetry["null_percentage"] > 5:
            return {
                "pipeline": telemetry["pipeline"],
                "condition": "null_percentage_above_threshold"
            }

        return {
            "pipeline": telemetry["pipeline"],
            "condition": "normal"
        }
