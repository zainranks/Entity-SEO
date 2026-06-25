# Entity extraction prompt

Extract only entities explicitly supported by the supplied evidence.

Return JSON matching the entity output schema. For each entity include canonical candidate, observed label, entity type, page role, evidence, source reference, confidence, and typed relationship candidates.

Rules:
- Do not invent entities, relationships, aliases, identifiers, or sameAs URLs.
- Separate named entities from domain concepts, services, products, problems, processes, technologies, people, organizations, places, regulations, and creative works.
- Prefer a precise type over `Thing`.
- Evidence must be traceable to the supplied source.
- Lower confidence when identity, scope, or relationship is ambiguous.
- Navigation and boilerplate do not establish topical importance.
