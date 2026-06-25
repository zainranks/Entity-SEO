from typing import Literal
from pydantic import BaseModel, Field

class Evidence(BaseModel):
    source: str
    excerpt: str
    query: str | None = None

class Relationship(BaseModel):
    target: str
    relation: str
    confidence: float = Field(ge=0, le=1)
    evidence: list[Evidence] = []

class Entity(BaseModel):
    entity_id: str
    canonical_name: str
    observed_labels: list[str] = []
    entity_type: str
    role: Literal["primary", "supporting", "mentioned", "candidate"] = "candidate"
    confidence: float = Field(ge=0, le=1)
    evidence: list[Evidence] = []
    relationships: list[Relationship] = []

class PageDecision(BaseModel):
    entity_id: str
    decision: Literal[
        "entity_home", "commercial_page", "supporting_article", "comparison_page",
        "location_page", "glossary_page", "section", "mention", "reject"
    ]
    primary_intent: str
    parent_entity_id: str | None = None
    rationale: str
    confidence: float = Field(ge=0, le=1)
