import json
from pathlib import Path


class AuditLogger:
    def __init__(self, log_path: str = "audit_log.jsonl"):
        self.log_path = Path(log_path)

    def log(self, event: dict) -> None:
        with self.log_path.open("a") as file:
            file.write(json.dumps(event) + "\n")
