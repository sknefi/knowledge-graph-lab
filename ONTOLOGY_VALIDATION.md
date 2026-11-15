# Ontology Validation

Validated version: **1.0.0**, file [ontology.ttl](ontology.ttl).

## Results

**All checks performed passed.** HermiT found no inconsistency in the ontology and no unsatisfiable named class.

| Check | Result |
| --- | --- |
| Turtle loading with RDFLib | Successful: 97 schema triples. |
| Model size | 7 named classes and 10 domain properties: 5 object properties and 5 datatype properties. |
| Term documentation | Every named class and domain property has non-empty `rdfs:label` and `rdfs:comment` annotations. |
| English annotations | All `rdfs:label` and `rdfs:comment` values, including ontology metadata, are in English and tagged `@en`. |
| Annotation language regression | The updated validator correctly rejected the original Slovak annotations. |
| Domains and ranges | Every domain property has one domain definition and one range definition; checks of object and datatype property declarations passed. |
| Schema separation | The ontology contains no declared `owl:NamedIndividual` data objects. |
| Schema consistency | HermiT: consistent; all named classes are satisfiable. |
| Currently qualifying postings | With SQL in the candidate profile, only posting A qualifies in the example scenario. |
| Missing skills | The candidate is missing Python for posting B. |
| Course benefit | The Python course makes 1 additional posting accessible; the Python and Git course makes 2 additional postings accessible. |
| An already known skill in a course | The second course also includes SQL, which the candidate already knows; the result remains 2 additional postings. |
| An organization with both roles | HermiT inferred both `Company` and `CourseProvider` for one organization without a conflict. |
| Deliberately invalid scenario | HermiT correctly rejected an object belonging to both `Candidate` and `Skill`. |

The English translation preserves all non-annotation ontology triples: classes, properties, domains, ranges, hierarchy, disjointness, datatypes, and identifiers are unchanged. All eight competency question identifiers and checklist completion states are preserved. Internal file links were updated to the English filenames and checked.

## Environment and Reproduction

- Python 3.12.
- RDFLib 7.6.0.
- Owlready2 0.51 with its bundled HermiT reasoner.
- Java 21.0.2.

Python package versions are listed in [requirements-ontology.txt](requirements-ontology.txt). Reproduction instructions are in [the ontology design](02_ONTOLOGY_DESIGN.md#validation-and-next-steps). The [validate_ontology.py](validate_ontology.py) script creates example data and temporary RDF/XML files only during the checks; it does not modify project files. A failed check causes the script to exit with an error.

## Validation Boundaries

- The 97 triples constitute the **ontology**, rather than the required final data graph. Step 4 remains open.
- The small scenario verifies the model and the main recommendation rule. It is not the final set of eight SPARQL queries; step 5 remains open.
- These checks cover logical consistency and selected model behavior. Required values, value counts, non-negative prices, and positive durations will be addressed by SHACL in step 6.
- Research and decisions about reusing external vocabularies belong to the open step 3.
