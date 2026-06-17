# Deduplication Policy

Deduplicate before assigning inventory IDs.

## Strong Duplicate Signals

Treat as duplicate unless the user requests otherwise:

- identical job detail URL,
- identical platform job ID in the URL,
- same company, same job title, same city, and substantially same JD text.

## Weak Duplicate Signals

Investigate before adding:

- same company and same normalized title, different URL,
- same title and same JD body, different work schedule or education,
- same company group or brand written with aliases,
- platform duplicate cards from collection pages.

## Keep Separate When

Keep two records separate when one of these differs materially:

- distinct official job IDs with different responsibilities,
- different hiring project or business unit,
- different city that affects application path,
- different source channel and the user needs both application routes,
- same title but materially different JD body.

## Normalization

Normalize only for comparison, not for stored text:

- trim whitespace,
- remove full-width/half-width spacing differences,
- lowercase Latin letters,
- remove bracket variants when comparing titles,
- map common company aliases where known.

Store the original official wording in the JD dictionary.

## Practical Rule

If unsure, compare the detail text. Do not add a role solely because a list page shows a different link.
