# ED50 Ranking Notes

## Purpose

This note summarizes the first interpretation of the curated Table VI ED50 values from the E-1020 AI Rediscovery project.

The goal is not to claim that ED50 ranking explains the discovery of E-1020. The goal is narrower:

- separate exact ED50 values from right-censored ED50 values;
- generate a transparent first-pass potency ranking;
- highlight key compounds for later analysis;
- explain why ED50 alone is insufficient for reconstructing the historical compound-selection logic.

This note should be read together with:

- `data/curated/e1020_table_vi_v0.csv`
- `notebooks/01_table_vi_ed50_ranking.ipynb`
- `docs/data_dictionary.md`
- `docs/curation_notes.md`

## Input dataset

The input dataset is the curated Table VI dataset:

```text
data/curated/e1020_table_vi_v0.csv
```

The relevant ED50 fields are:

| Column | Meaning |
|---|---|
| `ed50_ug_per_kg` | Numeric ED50 value or censoring threshold in μg/kg |
| `ed50_relation` | `=` for exact ED50, `>` for right-censored ED50 |
| `ed50_censored` | `none` for exact ED50, `right` for right-censored ED50 |
| `iv_potency_class` | Coarse derived IV potency label from Table VI ED50 |

## Exact versus right-censored ED50

Table VI includes two different types of ED50 values.

| Type | Example | Interpretation | Ranking treatment |
|---|---|---|---|
| Exact ED50 | `23` | ED50 was reported as an estimated value | Can be sorted directly |
| Right-censored ED50 | `>300`, `>1000` | ED50 is greater than the reported threshold | Should not be treated as an exact value |

A value such as `>300` does **not** mean ED50 equals 300 μg/kg. It means the ED50 is greater than 300 μg/kg. The numeric field stores the threshold value, but the relation field preserves the inequality.

## Exact ED50 ranking

The exact ED50 rows can be ranked directly by `ed50_ug_per_kg`.

| Rank | Compound | ED50 μg/kg | IV potency class | Note |
|---:|---|---:|---|---|
| 1 | 3u | 11 | strong | Lowest exact ED50 in the current curated Table VI dataset |
| 2 | 11b | 18 | strong | Exact ED50 lower than 11a |
| 3 | 11a | 23 | strong | E-1020 candidate / hydrochloride monohydrate |
| 4 | Milrinone | 25 | strong | Reference drug |
| 5 | 3q | 27 | strong | Strong by the current derived threshold rule |
| 6 | 3e | 31 | moderate | Near the strong/moderate boundary |
| 7 | 3g | 32 | moderate | Near the strong/moderate boundary |
| 8 | 3n | 33 | moderate | Near the strong/moderate boundary |
| 9 | 3a | 52 | moderate | Moderate by the current derived threshold rule |
| 10 | 11f | 52 | moderate | Same numeric ED50 as 3a |
| 11 | 3f | 58 | moderate | Moderate by the current derived threshold rule |
| 12 | 13 | 87 | moderate | Moderate by the current derived threshold rule |
| 13 | 3t | 91 | moderate | Moderate by the current derived threshold rule |
| 14 | 3k | 123 | weak | Exact ED50 above 100 μg/kg |
| 15 | 12 | 172 | weak | Exact ED50 above 100 μg/kg |
| 16 | 3o | 177 | weak | Exact ED50 above 100 μg/kg |
| 17 | 3p | 193 | weak | Exact ED50 above 100 μg/kg |
| 18 | 3m | 195 | weak | Exact ED50 above 100 μg/kg |
| 19 | 11g | 197 | weak | Exact ED50 above 100 μg/kg |
| 20 | 11d | 218 | weak | Exact ED50 above 100 μg/kg |

## Right-censored ED50 rows

The right-censored rows should be listed separately rather than mixed into the exact ED50 ranking as if their threshold values were exact measurements.

| Censoring threshold | Compounds | Interpretation |
|---:|---|---|
| `>300` | 3b, 3c, 3d, 3h, 3i, 3j, 3l, 3r, 3s, 11c, 32a | ED50 is greater than 300 μg/kg |
| `>1000` | 11e, 18, 23, 32b | ED50 is greater than 1000 μg/kg |

