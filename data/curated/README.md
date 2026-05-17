# Curated data

## e1020_table_vi_v0.csv

Manual curation of Table VI from Yamanaka et al. 1991.

Table VI reports cardiovascular profiles after intravenous administration in anesthetized dogs. The dataset is intended as the first machine-readable input for retrospective SAR and AI-rediscovery analysis.

## Curation principles

- Preserve the original compound IDs.
- Preserve right-censored ED50 values such as `>300` and `>1000` using:
  - `ed50_ug_per_kg`: numeric threshold value
  - `ed50_relation`: `>` for censored rows, `=` for exact rows
  - `ed50_censored`: `right` or `none`
- Use `iv_potency_class` only as a coarse Table VI potency label.
- Do not treat `iv_potency_class` as a clinical or therapeutic ranking.
