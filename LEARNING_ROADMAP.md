# Learning Roadmap

## Purpose

This project is both a retrospective computational study and a beginner-oriented learning project.

It uses the historical E-1020 SAR data as a concrete case study for learning:

- drug-discovery data curation
- basic pharmacology concepts
- structure-activity relationships (SAR)
- cheminformatics
- machine learning for small molecular datasets
- the limits of AI-assisted research

The goal is not to claim that AI has rediscovered E-1020. The goal is to learn how far a transparent, reproducible, AI-assisted workflow can go when reconstructing parts of a historical medicinal chemistry decision process.

## Guiding principle

Before doing AI drug discovery, first learn to question the data.

This project starts from a real historical paper rather than a clean benchmark dataset. That means the learning process includes ambiguity, manual curation, censored values, incomplete structure metadata, and cautious interpretation.

## Audience

This roadmap is intended for learners who may be new to medicinal chemistry, cheminformatics, or machine learning, but who want to understand how these fields connect in a concrete case study.

No claim is made that this roadmap provides professional training in drug discovery, medicinal chemistry, pharmacology, toxicology, or clinical development.

## Module 0 — Project position and research ethics

### Core question

What can an AI-assisted independent researcher learn from a historical SAR dataset?

### Learning objectives

- Understand the difference between a research project, a learning project, and a drug-discovery claim.
- Understand why this project is retrospective and computational.
- Understand why AI assistance must be disclosed.
- Understand why the original article PDF, scanned pages, screenshots, and publisher figures should not be redistributed.
- Understand why final responsibility remains with the human researcher.

### Project artifacts

- `README.md`
- `AI_USE.md`
- `NON_EXPERT_POSITION.md`
- `docs/source_papers.md`

### Key caution

AI can help draft, organize, and check work, but it cannot replace source verification or domain expertise.

## Module 1 — From paper table to curated dataset

### Core question

How do we turn a historical pharmacology table into a machine-readable dataset?

### Learning objectives

- Read a source table carefully.
- Separate source facts from curated fields and derived labels.
- Create a CSV dataset from manual curation.
- Track source table, compound ID, dose, pharmacological endpoints, and notes.
- Understand why manual data entry requires later verification.

### Project artifacts

- `data/curated/e1020_table_vi_v0.csv`
- `docs/data_dictionary.md`
- `docs/curation_notes.md`

### Key concepts

- curation
- provenance
- source table
- compound identifier
- data dictionary
- independent verification

### Suggested exercise

Pick five rows from Table VI and manually verify every curated value against the source paper.

## Module 2 — ED50, potency, and censored values

### Core question

What does an ED50 value tell us, and what does it not tell us?

### Learning objectives

- Understand ED50 as a potency-related measure.
- Understand the difference between exact and right-censored values such as `>300` or `>1000`.
- Understand why a low ED50 does not automatically mean a better drug candidate.
- Understand why the derived `iv_potency_class` is only a coarse IV inotropic potency label.

### Project artifacts

- `docs/data_dictionary.md`
- `notebooks/01_table_vi_exploration.ipynb`

### Key concepts

- ED50
- dose-response
- potency
- right censoring
- coarse labels
- label leakage risk

### Suggested exercise

Rank compounds by ED50, then mark which values are exact and which are right-censored. Discuss how the ranking changes when censored values are treated cautiously.

## Module 3 — Pharmacological profile beyond one number

### Core question

Why is one potency value not enough to explain candidate selection?

### Learning objectives

- Compare inotropic response with heart-rate and blood-pressure effects.
- Understand why a compound can be potent but still not ideal.
- Understand why historical candidate selection appears multi-objective.
- Learn to avoid reducing a medicinal chemistry decision to a single column.

### Project artifacts

- `data/curated/e1020_table_vi_v0.csv`
- `notebooks/01_table_vi_exploration.ipynb`

### Key concepts

- efficacy
- potency
- heart-rate effect
- blood-pressure effect
- therapeutic window
- multi-objective optimization

### Suggested exercise

Compare compounds with strong IV potency. Identify whether any show larger heart-rate or mean arterial pressure changes than 11a.

## Module 4 — SAR and activity cliffs

### Core question

How can small structural changes create large activity differences?

### Learning objectives

- Understand structure-activity relationship (SAR) reasoning.
- Understand why regioisomers can have different biological activity.
- Analyze the 11a versus 23 comparison as an activity-cliff case.
- Understand why similar molecules can behave differently.

### Project artifacts

- future structure metadata from Tables I, IV, and V
- future SMILES curation file
- future activity-cliff notebook

### Key concepts

- SAR
- regioisomer
- activity cliff
- molecular recognition
- structure comparison

### Suggested exercise

Write a short note explaining why 11a versus 23 is a stronger teaching example than a simple ED50 ranking.

## Module 5 — Oral activity, duration, and PK/PD entry points

### Core question

Why does route of administration and duration matter?

### Learning objectives

- Understand why IV potency is not the same as oral usefulness.
- Learn the basic idea of pharmacokinetics and pharmacodynamics.
- Understand why Table VIII should be curated before making stronger claims about historical selection logic.
- Learn why duration can matter as much as potency.

### Project artifacts

- future Table VIII curated dataset
- future oral-duration analysis notebook

### Key concepts

- oral administration
- IV administration
- duration
- PK/PD
- exposure
- onset and offset

