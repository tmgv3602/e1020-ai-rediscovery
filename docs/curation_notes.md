# Curation notes

## Version 0.1.0

Initial curated file:

```text
data/curated/e1020_table_vi_v0.csv
```

Curation scope:

- Table VI only
- Cardiovascular profile after IV administration in anesthetized dogs
- ED50 represented with explicit relation and censoring fields

Known limitations:

- No SMILES yet
- No Table IV / V structure metadata yet
- No Table VIII oral-duration data yet
- No Table IX PDE IC50 data yet
- No independent double-entry verification yet

## Manual checks to perform before publishing a formal release

- Re-check every row against Table VI.
- Confirm compound IDs against the source paper.
- Confirm censored ED50 rows.
- Add `curation_status` if needed:
  - `manual_checked`
  - `needs_review`
  - `ambiguous`
  - `derived`
