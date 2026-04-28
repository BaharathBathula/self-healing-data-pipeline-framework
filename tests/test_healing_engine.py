from src.healing_engine import HealingEngine


def test_schema_drift_healing():
    engine = HealingEngine("config/healing_rules.yaml")

    event = {
        "pipeline": "daily_policy_etl",
        "condition": "schema_version_changed"
    }

    result = engine.evaluate_event(event)

    assert result["status"] == "healed"
    assert result["selected_action"] == "schema_remap"
    assert result["severity"] == "high"
