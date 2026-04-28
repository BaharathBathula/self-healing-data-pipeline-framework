import yaml
from datetime import datetime


class HealingEngine:
    def __init__(self, config_path):
        with open(config_path, "r") as file:
            self.rules = yaml.safe_load(file)["rules"]

    def evaluate_event(self, event):
        for rule in self.rules:
            if event["condition"] == rule["condition"]:
                return self.execute_action(rule, event)
        return {"status": "no_action", "message": "No matching rule found"}

    def execute_action(self, rule, event):
        return {
            "timestamp": str(datetime.utcnow()),
            "issue": rule["id"],
            "severity": rule["severity"],
            "selected_action": rule["action"],
            "pipeline": event["pipeline"],
            "status": "healed"
        }


if __name__ == "__main__":
    engine = HealingEngine("config/healing_rules.yaml")

    sample_event = {
        "pipeline": "daily_sales_etl",
        "condition": "expected_partition_missing"
    }

    result = engine.evaluate_event(sample_event)
    print(result)
