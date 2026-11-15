# 1. Project Domain and Purpose

## Domain

The project covers job postings, skills, and education across IT. It includes areas such as software development, testing, analytics, systems administration, and cybersecurity.

The knowledge graph will connect candidates and their skills with job postings, employer requirements, and courses that teach specific skills. The domain also includes companies offering jobs and organizations providing courses.

## Target User

The target user is someone seeking to enter IT, advance their career, or change specialization. This may be a student, an entry-level candidate, or an experienced professional, such as a tester interested in test automation.

The project is not restricted to junior or data-related positions. A student can serve as the user in the demonstration scenario.

## Project Purpose

The goal is to help a candidate compare their skills with job requirements, identify missing skills, and select a course that would allow them to meet the skill requirements of additional job postings.

**Main project question:** Which course would allow a candidate to meet the requirements of the largest number of additional job postings, given their current skills?

Recommendations should be explainable: alongside the course, the results should identify the skills gained and the specific additional job postings whose skill requirements would then be covered.

## Use Case

1. Start with the candidate's recorded skills.
2. Compare them with the mandatory skills required by job postings.
3. Identify postings the candidate already qualifies for in terms of skills, and the skills missing for the remaining postings.
4. Evaluate how gaining the skills taught by each course would change the candidate's situation.
5. Compare courses by the number of additional qualifying postings and explain the results.

## Agreed Rules and Scope

- **No proficiency levels:** record specific skills, such as Python, SQL, or Git, without distinguishing beginner and advanced proficiency.
- **Mandatory skills:** evaluate the mandatory skills listed for each posting. The candidate meets a posting's skill requirements only when all listed mandatory skills are covered.
- **One course at a time:** evaluate each course independently against the candidate's original skills.
- **Successful completion:** when estimating a course's benefit, assume the candidate gains every skill the course teaches. These skills are added to their original skills.
- **Additional postings only:** exclude postings whose requirements were already covered before the course. Count each additional posting only once.
- **Main criterion:** recommend courses based on the number of additional postings whose mandatory skills would all be covered after the course.
- **Additional information:** record course price and duration for further comparisons; they do not change the main recommendation criterion.

Evaluation is based on the skills and requirements recorded in the dataset. A posting becoming "accessible" means that its recorded skill requirements are met; it does not guarantee employment.

## Illustrative Example

The candidate knows SQL. The course under consideration teaches Python.

| Posting | Mandatory skills | Before the course | After the course |
| --- | --- | --- | --- |
| A | SQL | Requirements met | Requirements met |
| B | SQL, Python | Requirements not met | Requirements met |
| C | Python, Git | Requirements not met | Requirements not met: Git is still missing |

**The course's benefit is one additional posting: B.** Posting A already qualified before the course, while posting C still has an uncovered mandatory skill.

## Competency Questions

| ID | Question |
| --- | --- |
| CQ1 | For which job postings does the candidate already meet all required skills? |
| CQ2 | Which skills is the candidate missing for a particular posting? |
| CQ3 | Which courses teach skills the candidate is missing for a selected posting? |
| CQ4 | Which course would allow the candidate to meet the requirements of the largest number of additional postings? |
| CQ5 | Which specific additional postings would become accessible to the candidate after taking a selected course? |
| CQ6 | Which skills are required by the largest number of job postings? |
| CQ7 | Which course has the lowest price per additional accessible posting? |
| CQ8 | On average, how many required skills is the candidate missing for postings from each company? |

**CQ4 is the main project question.** CQ2, CQ3, and CQ5 help explain the recommendation. CQ6-CQ8 provide analytical perspectives: frequency, the price-to-benefit ratio, and the average number of missing skills.

For CQ7, compare only courses that make at least one additional posting accessible to the candidate.
