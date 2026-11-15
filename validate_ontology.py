"""Check the ontology and a small, temporary scenario; does not edit project files."""

from pathlib import Path
from tempfile import TemporaryDirectory

from rdflib import Graph, Literal, Namespace, RDF, RDFS, OWL, XSD
from owlready2 import World, sync_reasoner, OwlReadyInconsistentOntologyError


BASE = Path(__file__).resolve().parent
ONTO = Namespace("https://example.org/it-learning/ontology#")
DATA = Namespace("https://example.org/it-learning/data/")

FIXTURE = """
@prefix : <https://example.org/it-learning/ontology#> .
@prefix data: <https://example.org/it-learning/data/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

data:candidate a :Candidate ; :name "Example candidate" ; :hasSkill data:sql .
data:sql a :Skill ; :name "SQL" .
data:python a :Skill ; :name "Python" .
data:git a :Skill ; :name "Git" .
data:organization a :Organization ; :name "Example organization" ;
    :website "https://example.org/organization"^^xsd:anyURI .
data:jobA a :JobPosting ; :name "A" ;
    :requiresSkill data:sql ; :offeredBy data:organization .
data:jobB a :JobPosting ; :name "B" ;
    :requiresSkill data:sql, data:python ; :offeredBy data:organization .
data:jobC a :JobPosting ; :name "C" ;
    :requiresSkill data:python, data:git ; :offeredBy data:organization .
data:coursePython a :Course ; :name "Python" ; :description "Python course" ;
    :teachesSkill data:python ; :providedBy data:organization ;
    :priceEUR "50.0"^^xsd:decimal ; :durationHours "10.0"^^xsd:decimal .
data:coursePythonGit a :Course ; :name "Python and Git" ;
    :teachesSkill data:sql, data:python, data:git ; :providedBy data:organization ;
    :priceEUR "100.0"^^xsd:decimal ; :durationHours "20.0"^^xsd:decimal .
"""

PREFIXES = """
PREFIX : <https://example.org/it-learning/ontology#>
PREFIX data: <https://example.org/it-learning/data/>
"""


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def reason(graph, path):
    graph.serialize(destination=path, format="xml")
    world = World()
    try:
        world.get_ontology(path.as_uri()).load()
        sync_reasoner(world, debug=0)
        unsatisfiable = [c for c in world.inconsistent_classes() if c.iri != str(OWL.Nothing)]
        require(not unsatisfiable, f"Unsatisfiable classes: {unsatisfiable}")
        return world
    except Exception:
        world.close()
        raise


