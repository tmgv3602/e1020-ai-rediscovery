# E-1020 AI Rediscovery

**Can modern AI rediscover E-1020 from historical SAR data?**

This repository is an open, work-in-progress research project that revisits the discovery of **E-1020**, also known in early literature as **loprinone** and later standardized as **olprinone hydrochloride**, using modern cheminformatics and AI methods.

The project starts from the 1991 paper by **Yamanaka, Miyake, Suda, Ohhara, and Ogawa** on imidazo[1,2-a]pyridines and their inotropic activity. The first curated dataset in this repository is based on **Table VI**, which reports cardiovascular profiles after intravenous administration in anesthetized dogs.

The central question is not whether AI can replace medicinal chemists. The more interesting question is:

> Where do modern computational methods reproduce, explain, or fail to reproduce the discovery logic behind E-1020?

## Status

**Work in progress.**

Current stage:

- Source paper identified
- Table VI manually curated into CSV
- ED50 censoring and coarse IV potency labels added
- Initial repository structure prepared
- Predictive modeling not yet performed
- SMILES curation not yet complete
- Table VIII and Table IX not yet curated

This repository should be read as a transparent research notebook, not as a finished result.

## Motivation

E-1020 was selected as a candidate compound after medicinal chemistry, pharmacology, and toxicology evaluation. A simple ranking by IV ED50 alone does not fully explain the historical selection of E-1020.

That makes this a useful retrospective benchmark:

- Can modern cheminformatics recover the same candidate from historical SAR data?
- Does an ED50-based model select E-1020, or does it prefer other potent analogs?
- Can modern methods explain the activity cliff between closely related isomers?
- Where do AI models fail compared with human medicinal chemistry judgment?

The goal is to study the historical discovery process carefully, not to overclaim that AI has “rediscovered” E-1020.

## Primary source

Yamanaka M, Miyake K, Suda S, Ohhara H, Ogawa T.  
**Imidazo[1,2-a]pyridines. I. Synthesis and inotropic activity of new 5-imidazo[1,2-a]pyridinyl-2(1H)-pyridinone derivatives.**  
*Chemical and Pharmaceutical Bulletin.* 1991;39(6):1556–1567.  
DOI: `10.1248/cpb.39.1556`

## Data and copyright note

This repository does **not** redistribute the original article PDF, scanned pages, article screenshots, or figures from the source publication.

The CSV files in this repository are manually prepared derivative datasets for historical and computational analysis. Users should cite the original paper when using these data.

## Dataset v0.1

The first curated dataset is:

```text
data/curated/e1020_table_vi_v0.csv
```

It contains a manual curation of Table VI from the 1991 paper.

Table VI reports cardiovascular profiles after intravenous administration in anesthetized dogs, including:

- compound ID
- dose
- percent change in LVDp/dtmax
- percent change in heart rate
- percent change in mean arterial pressure
- ED50
- ED50 censoring information
- coarse IV potency class

## ED50 censoring

Some ED50 values are reported as thresholds, such as `>300` or `>1000`. These are treated as right-censored values.

The dataset separates the numeric threshold from the relation:

| Original value | `ed50_ug_per_kg` | `ed50_relation` | `ed50_censored` |
|---|---:|---|---|
| `23 ± 2` | `23` | `=` | `none` |
| `>300` | `300` | `>` | `right` |
| `>1000` | `1000` | `>` | `right` |

## IV potency class

The column `iv_potency_class` is a coarse derived label from Table VI ED50 values.

| Rule | Class |
|---|---|
| ED50 <= 30 μg/kg | `strong` |
| 30 < ED50 <= 100 μg/kg | `moderate` |
| ED50 > 100 μg/kg | `weak` |
| Right-censored ED50 such as `>300` or `>1000` | `weak` |

Important: `iv_potency_class` is **not** a claim of overall drug-likeness, clinical value, safety, or therapeutic superiority. It is only a rough label for IV inotropic potency in Table VI.

## Why Table VI is only the starting point

Table VI is useful because it gives a compact pharmacological ranking. But E-1020 was not necessarily selected because it had the lowest ED50 in Table VI.

The historical selection appears to be multi-objective, involving factors such as:

- IV inotropic potency
- heart-rate effect
- blood-pressure effect
- oral duration
- PDE III selectivity
- safety and toxicology considerations
- medicinal chemistry feasibility

Therefore, future versions of this repository should also curate:

```text
Table VIII: oral duration data
Table IX: PDE I / II / III inhibition data
Tables I, IV, V: structure and analog metadata
```

## Planned analyses

1. Verify Table VI dataset against the source paper
2. Generate ED50 rankings
3. Compare E-1020 / 11a with milrinone
4. Analyze the 11a versus 23 activity cliff
5. Curate Table VIII oral-duration data
6. Curate Table IX PDE inhibition data
7. Add compound structure metadata from Tables I, IV, and V
8. Curate SMILES for E-1020, key analogs, and reference compounds
9. Run RDKit fingerprint and Tanimoto similarity analyses
10. Perform retrospective hold-out experiments: can baseline models rank E-1020 highly when it is hidden?

## Repository structure

```text
e1020-ai-rediscovery/
  README.md
  CITATION.cff
  LICENSE
  data/
    raw/
      README.md
    curated/
      e1020_table_vi_v0.csv
      README.md
  docs/
    source_papers.md
    data_dictionary.md
    curation_notes.md
  notebooks/
    01_table_vi_exploration.ipynb
  src/
    e1020/
  tests/
```

## Suggested milestones

### v0.1.0 — Historical Table VI Dataset

- Table VI CSV
- Data dictionary
- Curation notes
- Basic ED50 ranking notebook

### v0.2.0 — Multi-objective Pharmacology Dataset

- Add Table VIII
- Add Table IX
- Start comparing potency, duration, and PDE selectivity

### v0.3.0 — Structure Metadata and SMILES

- Add structure metadata from Tables I, IV, and V
- Curate SMILES
- Validate molecules with RDKit

### v0.4.0 — Similarity and Activity-Cliff Analysis

- Compute molecular fingerprints
- Calculate Tanimoto similarity
- Analyze 11a versus 23

### v0.5.0 — Retrospective AI Rediscovery Baseline

- Hide E-1020 / 11a
- Train simple baseline models
- Test whether E-1020 ranks highly
- Compare classical ML and similarity-based methods

## What this project is not

This project is not:

- medical advice
- a therapeutic recommendation
- a claim that E-1020 should be used clinically in any context
- a claim that AI has already rediscovered E-1020
- a drug development program
- a replacement for experimental medicinal chemistry

## Citation

If you use this repository or dataset, please cite both:

1. This repository or its Zenodo DOI, once available
2. The original 1991 paper by Yamanaka et al.

See [`CITATION.cff`](CITATION.cff) for citation metadata.

## License

Code in this repository is released under the MIT License unless otherwise noted.

Curated data are provided for historical and computational research use with source attribution. Please cite the original paper when using the dataset.

## Acknowledgment

This project is motivated by the historical discovery of E-1020 and by the broader question of how modern AI methods can help us understand, reproduce, or challenge past medicinal chemistry decisions.
