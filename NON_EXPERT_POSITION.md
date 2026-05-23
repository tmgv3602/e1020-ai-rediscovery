# Non-Expert Position Statement

## Purpose of this document

This project is led by an independent researcher who is not formally trained as a medicinal chemist, pharmacologist, toxicologist, or drug-discovery scientist.

That limitation is not hidden. It is central to the project.

The project asks whether a non-domain expert, using AI assistance, public literature, transparent data curation, and reproducible computational workflows, can learn from and partially reconstruct a historical drug-discovery decision process.

## What this project is

This project is:

- an independent research and learning project
- a retrospective computational study
- a historical SAR data-curation exercise
- an AI-assisted cheminformatics and machine-learning case study
- a beginner-oriented teaching resource for drug-discovery data science
- an experiment in transparent non-expert participation in research-adjacent work

## What this project is not

This project is not:

- professional medicinal chemistry judgment
- a drug-discovery program
- a therapeutic recommendation
- medical advice
- clinical guidance
- a safety or toxicology assessment
- a claim that E-1020 should be used clinically
- a claim that AI has rediscovered E-1020
- a replacement for domain experts or experimental validation

## Why the non-expert position matters

Drug-discovery knowledge is often locked inside specialized papers, expert workflows, proprietary datasets, and tacit domain judgment.

This project explores whether AI-assisted independent researchers can help make parts of that knowledge more learnable, reusable, and reviewable through:

- careful source tracking
- transparent curation notes
- small derivative datasets
- reproducible notebooks
- explicit uncertainty labels
- open issue lists
- cautious interpretation

The value is not that a non-expert can replace experts. The value is that non-experts may be able to participate more responsibly in early-stage computational learning, historical reanalysis, and data preparation.

## Central learning question

The central learning question is:

> How far can a non-domain expert go, with AI support and public sources, before expert medicinal chemistry judgment becomes essential?

That boundary is part of the research object.

## Guardrails

The project follows these guardrails:

1. Do not claim automated rediscovery.
2. Do not claim clinical superiority, safety, or therapeutic value from ED50 labels.
3. Do not treat a low ED50 value as sufficient evidence of candidate quality.
4. Do not hide AI assistance.
5. Do not hide non-expert status.
6. Do not redistribute the original article PDF, scanned pages, screenshots, or publisher figures.
7. Separate source facts, curated data, derived labels, interpretations, and hypotheses.
8. Mark uncertain entries clearly.
9. Prefer small reproducible steps over broad claims.
10. Invite expert correction.

## Interpretation stance

This project treats historical E-1020 selection as a multi-objective medicinal chemistry decision, not a simple ED50 ranking problem.

Relevant factors may include:

- IV inotropic potency
- heart-rate effect
- blood-pressure effect
- oral duration
- PDE III selectivity
- safety and toxicology considerations
- synthetic feasibility
- historical context

A non-expert project can explore these factors, but should not pretend to fully reproduce the original expert judgment.

## Curation stance

The project should mark data by confidence and review status.

Suggested statuses include:

| Status | Meaning |
|---|---|
| `raw_transcribed` | Entered from source but not yet checked. |
| `manual_checked` | Checked against source by the project maintainer. |
| `double_checked` | Checked in a second pass or by another reviewer. |
| `needs_review` | Ambiguous or uncertain. |
| `expert_review_needed` | Requires review by a domain expert. |
| `derived` | Computed or assigned from curated data. |

For chemical structures and SMILES, `expert_review_needed` should be used liberally until a reliable verification workflow is in place.

## Educational stance

This project can be useful as an introductory learning resource because it exposes real-world messiness:

- historical tables are not ready-made ML datasets
- pharmacological endpoints require interpretation
- censored values complicate modeling
- chemical structures require careful normalization
- activity labels can overstate what the data prove
- small datasets make machine learning fragile
- AI assistance can speed up work but also amplify mistakes

That messiness is not a defect. It is the lesson.

## How experts are invited to contribute

Domain experts are welcome to challenge and improve:

- compound identity assignments
- structure metadata
- SMILES curation
- pharmacological interpretation
- SAR explanations
- PDE selectivity interpretation
- modeling assumptions
- educational framing

Corrections should be treated as improvements, not as failures.

## Suggested public positioning

A concise public description is:

> This is an AI-assisted independent research and learning project by a non-domain expert. It uses historical E-1020 SAR data to learn how drug-discovery data can be curated, analyzed, and interpreted with modern cheminformatics and machine-learning workflows. The project emphasizes provenance, uncertainty, reproducibility, and expert-review needs rather than claiming automated drug rediscovery.

## Bottom line

The non-expert position is not a license to make weaker claims.

It is a reason to make claims more carefully, document decisions more transparently, and design the project so that others can inspect, reproduce, and correct it.
