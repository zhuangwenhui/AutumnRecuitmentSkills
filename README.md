# AutumnRecuitmentSkills

Reusable Codex skills for autumn recruiting workflows.

## Skills

- `skills/recruiting-jd-sync`: collects recruiting jobs, deduplicates JD entries, classifies roles by technical stack and resume availability, and synchronizes JD Markdown, classification Markdown, and XLSX application trackers.

## Current Scope

This repository currently contains one production-oriented skill:

- dynamic D-style inventory IDs based on JD clusters and available resume variants
- browser preflight guidance for logged-in recruiting sites
- workbook validation, style normalization, and hyperlink repair scripts
- deduplication and group-sheet rules for application trackers

## Install Locally

Copy a skill directory into `~/.codex/skills/`:

```bash
mkdir -p ~/.codex/skills
cp -R skills/recruiting-jd-sync ~/.codex/skills/
```
