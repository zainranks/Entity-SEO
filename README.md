دي صفحة README جاهزة للنسخ داخل README.md:

Entity-First SEO Content Skill

A comprehensive framework for planning, structuring, and producing entity-led websites and content using Codex or Claude Code.

The skill helps transform a business brief, seed topics, competitor inputs, and research sources into a structured entity map, topical architecture, content briefs, internal linking plans, schema recommendations, and quality-controlled drafts.

What This Project Does

This project is designed for new websites and content expansion projects where entity coverage needs to be planned before writing pages.

#It supports the full workflow:

Business Brief
→ Seed Entity Discovery
→ SERP and Competitor Research
→ Entity Extraction
→ Entity Resolution
→ Entity Scoring
→ Entity Graph
→ Site Architecture
→ Topic Clusters
→ Page Decisions
→ Content Briefs
→ Draft Generation
→ Internal Linking
→ Schema Recommendations
→ QA

The system does not treat every keyword or extracted term as a page opportunity. Each entity is evaluated and assigned one of the following roles:

* Entity home
* Supporting page
* Section within another page
* Contextual mention
* Rejected entity

This prevents thin content, topic duplication, and entity cannibalization.

#Core Outputs

##The skill can generate:

* Canonical entity inventory
* Entity aliases and normalized names
* Entity relationship graph
* Seed topic expansion
* Competitor entity coverage analysis
* Entity scoring and prioritization
* Topic clusters
* Site architecture
* Page, section, mention, or reject decisions
* Search intent classification
* Cannibalization risk checks
* Content gap analysis
* Content briefs
* Page outlines
* Internal linking plans
* Schema recommendations
* Content QA reports
* Confidence scores and evidence references

#Typical generated files:

outputs/
├── entities.json
├── entity_aliases.json
├── entity_graph.json
├── entity_map.csv
├── topic_clusters.csv
├── page_plan.csv
├── internal_link_plan.csv
├── schema_recommendations.json
├── qa_report.json
└── content_briefs/

#Repository Structure

.
├── CLAUDE.md
├── CODEX.md
├── README.md
├── SKILL.md
├── pyproject.toml
├── docs/
├── examples/
├── prompts/
├── schemas/
├── src/
│   └── entity_seo_skill/
├── templates/
└── tests/

#Main Files

##File	Purpose
SKILL.md	Main operating instructions and execution workflow
CLAUDE.md	Claude Code-specific instructions
CODEX.md	Codex-specific instructions
examples/	Example business briefs and project inputs
prompts/	Structured prompts for extraction, classification, briefs, and QA
schemas/	JSON schemas for validating inputs and outputs
templates/	Reusable templates for briefs, entity maps, and reports
src/entity_seo_skill/	Python package and CLI
tests/	Automated validation tests

#Requirements

* Python 3.11 or later
* Codex or Claude Code
* Internet access for SERP and competitor research
* Optional API access for search, crawling, NLP, or LLM providers

#Recommended production components:

Python
PostgreSQL or SQLite
Pydantic
Typer
httpx
BeautifulSoup
Playwright
pandas
NetworkX
RapidFuzz
pytest

#Installation

Clone the repository:

git clone https://github.com/zainranks/Entity-SEO.git
cd Entity-SEO

Create a virtual environment:

python -m venv .venv

Activate it.

macOS or Linux:

source .venv/bin/activate

Windows:

.venv\Scripts\activate

Install the package:

pip install -e .

For development dependencies:

pip install -e ".[dev]"

Quick Start

Copy the example project file:

cp examples/project.example.yaml project.yaml

Edit project.yaml with the business and market information:

business:
  name: Example Brand
  type: ProfessionalService
  description: SEO consultancy serving ecommerce businesses
  services:
    - Technical SEO
    - Ecommerce SEO
    - Content Strategy
  products: []
  locations:
    - Egypt
  audience:
    - Ecommerce founders
    - Marketing teams
market:
  language: en
  country: EG
  industry: Search Engine Optimization
seed_topics:
  - Technical SEO
  - Ecommerce SEO
  - Content Strategy
competitors:
  - https://example-competitor.com
constraints:
  publishing_mode: draft_only
  require_human_approval: true

#Validate the project configuration:

python -m entity_seo_skill.cli validate project.yaml

Then give the repository to Codex or Claude Code and instruct it to follow SKILL.md.

#Example instruction:

Read SKILL.md and CODEX.md.
Use project.yaml as the source configuration.
Run the complete entity-first SEO workflow.
Do not skip entity resolution, page-decision validation, cannibalization checks, or QA.
Save all outputs inside outputs/.

#For Claude Code:

Read SKILL.md and CLAUDE.md.
Use project.yaml as the project input.
Execute each phase in order and validate every generated artifact against the schemas directory.
Do not publish content automatically.

Workflow

1. Business Intake

The system starts with the business itself.

Required inputs include:

* Brand name
* Business type
* Services
* Products
* Locations
* Target audience
* Commercial goals
* Seed topics
* Language and country
* Known competitors

The business brief is the primary source for commercial relevance. Search data alone must not dictate the site architecture.

2. Seed Entity Discovery

#Initial entities are extracted from:

* Brand information
* Services
* Products
* Locations
* Audience
* Industry
* Seed topics
* Conversion goals

These entities become the starting points for research.

3. Entity Expansion

Each seed entity is expanded through related dimensions such as:

* Types
* Components
* Processes
* Problems
* Solutions
* Tools
* Technologies
* People
* Organizations
* Locations
* Regulations
* Comparisons
* Use cases
* Risks
* Alternatives

4. SERP Research

The skill analyzes search results for each priority seed topic.

Research may include:

* Titles
* Meta descriptions
* Headings
* People Also Ask questions
* Related searches
* Ranking page structures
* Repeated concepts
* Named entities
* Products
* Tools
* Organizations
* Locations
* Schema types

SERP repetition is treated as evidence, not truth. Repeated low-value concepts are not automatically accepted.

5. Competitor Research

The system separates:

* Business competitors
* Search competitors
* Content competitors

This distinction matters because a ranking publisher may have strong informational coverage but no commercial similarity to the target business.

Competitor analysis records:

* Entities covered
* Page types
* Content depth
* Internal link patterns
* Service coverage
* Topic clusters
* Schema usage
* Missing topics
* Weak or duplicated coverage

6. Entity Extraction

Entities must be extracted using structured outputs.

Each extracted entity should include:

{
  "canonical_name": "Technical SEO",
  "entity_type": "Concept",
  "role": "primary",
  "aliases": [
    "Technical Search Engine Optimization"
  ],
  "relationships": [
    {
      "target": "Crawling",
      "relationship": "includes"
    }
  ],
  "evidence": [
    "Supported source excerpt or source reference"
  ],
  "confidence": 0.94
}

Entities without evidence should not enter the approved graph.

7. Entity Resolution

Duplicate and ambiguous entities must be resolved before planning pages.

Resolution methods include:

1. Exact normalized matching
2. Alias dictionary matching
3. Fuzzy similarity
4. Embedding similarity
5. Relationship comparison
6. LLM-assisted validation
7. Human review for uncertain cases

Examples:

SEO
Search Engine Optimization
تحسين محركات البحث

These may represent one canonical entity.

However:

Google Ads
Google AdSense

These must remain separate entities despite lexical similarity.

8. Entity Scoring

Entities are scored using multiple factors:

* Business relevance
* Search opportunity
* Semantic importance
* Competitor coverage
* Conversion value
* Topical centrality
* Evidence quality
* Content differentiation
* Maintenance cost
* Cannibalization risk

A high entity score does not automatically mean the entity deserves its own page.

9. Page Decision

Each entity receives one final content decision.

Entity Home

A canonical page representing an important business or topical entity.

Examples:

* Main service
* Product category
* Location
* Expert profile
* Core topic

Supporting Page

A separate page supporting a parent entity.

Examples:

* Process
* Comparison
* Risk
* Cost
* Eligibility
* Use case

Section

The entity should appear as a section inside another page.

Examples:

* Component
* Material
* Minor process step
* Supporting technology

Mention

The entity only requires contextual mention.

Reject

The entity is irrelevant, unsupported, duplicative, too weak, or commercially useless.

10. Entity Graph

The approved entity graph defines relationships such as:

is_a
part_of
offers
requires
used_for
located_in
authored_by
works_for
founded_by
has_component
has_service
has_product
related_to

Generic related_to relationships should be minimized. Specific relationships provide more useful architecture and content guidance.

11. Site Architecture

The entity graph is converted into a site structure.

Example:

Home
├── Services
│   ├── Technical SEO
│   │   ├── Crawl Budget
│   │   ├── Log File Analysis
│   │   └── JavaScript SEO
│   ├── Ecommerce SEO
│   └── Content Strategy
├── Industries
├── Resources
├── Case Studies
└── About

The architecture must reflect:

* Business priorities
* Entity relationships
* Search intent
* Conversion paths
* Content depth
* Internal PageRank flow

12. Cannibalization Prevention

Before approving a page, the system checks for overlap in:

* Primary entity
* Search intent
* Page purpose
* Target audience
* SERP target
* Content angle
* Conversion goal

Two pages mentioning the same entity do not automatically cannibalize each other.

Cannibalization risk increases when the same entity, intent, and page purpose overlap.

13. Content Brief Generation

Each approved page receives a structured brief containing:

* Page objective
* Primary entity
* Supporting entities
* Search intent
* Target audience
* Funnel stage
* Recommended page type
* Parent page
* Related pages
* Required relationships
* Required sections
* Questions to answer
* Internal link targets
* External evidence requirements
* Schema recommendation
* Conversion action
* Differentiation requirements
* Prohibited overlap
* QA criteria