def main():
    schema = Graph().parse(BASE / "ontology.ttl", format="turtle")
    classes = {s for s in schema.subjects(RDF.type, OWL.Class) if str(s).startswith(str(ONTO))}
    objects = set(schema.subjects(RDF.type, OWL.ObjectProperty))
    datatypes = set(schema.subjects(RDF.type, OWL.DatatypeProperty))
    properties = objects | datatypes
    require(5 <= len(classes) <= 15, "The number of named classes is outside the assignment limits.")
    require(10 <= len(properties) <= 30, "The number of properties is outside the assignment limits.")
    require(not (objects & datatypes), "A property is declared as both an object property and a datatype property.")
    documented_terms = classes | properties | set(schema.subjects(RDF.type, OWL.Ontology))
    for term in documented_terms:
        for annotation in (RDFS.label, RDFS.comment):
            values = list(schema.objects(term, annotation))
            require(values and all(isinstance(v, Literal) and str(v).strip() and v.language == "en"
                                   for v in values),
                    f"Missing or non-English annotation {annotation} on {term}.")
    for prop in properties:
        require(len(list(schema.objects(prop, RDFS.domain))) == 1, f"Ambiguous domain: {prop}")
        require(len(list(schema.objects(prop, RDFS.range))) == 1, f"Ambiguous range: {prop}")
        if prop in objects:
            require(schema.value(prop, RDFS.domain) in classes, f"Unknown domain: {prop}")
            require(schema.value(prop, RDFS.range) in classes, f"Unknown range: {prop}")
        else:
            require(schema.value(prop, RDFS.range) in {XSD.string, XSD.decimal, XSD.anyURI},
                    f"Unknown datatype: {prop}")
    require(not list(schema.subjects(RDF.type, OWL.NamedIndividual)), "The schema contains data individuals.")
    print(f"PASS Turtle: {len(schema)} triples, {len(classes)} classes, {len(properties)} properties.")
    print("PASS English annotations, domains, ranges, and schema/data separation.")

    fixture = Graph().parse(data=FIXTURE, format="turtle")
    declared = classes | properties
    for subject, predicate, obj in fixture:
        for term in (predicate, obj if predicate == RDF.type else None):
            if term is not None and str(term).startswith(str(ONTO)):
                require(term in declared, f"The scenario uses an undefined term: {term}")

    current = fixture.query(PREFIXES + """
        SELECT DISTINCT ?job WHERE {
          ?job a :JobPosting ; :requiresSkill ?anyRequirement .
          FILTER NOT EXISTS {
            ?job :requiresSkill ?missing .
            FILTER NOT EXISTS { data:candidate :hasSkill ?missing }
          }
        }
    """)
    require({r.job for r in current} == {DATA.jobA}, "Incorrect currently qualifying postings.")

    missing = fixture.query(PREFIXES + """
        SELECT ?skill WHERE {
          data:jobB :requiresSkill ?skill .
          FILTER NOT EXISTS { data:candidate :hasSkill ?skill }
        }
    """)
    require({r.skill for r in missing} == {DATA.python}, "Incorrect missing skill.")

    gains = fixture.query(PREFIXES + """
        SELECT ?course (COUNT(DISTINCT ?job) AS ?newCount) WHERE {
          ?course a :Course .
          ?job a :JobPosting .
          FILTER EXISTS {
            ?job :requiresSkill ?originallyMissing .
            FILTER NOT EXISTS { data:candidate :hasSkill ?originallyMissing }
          }
          FILTER NOT EXISTS {
            ?job :requiresSkill ?missing .
            FILTER NOT EXISTS { data:candidate :hasSkill ?missing }
            FILTER NOT EXISTS { ?course :teachesSkill ?missing }
          }
        } GROUP BY ?course
    """)
    require({r.course: int(r.newCount) for r in gains} ==
            {DATA.coursePython: 1, DATA.coursePythonGit: 2}, "Incorrect course benefit.")
    print("PASS scenario: only A initially qualifies; B requires Python; course benefits are 1 and 2 additional postings.")

    with TemporaryDirectory(prefix="it-ontology-check-") as temporary:
        temporary = Path(temporary)
        world = reason(schema, temporary / "schema.owl")
        world.close()
        print("PASS HermiT: the schema is consistent and its named classes are satisfiable.")

        world = reason(schema + fixture, temporary / "positive.owl")
        try:
            organization = world[str(DATA.organization)]
            types = {c.iri for c in organization.INDIRECT_is_a if hasattr(c, "iri")}
            require(str(ONTO.Company) in types and str(ONTO.CourseProvider) in types,
                    "Both organization roles could not be inferred.")
            require(str(ONTO.Organization) in types, "The organization superclass is missing.")
        finally:
            world.close()
        print("PASS HermiT: the example data is consistent; a company can also be a course provider.")

        conflicting = schema + fixture
        conflicting.add((DATA.conflict, RDF.type, ONTO.Candidate))
        conflicting.add((DATA.conflict, RDF.type, ONTO.Skill))
        try:
            world = reason(conflicting, temporary / "negative.owl")
        except OwlReadyInconsistentOntologyError:
            print("PASS negative scenario: HermiT detected the Candidate/Skill conflict.")
        else:
            world.close()
            raise RuntimeError("The reasoner did not detect the deliberate conflict between disjoint classes.")
    print("All checks passed.")


if __name__ == "__main__":
    main()
