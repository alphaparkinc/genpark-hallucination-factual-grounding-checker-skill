"""Factual Grounding & Hallucination Verifier.
100% Python Standard Library.
"""

import re

class GroundingChecker:
    """Evaluates lexical grounding and token support between claims and source context."""
    @staticmethod
    def evaluate(claim, source_context):
        claim_words = [w.lower() for w in re.findall(r'\b\w+\b', claim) if len(w) > 2]
        source_words = set(w.lower() for w in re.findall(r'\b\w+\b', source_context))
        if not claim_words:
            return {"grounded_ratio": 1.0, "is_grounded": True, "unsupported_terms": []}
        unsupported = [w for w in claim_words if w not in source_words]
        ratio = 1.0 - (len(unsupported) / len(claim_words))
        return {
            "grounded_ratio": round(ratio, 4),
            "is_grounded": ratio >= 0.7,
            "unsupported_terms": unsupported
        }