14. Draft Generation

Drafts must follow the approved brief.

Draft rules:

* Do not invent facts
* Do not invent credentials
* Do not invent statistics
* Do not invent testimonials
* Do not create fake experts
* Do not force every supporting entity into the copy
* Avoid keyword stuffing
* Avoid repetitive introductions
* Match the required search intent
* Preserve the entity relationships from the brief
* Add unresolved facts to a review queue

15. Internal Linking

Internal links are derived from entity relationships and page hierarchy.

Recommended link types:

* Parent to child
* Child to parent
* Sibling pages where contextually relevant
* Supporting page to entity home
* Informational page to commercial page
* Author page to authored content
* Location page to relevant services

Anchor text should describe the destination entity or purpose.

Avoid:

Click here
Read more
Learn more

when a descriptive anchor is possible.

16. Schema Recommendations

Schema recommendations are generated only from verified information.

Possible types include:

* Organization
* LocalBusiness
* Person
* ProfilePage
* Service
* Product
* Article
* BlogPosting
* WebPage
* WebSite
* BreadcrumbList
* FAQPage
* DefinedTerm

Schema must match visible page content.

The system must not invent:

* Ratings
* Reviews
* Prices
* Credentials
* Founding dates
* Locations
* Awards
* Social profiles
* SameAs URLs

17. Quality Assurance

QA checks include:

* Entity evidence coverage
* Duplicate entity detection
* Alias conflicts
* Missing primary entity
* Multiple primary entities
* Weak page justification
* Entity cannibalization
* Unsupported relationships
* Missing internal links
* Orphan pages
* Invalid schema recommendations
* Brief and outline mismatch
* Draft and brief mismatch
* Missing conversion path
* Insufficient differentiation
* Low-confidence entities
* Unsupported claims

Research Principles

The project follows these principles:

1. Evidence before inference
2. Business relevance before raw search volume
3. Entity resolution before page planning
4. Page justification before content generation
5. Human review before publishing
6. Specific relationships before generic associations
7. Structured outputs before prose outputs
8. Deterministic rules before unnecessary LLM decisions

Safety and Publishing Rules

This package defaults to:

Research
→ Planning
→ Draft generation
→ Human review

It must not automatically publish content unless the project configuration explicitly enables publishing and the implementation includes approval controls.

Recommended default:

constraints:
  publishing_mode: draft_only
  require_human_approval: true

Validation

Run the project tests:

pytest

Validate the input file:

python -m entity_seo_skill.cli validate project.yaml

Validate generated outputs:

python -m entity_seo_skill.cli validate-outputs outputs/

Example Project

Example input files are available inside:

examples/

Use them as a starting point, then replace:

* Business information
* Services
* Locations
* Seed topics
* Competitors
* Language
* Market
* Constraints

Recommended Execution Order

Do not skip phases.

1. Validate project input
2. Extract seed entities
3. Expand entity neighborhoods
4. Collect SERP evidence
5. Analyze competitors
6. Extract entities
7. Normalize aliases
8. Resolve duplicates
9. Score entities
10. Build entity graph
11. Assign page decisions
12. Build topical map
13. Build site architecture
14. Run cannibalization checks
15. Generate content briefs
16. Generate internal linking plan
17. Generate schema recommendations
18. Generate drafts
19. Run QA
20. Submit for human review

Using Codex

Read:

CODEX.md
SKILL.md

Then run:

Use project.yaml as the source configuration.
Follow every phase in SKILL.md.
Validate all outputs against schemas/.
Do not skip entity resolution, page decisions, cannibalization checks, or QA.
Do not publish automatically.

Using Claude Code

Read:

CLAUDE.md
SKILL.md

Then run:

Execute the entity-first SEO workflow using project.yaml.
Save all research evidence and generated artifacts.
Do not accept entities without evidence.
Do not generate pages before entity resolution and page-decision approval.
Do not publish content automatically.

Project Status

Current version:

Comprehensive v1

Primary focus:

* New website entity planning
* Topical architecture
* Entity-led content production
* Structured research
* Content quality control

Future modules may include:

* Existing-site entity audits
* Google Search Console integration
* CMS integrations
* Automated brief dashboards
* Entity graph visualization
* Performance monitoring
* Content refresh recommendations
* Log-based crawl intelligence

Contributing

Contributions should preserve the following rules:

* Keep outputs structured and schema-valid
* Add tests for new logic
* Avoid hidden publishing behavior
* Document new configuration fields
* Preserve evidence and confidence fields
* Do not replace deterministic checks with opaque LLM decisions
* Maintain backward compatibility where practical

License

Add the appropriate license for your intended use before public distribution.

Disclaimer

This project supports SEO research, planning, and content production. It does not guarantee rankings, traffic, rich results, Knowledge Panels, or search visibility.

Search performance depends on technical quality, content usefulness, competition, authority, user experience, market conditions, and search engine systems.
