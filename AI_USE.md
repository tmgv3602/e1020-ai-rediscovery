# AI Use Disclosure

## Purpose of this document

This project is explicitly AI-assisted.

The purpose of this document is to describe how AI tools are used, what they are not used for, and how the project maintains human responsibility, source verification, and reproducibility.

## Project position

This is an AI-assisted independent research and learning project about historical E-1020 SAR data.

AI tools are used as research assistants. They are not treated as authors, inventors, domain experts, or final authorities.

All final responsibility for curation decisions, analysis, interpretation, repository content, and public claims remains with the human project maintainer.

## Suggested disclosure statement

A short disclosure suitable for the README, release notes, or related outputs is:

> This project was conducted as an independent research and learning project. ChatGPT/OpenAI was used as an AI research assistant for brainstorming, drafting, code assistance, data-curation support, and review suggestions. All source checks, curated data, analyses, interpretations, and final responsibility remain with the human project maintainer.

## How AI is used

AI assistance may be used for:

- brainstorming research questions
- outlining repository structure
- drafting README and documentation text
- suggesting data dictionary fields
- suggesting curation workflows
- identifying possible sources of ambiguity
- generating starter code or notebook scaffolds
- explaining medicinal chemistry, pharmacology, cheminformatics, and machine-learning concepts at an introductory level
- proposing validation checks and tests
- improving wording and clarity
- helping prepare educational material

## How AI is not used

AI assistance is not used as the sole authority for:

- source-paper transcription
- final compound identity assignment
- final chemical structure assignment
- final SMILES validation
- final pharmacological interpretation
- final medicinal chemistry conclusions
- clinical or therapeutic claims
- safety or toxicology conclusions
- claims that E-1020 has been rediscovered by AI

AI-generated content is treated as provisional until checked against primary sources, curated files, or executable code.

## Verification rules

The project should follow these rules whenever possible:

1. Source facts should be checked against the original paper, patent record, or other cited source.
2. Curated values should be traceable to a source table or source note.
3. Derived labels should be clearly separated from source facts.
4. AI-suggested interpretations should be labeled as interpretations, not source facts.
5. Ambiguous entries should be marked as `needs_review` or equivalent.
6. Chemical structures and SMILES should be validated with cheminformatics tools and, ideally, expert review.
7. Public claims should remain cautious and reproducible.

## Data-curation policy

The project distinguishes between:

| Category | Meaning |
|---|---|
| Source fact | Information directly reported in the source paper or patent record. |
| Curated data | Machine-readable data manually transcribed or normalized from source facts. |
| Derived label | A project-defined label computed or assigned from curated data. |
| Interpretation | A human or AI-assisted explanation based on source facts and curated data. |
| Hypothesis | A tentative claim to be tested, not a conclusion. |

Example: `iv_potency_class` is a derived label from Table VI ED50 values. It is not a claim of clinical value, drug-likeness, safety, or therapeutic superiority.

## Recommended curation-status values

When adding new curated data, consider using curation-status fields such as:

| Value | Meaning |
|---|---|
| `raw_transcribed` | Entered from the source but not yet independently checked. |
| `manual_checked` | Checked manually against the source. |
| `double_checked` | Checked independently or in a second pass. |
| `needs_review` | Requires review due to ambiguity or possible error. |
| `expert_review_needed` | Requires domain expert review. |
| `derived` | Computed from curated data rather than directly reported. |

## AI-generated code policy

AI-generated code should be treated as draft code.

Before relying on it:

- read it line by line
- run it locally
- add tests where possible
- check edge cases
- avoid hidden assumptions
- record package versions
- keep notebooks reproducible

For cheminformatics code, validate molecule parsing and standardization behavior explicitly.

## AI-generated text policy

AI-generated text should be edited for:

- factual accuracy
- cautious interpretation
- clear separation of facts and hypotheses
- avoidance of overclaiming
- appropriate citations
- consistency with project scope

The project should not use AI-generated text to imply professional medicinal chemistry judgment where none has been independently obtained.

## Publication policy

When publishing repository releases, datasets, notes, or teaching material:

- disclose AI assistance
- cite the original scientific sources
- do not redistribute the original article PDF, scanned pages, screenshots, or publisher figures
- release only original notes, curated derivative datasets, code, notebooks, documentation, and citation metadata
- state known limitations clearly
- invite correction and expert review

## Authorship and credit

AI tools should not be listed as authors.

A suitable acknowledgment is:

> AI tools were used to assist with drafting, organization, code suggestions, and review prompts. The human project maintainer is responsible for all final content and interpretations.

## Known risks

AI assistance can introduce risks, including:

- hallucinated references
- plausible but incorrect chemical reasoning
- transcription mistakes
- overconfident interpretation
- hidden assumptions in generated code
- oversimplification of drug-discovery decisions

This project treats those risks as part of the learning process and addresses them through transparent documentation, source checking, and cautious release practices.

## Bottom line

AI assistance is a feature of this project, not something to hide.

The standard is not AI-free work. The standard is transparent, checked, reproducible, and responsibly interpreted work.
