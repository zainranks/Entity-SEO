# Entity-First SEO Content Skill

Comprehensive skill package for planning and producing entity-led websites and content using Codex or Claude Code.

## Core outputs
- Entity inventory and canonical aliases
- Entity relationship graph
- Topic clusters and site architecture
- Page/section/mention decisions
- Search intent and cannibalization checks
- Content briefs, outlines, internal links, and schema recommendations
- QA reports with evidence and confidence scores

## Use
1. Copy `examples/project.example.yaml` to `project.yaml`.
2. Fill business, market, seed topics, competitors, and constraints.
3. Give the repository to Codex or Claude Code and ask it to follow `SKILL.md`.
4. Run `python -m entity_seo_skill.cli validate project.yaml`.
5. Run the phases in order; do not skip entity resolution or page-decision QA.

This package defaults to research and draft generation. It must not publish content automatically.
