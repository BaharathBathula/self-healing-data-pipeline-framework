from src.healing_engine import HealingEngine


engine = HealingEngine("config/healing_rules.yaml")

events = [
    {
        "pipeline": "daily_policy_etl",
        "condition": "schema_version_changed"
    },
    {
        "pipeline": "claims_fact_pipeline",
        "condition": "expected_partition_missing"
    },
    {
        "pipeline": "customer_profile_load",
        "condition": "null_percentage_above_threshold"
    }
]

for event in events:
    result = engine.evaluate_event(event)
    print(result)
