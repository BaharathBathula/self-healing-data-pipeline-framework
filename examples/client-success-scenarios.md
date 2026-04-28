# Client Success Scenarios

1. Missing partition detected → Auto backfill completed in 3 mins
2. Schema drift detected → Field mapping repaired automatically
3. Upstream delay → Switched to fallback source
4. Null spike → Quarantined corrupted records
5. Runtime spike → Re-ran with scaled compute
