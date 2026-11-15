# Project Checklist

Checklist based on the updated semester project instructions for courses 4IZ444/4IZ441, intended for a **two-member team**. Additional recommendations are listed separately at the end.

## 1. Domain and Purpose

- [x] Describe the project domain: job postings, skills, and education in IT.
- [x] Define a particular use case.
- [x] Explain who will use the knowledge graph and what it will help them discover.
- [x] Create **5-10 competency questions** that the graph should answer.

Documentation: [Project domain and purpose](01_DOMAIN_AND_PURPOSE.md).

## 2. Ontology Design

- [x] Derive the model from the competency questions.
- [x] Define **5-15 classes**.
- [x] Define **10-30 properties**.
- [x] Include axioms or constraints, such as property domains and ranges or class hierarchies.
- [x] Add **`rdfs:label` and `rdfs:comment`** to every class and property.
- [x] Encode the ontology in **valid Turtle**.
- [x] Verify that the ontology contains no logical inconsistencies.
- [x] Create a **diagram of classes and properties**.
- [x] Explain the model in writing.

Documentation: [Ontology design](02_ONTOLOGY_DESIGN.md). Ontology: [ontology.ttl](ontology.ttl). Validation: [check results](ONTOLOGY_VALIDATION.md).

## 3. Research Existing Ontologies and Vocabularies

- [ ] Research existing terms that could be reused.
- [ ] Decide which terms to reuse and which to define ourselves.
- [ ] **Justify both choices**: reuse and custom definitions.

Schema.org and ESCO are possible sources to investigate for this domain.

## 4. Data and Knowledge Graph

- [ ] Create data using our ontology, either by generating it or transforming existing data.
- [ ] Reach an indicative size of **at least 50-100 RDF triples**. The instructions describe this as a rough estimate.
- [ ] Adequately cover **all defined classes and properties**.
- [ ] Prepare data suitable for meaningful analysis.

Generated data is allowed; the instructions explicitly permit using an LLM to generate it.

## 5. SPARQL Queries and Results

- [ ] Translate the competency questions into **SPARQL queries**.
- [ ] Execute the queries and obtain answers.
- [ ] Include more complex or analytical queries.
- [ ] If the competency questions do not cover these, add **three further analytical queries**, for example using aggregation, grouping, or string operations.
- [ ] Include **all queries, their descriptions, and explanations of the results** in the report.

## 6. SHACL Validation

- [ ] Create **3-4 SHACL shapes**.
- [ ] Include all shapes in the report and explain their meaning.

A single shape may contain several checks, such as a required course name and a non-negative price.

## 7. Written Report

- [ ] Produce the full project report as a **PDF**.
- [ ] Include the domain description and competency questions.
- [ ] Include the ontology description, diagram, and research into existing vocabularies.
- [ ] Describe how the data was created.
- [ ] Include the SPARQL queries and results.
- [ ] Include the SHACL shapes and explanations.

## 8. Submission and Organization

- [ ] Verify team registration in the list for the appropriate seminar. The deadline stated in the instructions was **24 October 2026**.
- [ ] Prepare **one ZIP file** containing:
  - the PDF report,
  - the ontology,
  - the data file,
  - SPARQL queries,
  - SHACL shapes.
- [ ] Assign one team member to submit the project through **InSIS** on behalf of the team.
- [ ] Submit by **4 December 2026 at 23:59**.

Project consultation sessions are scheduled for **30 November and 1 December**.

## 9. Presentation

- [ ] Prepare a presentation lasting **no more than 10 minutes**.
- [ ] Introduce the domain and motivation.
- [ ] Show the ontology's conceptual model.
- [ ] Demonstrate a use case with **one interesting SPARQL query and its results**.
- [ ] Evaluate collaboration and lessons learned.

Presentations take place in **teaching weeks 12 and 13**.

**Grading:** **35 points** for the project and **10 points** for the presentation. The instructions do not provide a more detailed breakdown of points by section.

## Additional Recommendations

These steps help verify the quality of the solution:

- [ ] First verify a small example with an expected answer calculated manually.
- [ ] Test SHACL on deliberately invalid data as well.
- [ ] Verify that recommendations count only additional postings, and count each posting once.
- [ ] Add instructions for loading the data, running queries, and performing validation.

**The instructions do not require a web application, a user interface, or live collection of job postings.**
