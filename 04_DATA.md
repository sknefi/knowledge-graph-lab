# 4. Data and Knowledge Graph

## Source

[data.ttl](data.ttl) contains **358 RDF triples describing 58 objects**, generated with LLM assistance using [our ontology](ontology.ttl).

All people, organizations, postings, courses, prices, and web addresses are fictional.

## Contents

| Type | Count |
| --- | --- |
| Candidates | 3 |
| Skills | 20 |
| Job postings | 20 |
| Courses | 8 |
| Organizations | 7: 5 companies and 3 course providers, with one organization in both roles |

The postings cover development, testing, systems administration, cloud, security, and analytics. QualityBridge Labs is both an employer and a course provider.

## Data Rules

- Skill identifiers are shared across candidates, postings, and courses.
- Listed job skills are mandatory and have no proficiency levels.
- Course prices are in EUR; durations are in hours.
- Each posting has one employer, and each course has one provider.
- The data includes a free course, courses with no benefit for some candidates, and postings that no single course can make accessible.

## Example

Alex Morgan has SQL, Git, HTML, and CSS. Alex already meets the skill requirements of `job-01` and `job-05`.

Python Backend Development teaches Python and REST APIs. It makes **three additional postings** accessible: `job-02`, `job-04`, and `job-20`. The two previously qualifying postings are not counted again.

The data uses all **7 classes and 10 properties** and is logically consistent with the ontology.
