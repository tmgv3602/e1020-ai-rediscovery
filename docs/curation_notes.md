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

## Table VI verification

Table VI was manually re-checked against the source paper.

Verification scope:

- compound IDs
- number of experiments
- dose values
- LVDp/dtmax percent changes
- heart-rate percent changes
- mean arterial pressure percent changes
- ED50 values
- ED50 relation symbols such as `>`
- right-censoring treatment for threshold ED50 values

Rows confirmed against the source table were marked as `manual_checked`.

Rows requiring further review, if any, remain marked as `needs_review` or `ambiguous`.
