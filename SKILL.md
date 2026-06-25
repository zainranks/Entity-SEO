# Entity-First SEO Content System Skill

## Mission
Build an evidence-backed entity model for a new website, convert it into information architecture and content plans, and produce reviewable briefs and drafts without creating thin pages or entity cannibalization.

## Operating principles
1. Evidence before inference.
2. Business relevance before raw entity frequency.
3. One clear primary entity and intent per page.
4. Not every entity deserves a URL.
5. Separate facts, recommendations, and assumptions.
6. Never invent `sameAs`, credentials, statistics, relationships, or source claims.
7. Use deterministic rules for validation; use LLMs for extraction, classification, and synthesis.
8. Stop automatic progression when confidence or evidence thresholds fail.

## Required inputs
Read and validate `project.yaml` against `schemas/project-input.schema.json`.

Minimum inputs:
- Brand and business type
- Products/services
- Target markets, languages, and audiences
- Conversion goals
- Seed topics
- Known competitors or permission to discover them
- Publishing constraints and regulated-topic flags

## Workflow

### Phase 0: Intake validation
- Validate required fields.
- Normalize URLs, locations, languages, and service names.
- Flag contradictory goals and missing commercial priorities.
- Output `outputs/00_intake_report.json`.

### Phase 1: Seed entity discovery
Extract entities from business facts and seed topics.
Classify as brand, organization, person, service, product, location, audience, problem, process, technology, concept, regulation, or creative work.
Output `outputs/01_seed_entities.json`.

### Phase 2: Search and competitor research
For every priority seed:
- Collect search result titles, snippets, People Also Ask, related searches, and representative ranking pages.
- Distinguish business competitors from content competitors.
- Capture source URL, query, rank/date when available, page type, headings, and visible schema.
- Respect robots, rate limits, terms, and access controls.
Output evidence to `outputs/research/`.

### Phase 3: Entity extraction
Use `prompts/entity-extraction.md`.
Every entity must have:
- canonical candidate
- observed label
- type
- evidence excerpt or source reference
- source URL/query
- page role
- confidence
- suggested relationships
Reject unsupported entities.
Output `outputs/02_raw_entities.jsonl`.

### Phase 4: Resolution and canonicalization
Apply in order:
1. Unicode and punctuation normalization
2. Singular/plural and language-aware normalization
3. Curated alias dictionary
4. Exact and fuzzy candidate matching
5. Embedding similarity as candidate generation only
6. Context/type compatibility check
7. Human review for ambiguous merges

Never merge based on lexical similarity alone.
Output:
- `outputs/03_entities.json`
- `outputs/03_aliases.csv`
- `outputs/03_merge_review.csv`

### Phase 5: Relationship graph
Create typed edges with evidence and confidence.
Allowed relations include:
- `is_a`, `part_of`, `offers`, `used_for`, `requires`, `has_component`
- `located_in`, `performed_by`, `authored_by`, `works_for`
- `solves`, `causes`, `prevents`, `compared_with`, `regulated_by`
Use `related_to` only when no more precise supported relation exists.
Output `outputs/04_entity_graph.json` and `.graphml`.

### Phase 6: Entity scoring
Score each entity from 0 to 5 on:
- business relevance
- conversion value
- search demand proxy
- competitor coverage
- semantic centrality
- evidence quality
- differentiation potential
- compliance risk

Do not use one summed score blindly. Preserve component scores and apply project weights from config.
Output `outputs/05_entity_scores.csv`.

### Phase 7: Page decision
Use `prompts/page-decision.md` and deterministic checks.
Assign one:
- Entity home
- Commercial page
- Supporting article
- Comparison page
- Location page
- Glossary/definition page
- Section within another page
- Mention only
- Reject

A standalone URL requires:
- distinct intent or user task
- enough unique substance
- business/topical role
- no unresolved overlap with planned/existing URLs
- reasonable maintenance value

Output `outputs/06_page_decisions.csv`.

### Phase 8: Site architecture and topical map
Build:
- hubs and clusters
- parent-child URL relationships
- breadcrumbs
- primary entity per page
- supporting entities
- page type and intent
- conversion role
- required internal links

Run cannibalization checks across primary entity, intent, purpose, and SERP target.
Output:
- `outputs/07_site_architecture.csv`
- `outputs/07_topical_map.json`
- `outputs/07_cannibalization_review.csv`

### Phase 9: Content briefs
Generate one brief per approved URL using `templates/content-brief.md`.
Briefs must include:
- page objective and conversion action
- primary entity and intent
- supporting entities with required context
- claims requiring verification
- outline and section purpose
- internal links in/out
- schema recommendation
- differentiation requirement
- prohibited or unsupported claims
- acceptance checks

Output to `outputs/briefs/`.

### Phase 10: Draft generation
Draft only after brief approval.
Rules:
- Answer the primary task early.
- Use entities naturally; never entity-stuff.
- Preserve terminology and aliases consistently.
- Do not fabricate facts, experience, citations, prices, or credentials.
- Mark facts needing external verification.
- Follow language, tone, and regulatory constraints.
Output to `outputs/drafts/` with a QA sidecar JSON.

### Phase 11: Internal linking
Recommend links only when they improve navigation or explain a supported relationship.
Each recommendation includes source URL, target URL, anchor concept, sentence context, relationship, and confidence.
Avoid exact-match anchor repetition and sitewide overlinking.
Output `outputs/09_internal_links.csv`.

### Phase 12: Schema recommendations
Generate schema from approved, visible facts only.
Use stable `@id` values and connect entities through `@graph`.
Do not promise rich results. Do not use `sameAs` for merely related sources.
Output `outputs/10_schema_recommendations.json`.

### Phase 13: QA gate
Run `docs/qa-checklist.md`.
Block release when:
- primary entity or intent is ambiguous
- unsupported claims remain
- duplicate entity homes exist
- page overlap exceeds threshold
- schema conflicts with visible content
- regulated content lacks required review

Output `outputs/11_qa_report.json`.

## Confidence policy
- 0.90–1.00: eligible for automatic acceptance when deterministic checks pass
- 0.75–0.89: accept with sampled review
- 0.50–0.74: mandatory review
- below 0.50: reject or research again

## Failure handling
- Preserve partial outputs.
- Log source, phase, error class, retry count, and remediation.
- Retry transient network/API errors with exponential backoff.
- Never replace missing evidence with model guesses.
- Degrade to manual research tasks when sources are inaccessible.

## Definition of done
A project is complete when all approved pages have a unique primary entity and intent, graph relationships contain evidence, aliases are resolved, cannibalization review is closed, briefs pass QA, and outputs validate against their schemas.
