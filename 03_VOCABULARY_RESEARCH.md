# 3. Existing Vocabularies

We checked three existing vocabularies to see which parts could be used in our project.

## What We Found

| Source | Useful parts | Our decision |
| --- | --- | --- |
| **Schema.org** | [Person](https://schema.org/Person), [JobPosting](https://schema.org/JobPosting), and [Course](https://schema.org/Course) describe similar objects. Its [skills](https://schema.org/skills) property covers both a person's skills and job requirements. | These are suitable alternatives. We keep our own terms so the project uses one consistent model with separate links for existing and required skills. |
| **[ESCO](https://esco.ec.europa.eu/en/use-esco)** | Standard names and identifiers for skills and occupations. | We keep a small set of local skill definitions. ESCO's [occupation profiles](https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/two-pillar-structure-esco) describe general roles; our requirements belong to individual job postings. |
| **[SKOS](https://www.w3.org/TR/skos-primer/)** | Tools for naming, grouping, and linking concepts. | We keep our simple `Skill` class because our questions do not need skill hierarchies or multilingual labels. |

## Final Decision

**Keep the current classes and properties in [ontology.ttl](ontology.ttl).**

Our main reasons are:

- `hasSkill`, `requiresSkill`, and `teachesSkill` clearly separate what a candidate knows, what a job requires, and what a course teaches.
- `priceEUR` and `durationHours` store values in fixed units for easy comparison.
- Keeping the same names throughout the model makes the data and queries easier to follow. This also applies to common properties such as `name` and `description`.

The trade-off is that other systems would need a translation between our terms and theirs. This comparison does not create those links automatically.
