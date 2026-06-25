import re
import unicodedata

_ARABIC_DIACRITICS = re.compile(r"[\u0617-\u061A\u064B-\u0652]")

def normalize_label(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold().strip()
    value = _ARABIC_DIACRITICS.sub("", value)
    value = re.sub(r"[^\w\s\u0600-\u06FF]", " ", value)
    return re.sub(r"\s+", " ", value).strip()

def exact_alias_key(value: str) -> str:
    return normalize_label(value)
