# Workbook Rules

Use this reference when editing an application tracker `.xlsx`.

## Structural Rules

- Keep the workbook as the practical application surface.
- Preserve existing sheet grouping conventions. If special company/group sheets exist, put matching companies only in their group sheets and remove them from the main sheet.
- Do not create duplicate rows for the same inventory ID.
- Keep hidden/sort helper columns consistent with the visible ID system.

## Link Rules

- Only web URLs should be Excel hyperlinks.
- Emails, WeChat IDs, phone numbers, and free-text contacts must remain plain text.
- Link display text can be short, such as `查看JD`, but the target must match the JD dictionary.
- After moving or deleting rows, rebuild or verify hyperlinks by inventory ID.
- Scan for orphan/dangling links in blank rows.

## Style Rules

New or moved rows must match the workbook's existing layout:

- same font family,
- same font size,
- same horizontal and vertical alignment,
- same wrap setting,
- same borders,
- same row height,
- same filter range,
- same freeze panes and column widths.

After setting a hyperlink, reset the visible cell font/alignment to the workbook standard. Excel/openpyxl default hyperlink styling can silently change a cell to Calibri 12 or remove centering.

## Submitted Fill Rule

Do not apply submitted/confirmed fill to new roles unless the user says the role was submitted. If the workbook uses light green for submitted roles, new rows must not inherit that fill.

## Validation Checklist

Before finalizing:

- total non-empty job rows matches expected inventory count,
- workbook IDs are unique,
- workbook ID set matches the JD dictionary and classification file,
- grouped company rows are not left in the main sheet,
- no non-web hyperlinks,
- no blank rows with hyperlinks,
- no new-row submitted fill,
- filters cover all populated rows,
- visible link cells use workbook font/size/alignment.