### Suggested exercise

After Table VIII is curated, compare oral duration against IV ED50. Identify compounds that look strong by one endpoint but weaker by another.

## Module 6 — PDE inhibition and selectivity

### Core question

How does target selectivity change the interpretation of pharmacological data?

### Learning objectives

- Understand the role of phosphodiesterase inhibition in this historical project.
- Understand the meaning of IC50.
- Compare PDE I, PDE II, and PDE III inhibition.
- Understand why PDE III selectivity matters for interpretation.

### Project artifacts

- future Table IX curated dataset
- future PDE selectivity analysis notebook

### Key concepts

- IC50
- enzyme inhibition
- PDE I / PDE II / PDE III
- selectivity
- off-target concern

### Suggested exercise

After Table IX is curated, calculate simple selectivity ratios and discuss what they do and do not prove.

## Module 7 — Molecular representation and SMILES

### Core question

How do we represent chemical structures for computation?

### Learning objectives

- Understand SMILES as a text representation of molecular structure.
- Understand why salts, tautomers, protonation states, and hydrates require careful handling.
- Learn why compound 11a as a candidate/hydrochloride monohydrate requires explicit representation choices.
- Learn to validate molecules with RDKit.

### Project artifacts

- future SMILES curation file
- future RDKit validation notebook

### Key concepts

- SMILES
- canonicalization
- salt form
- hydrate
- tautomer
- molecule validation

### Suggested exercise

Create a curation table with columns for `compound_id`, `smiles`, `structure_source`, `salt_state`, `curation_status`, and `notes`.

## Module 8 — Fingerprints and molecular similarity

### Core question

How do we measure molecular similarity, and where does that measurement fail?

### Learning objectives

- Generate molecular fingerprints.
- Compute Tanimoto similarity.
- Compare similarity-based ranking with pharmacological activity.
- Understand why molecular similarity does not guarantee similar activity.

### Project artifacts

- future fingerprint notebook
- future similarity matrix
- future 11a versus 23 activity-cliff analysis

### Key concepts

- molecular fingerprint
- Tanimoto similarity
- nearest neighbor
- similarity-property principle
- exception cases

### Suggested exercise

Once SMILES are curated, find the nearest neighbors of 11a and ask whether they are also pharmacologically strong.

## Module 9 — Baseline machine learning with small data

### Core question

What can machine learning learn from a tiny, biased, historical SAR dataset?

### Learning objectives

- Build simple baseline models before using complex models.
- Understand train/test splitting limitations with small datasets.
- Understand overfitting and unstable metrics.
- Understand why model performance should be interpreted skeptically.
- Test whether E-1020 / 11a ranks highly when hidden from training.

### Project artifacts

- future baseline ML notebook
- future hold-out experiment notebook
- future model card or analysis report

### Key concepts

- QSAR
- baseline model
- classification
- regression
- cross-validation
- overfitting
- uncertainty

### Suggested exercise

Train a simple model using only Table VI labels. Then repeat with 11a hidden. Compare the result with a similarity-based baseline.

## Module 10 — Interpreting AI-assisted results

### Core question

What does it mean if a model ranks 11a highly, and what does it not mean?

### Learning objectives

- Distinguish reproduction, explanation, and prediction.
- Avoid claiming that AI rediscovered E-1020.
- Identify where the model agrees with historical logic.
- Identify where the model fails or over-simplifies the historical decision.
- Write cautious, reproducible conclusions.

### Project artifacts

- final analysis notebook
- final curation notes
- versioned dataset release
- possible preprint or teaching article

### Key concepts

- retrospective validation
- benchmark limitation
- interpretability
- reproducibility
- uncertainty statement

### Suggested exercise

Write two conclusions: one overclaimed and one cautious. Then explain why the cautious version is more scientifically defensible.

## Suggested learning order

1. Read `README.md`.
2. Read `NON_EXPERT_POSITION.md` and `AI_USE.md`.
3. Inspect `data/curated/e1020_table_vi_v0.csv`.
4. Read `docs/data_dictionary.md` and `docs/curation_notes.md`.
5. Run or inspect `notebooks/01_table_vi_exploration.ipynb`.
6. Verify selected rows against the source paper.
7. Curate Table VIII and Table IX.
8. Add structure metadata and SMILES.
9. Run similarity analysis.
10. Run baseline machine-learning experiments.

## Recommended repository milestones

### v0.1.0 — Table VI learning dataset

- Table VI CSV
- data dictionary
- curation notes
- ED50 ranking notebook
- AI-use disclosure
- non-expert position statement
- learning roadmap

### v0.2.0 — Multi-endpoint pharmacology learning dataset

- Table VIII curation
- Table IX curation
- basic multi-objective comparison

### v0.3.0 — Structure and cheminformatics module

- structure metadata
- curated SMILES
- RDKit validation
- fingerprints and Tanimoto similarity

### v0.4.0 — Activity-cliff module

- 11a versus 23 comparison
- nearest-neighbor analysis
- similarity/activity mismatch discussion

### v0.5.0 — Baseline AI rediscovery module

- simple ML baselines
- E-1020 / 11a hold-out experiment
- cautious interpretation report

## Final caution

This roadmap is for learning how to read, curate, and analyze drug-discovery data. It is not a guide to medical use, clinical decision-making, or experimental drug development.
