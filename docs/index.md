---
title: Amazon PPC Wiki
page_type: landing
version: 1.0.0
---

# The Amazon PPC Wiki

A beginner-friendly, operator-ready knowledge base for Amazon PPC training, agency operations, and future app integration.

This repo was generated from the expanded Amazon PPC Wiki manual and is designed to work as:

- a GitHub wiki-style documentation repo,
- a MkDocs static knowledge base,
- a training library for VAs and junior strategists,
- a structured data source for simulators, quizzes, and future tools.

## Start here by role

- **Beginner VA:** Start with Sections 1-4, then 5-11, then 22.
- **Junior Strategist:** Read Sections 1-11, then 14-15, 18, 22-23.
- **Senior Strategist:** Read the core sections, then 12-13, 17, 21, 25, and 32.
- **Brand Owner:** Read Sections 1, 3, 10, 14-15, 18, 20, and 23.
- **Agency Owner:** Read Sections 2, 10-11, 16-17, 22-23, 26-27, and 32.

## Repo map

- `docs/sections/` - all wiki pages as Markdown.
- `docs/glossary/` - A-Z PPC terms and acronyms.
- `docs/appendix/` - formulas, calculators, and reference material.
- `docs/training/` - learning aids, quiz model, teaching guide model, handout model.
- `docs/app-layer/` - content-as-data and simulator integration notes.
- `data/` - machine-readable page index, glossary, formulas, quizzes, scenarios, and prerequisite graph.
- `schemas/` - JSON Schemas for app-facing content.
- `templates/` - reusable wiki page, changelog, quiz, and scenario templates.
- `scripts/` - validation and export helpers.

## Naming convention

Every page should keep these fields in YAML frontmatter:

``​`yaml
page_id: "1-1"
title: "What is Amazon PPC"
learner_level: "Foundational"
topic_tags: ["amazon-ppc", "foundations"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
``​`

## Local preview

``​`bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
``​`

Open the local URL MkDocs prints in your terminal.
