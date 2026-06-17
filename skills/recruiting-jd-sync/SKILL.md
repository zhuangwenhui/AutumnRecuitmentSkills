---
name: recruiting-jd-sync
description: "Synchronize recruiting job collections, JD dictionaries, technical-stack classification files, resume-version mappings, and application tracker workbooks. Use when Codex needs to ingest jobs from recruiting sites or company portals, deduplicate job postings, assign D-style inventory IDs, classify roles by JD technical requirements and available resumes, update Markdown JD/classification files, repair or validate Excel/XLSX application trackers, normalize workbook formatting, rebuild hyperlinks, or prepare reusable recruiting workflows for internship, campus, or full-time job applications."
---

# Recruiting JD Sync

Use this skill to run a durable recruiting workflow:

1. collect job list entries and authoritative detail pages,
2. deduplicate against the current inventory,
3. store complete JD text in a dictionary file,
4. classify jobs by technical-stack depth and resume availability,
5. synchronize the application workbook,
6. validate counts, IDs, links, styles, and grouping rules.

## Core Contract

Maintain three artifact roles unless the user specifies another architecture:

- JD dictionary Markdown: complete original JD text, URL, source, city, salary, dates, and notes.
- Classification Markdown: technical categories, inventory IDs, resume-version mapping, and application judgment.
- Application workbook: practical tracker for application actions, source, URL/contact, recommended resume, and company/group sheets.

Use `入库编号` as the only formal cross-file key. Do not add or preserve a second `原编号` field unless the user explicitly requests a historical migration table.

## Workflow

1. **Preflight**
   - Inspect the live file tree before assuming filenames or folder structure.
   - If browser login state is needed, read `references/browser-preflight.md` before controlling the browser.
   - If an `.xlsx` workbook is involved, load workbook dependencies and plan a verification pass.

2. **Collect**
   - Treat list pages as indexes only. Use job detail pages as the authoritative JD source.
   - Extract URL, company, job title, city, salary, education, source, refresh/date information, and full JD body.
   - Do not refresh or reset an already opened user page unless the user explicitly asks.

3. **Deduplicate**
   - Read `references/dedupe-policy.md`.
   - Prefer strong URL/job-id dedupe, then company-title-city, then JD-body comparison.
   - For same-title roles with different links, compare detail text before deciding whether to keep both.

4. **Classify And Number**
   - Read `references/classification-policy.md`.
   - Classify from the actual JD technical requirements, not from fixed category names.
   - Use `D{category}-{sequence}` IDs. Category count is determined by JD clusters and available resume variants.
   - If resume count is lower than category count, preserve the categories and use resume placeholders unless the user asks to merge categories.

5. **Update Files**
   - Update the JD dictionary first.
   - Update the classification file second.
   - Update the workbook last, using grouped sheets for special companies when the workbook already has that convention.
   - In the workbook, only web URLs should be hyperlinks. Emails and WeChat IDs must remain plain text.

6. **Validate**
   - Run the scripts in `scripts/` where applicable.
   - Required checks: equal ID sets across files, no duplicate IDs, no stale `原编号`, no orphan links, no bad web-link targets, no unintended submitted fill on new rows, workbook style consistency.

## References

- Browser and permissions: `references/browser-preflight.md`
- Classification and resume mapping: `references/classification-policy.md`
- Workbook rules: `references/workbook-rules.md`
- Deduplication: `references/dedupe-policy.md`

## Scripts

- `scripts/validate_artifacts.py`: compare IDs and basic invariants across Markdown and workbook files.
- `scripts/scan_workbook.py`: report sheet counts, sources, styles, hyperlinks, group hits, and submitted-fill issues.
- `scripts/normalize_xlsx_style.py`: normalize workbook row style, filters, freeze panes, and optional orphan blank rows.
- `scripts/rebuild_xlsx_links.py`: rebuild workbook link-column hyperlinks from the JD dictionary by inventory ID.
- `scripts/extract_resume_variants.py`: inspect available resume PDFs and infer resume/category mapping state.

Prefer running scripts from the project/workspace directory and pass explicit paths when filenames differ.
