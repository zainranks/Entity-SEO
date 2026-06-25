from entity_seo_skill.normalization import normalize_label

def test_normalizes_arabic_diacritics_and_spacing():
    assert normalize_label("  زِراعةُ   الأسنان! ") == "زراعة الاسنان"
