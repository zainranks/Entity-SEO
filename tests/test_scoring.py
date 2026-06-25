from entity_seo_skill.scoring import weighted_score

def test_weighted_score_is_numeric():
    score = weighted_score({"business_relevance": 5, "conversion_value": 4})
    assert isinstance(score, float)