For these rows, `ed50_ug_per_kg` stores the threshold value, but `ed50_relation` and `ed50_censored` must be used to preserve the censoring information.

## Key observations

### 1. E-1020 / 11a is strong, but not the lowest exact ED50 compound

Compound 11a has an exact ED50 of 23 μg/kg and is classified as `strong` by the current IV potency rule.

However, 11a is not the lowest exact ED50 compound in the current curated dataset. Compounds 3u and 11b have lower exact ED50 values.

This is important because it supports the core caution of the project: E-1020 should not be explained as a compound selected simply because it had the lowest Table VI ED50 value.

### 2. Milrinone is close to 11a by exact ED50

Milrinone has an exact ED50 of 25 μg/kg, close to 11a at 23 μg/kg.

This makes the 11a versus milrinone comparison useful for later teaching and interpretation. However, ED50 alone should not be used to claim overall superiority. Heart-rate effects, blood-pressure effects, oral duration, PDE selectivity, safety, and other factors are outside this ranking.

### 3. Compound 23 is a key weak comparator

Compound 23 is right-censored with ED50 reported as `>1000` μg/kg.

Compared with 11a at 23 μg/kg, this suggests that 11a is at least about 43-fold more potent than compound 23 by the Table VI IV ED50 metric:

```text
1000 / 23 ≈ 43.5
```

Because compound 23 is a 7-yl isomer and a weak comparator, it should be treated as a central compound for the later 11a versus 23 activity-cliff analysis.

This fold-difference should be interpreted cautiously because the ED50 value for 23 is right-censored. The true ED50 for 23 may be higher than 1000 μg/kg.

### 4. Right-censored values are informative, but not exact

Right-censored ED50 values are not missing data. They contain useful inequality information.

For example:

```text
>300 means ED50 is greater than 300 μg/kg
>1000 means ED50 is greater than 1000 μg/kg
```

But they should not be treated as exact values in ordinary ranking or fold-change calculations.

## Teaching interpretation

This ED50 ranking exercise is useful as an entry point for AI-assisted drug-discovery data science because it shows that the first hard problem is not machine learning. The first hard problem is deciding what the data actually mean.

Important teaching points:

1. **Potency ranking is not discovery logic.**  
   ED50 ranking is useful, but it does not reconstruct the full medicinal-chemistry decision process.

2. **Censored values require explicit handling.**  
   Treating `>300` or `>1000` as exact numeric values would create misleading rankings.

3. **Derived labels are limited.**  
   `iv_potency_class` is a coarse label for Table VI IV inotropic potency only. It is not a claim of drug-likeness, clinical value, safety, or therapeutic superiority.

4. **E-1020 selection appears multi-objective.**  
   Since 11a is not the lowest exact ED50 compound, later analysis should examine additional factors such as heart-rate effect, blood-pressure effect, oral duration, PDE III selectivity, medicinal-chemistry feasibility, and safety/toxicology context.

## What this note does not claim

This note does not claim that:

- AI rediscovered E-1020;
- ED50 ranking explains the historical selection of E-1020;
- 11a is clinically superior to milrinone;
- Table VI IV potency is sufficient to evaluate drug-likeness;
- right-censored thresholds are exact ED50 values;
- the current dataset is sufficient for predictive modeling.

## Next steps

Recommended next steps:

1. Compare 11a, milrinone, and 23 across Table VI pharmacological fields.
2. Create a focused note or notebook on the 11a versus 23 activity-cliff question.
3. Curate Table VIII oral-duration data.
4. Curate Table IX PDE inhibition data.
5. Add structure metadata and SMILES only after careful source checking.
6. Delay RDKit and baseline machine-learning experiments until structure data are curated and validated.

## Summary

The ED50 ranking confirms that 11a is a strong compound by Table VI IV potency, but it also shows why ED50 ranking alone is not enough. The most useful result is not a simple ranking. The useful result is a disciplined interpretation workflow:

```text
source table -> curated values -> censoring-aware ranking -> cautious interpretation -> next biological and chemical questions
```

That workflow is the real educational value of this phase.
