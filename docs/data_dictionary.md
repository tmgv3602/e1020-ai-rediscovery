# Data dictionary

## `data/curated/e1020_table_vi_v0.csv`

| Column | Description |
|---|---|
| `compound_id` | Compound identifier as reported in the source table, e.g., 11a, 23, Milrinone. |
| `source_table` | Source table in the 1991 paper. |
| `number_of_experiments` | Curated field from the source table or curation notes. |
| `dose_mg_per_kg` | Intravenous dose in mg/kg used for the cardiovascular profile. |
| `lv_dpdt_pct_change` | Percent change in LVDp/dtmax from control. |
| `hr_pct_change` | Percent change in heart rate from control. |
| `map_pct_change` | Percent change in mean arterial pressure from control. |
| `ed50_ug_per_kg` | ED50 in μg/kg. For censored rows, this stores the threshold value. |
| `ed50_relation` | `=` for exact values, `>` for right-censored values reported as greater than a threshold. |
| `ed50_error` | Reported error term when available. |
| `notes` | Curated field from the source table or curation notes. |
| `ed50_censored` | `none` for exact ED50, `right` for right-censored ED50. |
| `active_class` | Alias of iv_potency_class retained for compatibility; prefer iv_potency_class. |
| `iv_potency_class` | Coarse derived label from Table VI ED50: strong, moderate, or weak. |
| `curation_status` | Curation status for the row. Typical values are `needs_review`, `manual_checked`, and `ambiguous`. This status mainly refers to source-table verification of the original Table VI values. |
| `curation_note` | Free-text note describing source verification, uncertainty, or derived-value handling. |
## Derived-label rule

`iv_potency_class` is derived as follows:

| Rule | Label |
|---|---|
| `ed50_relation = "="` and `ed50_ug_per_kg <= 30` | `strong` |
| `ed50_relation = "="` and `30 < ed50_ug_per_kg <= 100` | `moderate` |
| `ed50_relation = "="` and `ed50_ug_per_kg > 100` | `weak` |
| `ed50_relation = ">"` | `weak` |

This label is only a coarse IV potency label. It is not a claim of overall drug-likeness, clinical value, or safety.
