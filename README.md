# genpark-hallucination-factual-grounding-checker-skill

Agent Skill implementing **Hallucination Detection & Citation Grounding Verification** in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Claim["Model Generated Claim C"] --> TokClaim["Token Extraction & Stopword Removal"]
    Source["Retrieved Evidence Context S"] --> TokSrc["Evidence Vocabulary Index"]
    TokClaim & TokSrc --> SetDiff["Unsupported Token Set Difference C \ S"]
    SetDiff --> Metric["Support Ratio: 1 - (|Unsupported| / |Claim|)"]
    Metric --> Threshold{"Support Ratio >= 0.7?"}
    Threshold -->|True| Grounded["Factual Grounding Verified"]
    Threshold -->|False| Hallucination["Flagged as Potential Hallucination"]
```
