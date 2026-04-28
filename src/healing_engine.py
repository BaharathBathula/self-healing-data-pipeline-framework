import yaml
from datetime import datetime
from src.audit_logger import AuditLogger


class HealingEngine:
    def __init__(self, config_path: str):
        with open(config_path, "r") as file:
            self.rules = yaml.safe_load(file)["rules"]
        self.audit_logger = AuditLogger()

    def evaluate_event(self, event: dict) -> dict:
        for rule in self.rules:
            if event.get("condition") == rule.get("condition"):
                result = self.execute_action(rule, event)
                self.audit_logger.log(result)
                return result

        result = {
            "timestamp": datetime.utcnow().isoformat(),
            "pipeline": event.get("pipeline"),
            "status": "no_action",
            "message": "No matching healing rule found"
        }
        self.audit_logger.log(result)
        return result

    def execute_action(self, rule: dict, event: dict) -> dict:
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "pipeline": event.get("pipeline"),
            "condition": event.get("condition"),
            "issue": rule["id"],
            "severity": rule["severity"],
            "diagnosis": rule["diagnosis"],
            "selected_action": rule["action"],
            "fallback_action": rule["fallback_action"],
            "status": "healed"
        }
