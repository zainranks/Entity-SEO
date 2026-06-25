DEFAULT_WEIGHTS = {
    "business_relevance": 1.4,
    "conversion_value": 1.3,
    "search_demand_proxy": 1.0,
    "competitor_coverage": 0.8,
    "semantic_centrality": 1.0,
    "evidence_quality": 1.2,
    "differentiation_potential": 0.9,
    "compliance_risk": -1.2,
}

def weighted_score(components: dict[str, float], weights: dict[str, float] | None = None) -> float:
    active = DEFAULT_WEIGHTS | (weights or {})
    total_weight = sum(abs(active.get(k, 0)) for k in components) or 1
    raw = sum(components[k] * active.get(k, 0) for k in components)
    return round(raw / total_weight, 4)
