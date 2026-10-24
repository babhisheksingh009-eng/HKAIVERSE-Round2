# CSE Curriculum Review and Redesign

## 1. Objective

This report evaluates curriculum alignment with practical software engineering, databases, operating systems, cloud computing, data science, and artificial intelligence.

The aim is to preserve essential computer-science foundations while proposing evidence-based improvements to practical learning, assessment, and industry readiness.

This is a student-led analysis. It is not an official IFHE curriculum revision.

## 2. Evidence Sources and Verification Status

The review uses the following project evidence:

1. Official IFHE/IcfaiTech B.Tech programme structure:
   https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure

2. Official IFHE/IcfaiTech syllabus archive:
   https://naac2020.ifheindia.org/1.1.3Syllabus%20IcfaiTech.html

3. A provisional course dataset:
   `data/curriculum.csv`

4. A separate reference extract from the published programme structure:
   `data/official_curriculum_reference.csv`

The reference extract contains 16 course entries with a combined listed-credit subtotal of 57. It is a partial extract, not the complete programme structure or the official total degree credits.

The exact applicability of the published structure to the 2023 admission batch has not been established. Course titles, semesters, credits, and equivalencies must therefore not be presented as verified requirements for that batch.

## 3. Preliminary Course Recommendations

The recommendations below are proposals based on course topics and potential practical-learning improvements. They must be checked against the applicable official syllabus before implementation.

| Subject or topic | Proposed decision | Reason |
|---|---|---|
| Computer Programming / C Programming | KEEP + UPDATE | Strengthen programming fundamentals through debugging and implementation exercises. Confirm the applicable official course title first. |
| Java Programming | UPDATE, if applicable | Include object-oriented application development and testing. |
| Python Programming | UPDATE, if applicable | Add data processing, API use, and automated testing exercises. |
| Object-Oriented Programming Concepts | KEEP | Preserve core software-design principles. |
| Data Structures | KEEP + UPDATE | Retain foundational structures and add practical problem-solving exercises. |
| Design and Analysis of Algorithms | KEEP | Preserve algorithm design, complexity analysis, and problem-solving. |
| Theory of Computation | KEEP | Retain theoretical computer-science foundations. |
| Computer Organization and Architecture | KEEP | Preserve processor and computer-system fundamentals. |
| Operating Systems | KEEP + UPDATE | Include Linux commands, process management, and troubleshooting labs. |
| Database Management System | KEEP + UPDATE | Strengthen SQL, database design, and secure data access. |
| Computer Networks | KEEP + UPDATE | Add networking diagnostics, HTTP, and API communication exercises. |
| Web Enabled Technologies | KEEP + UPDATE | Include secure API integration and practical web application development. |
| Software Engineering | KEEP + UPDATE | Introduce version control, code review, testing, and collaborative workflows. |
| Cloud Computing | KEEP + UPDATE | Include deployment, configuration, monitoring, and cloud-security fundamentals. |
| Artificial Intelligence | KEEP + UPDATE | Strengthen practical problem-solving and responsible AI evaluation. |
| Machine Learning | KEEP + UPDATE | Include data preparation, model evaluation, and error analysis. |
| Deep Learning | UPDATE, if applicable | Include practical model training, evaluation, and reproducibility. |
| Natural Language Processing | UPDATE, if applicable | Include language-processing applications and evaluation. |
| Human-Computer Interaction | UPDATE, if applicable | Add usability and accessibility testing. |
| Ethical Hacking | UPDATE, if applicable | Use authorized security laboratories and responsible disclosure exercises. |
| Introduction to Entrepreneurship | KEEP, if applicable | Retain innovation, business planning, and entrepreneurship fundamentals. |
| Overlapping introductory programming topics | REDUCE only if verified | Compare official course outcomes and remove unnecessary duplication only when evidence supports it. |
| Generative AI and LLM Applications | ADD only if justified | Consider prompt evaluation, retrieval-augmented generation, model assessment, and responsible AI if these outcomes are not adequately covered elsewhere. |
| Practical API Integration and Deployment | ADD or integrate into existing labs | First establish whether current courses already teach these skills. A separate course is not automatically necessary. |

The phrase "if applicable" indicates that a subject's presence and exact title in the 2023-batch curriculum remain to be confirmed.

## 4. Reasons Supporting the Recommendations

1. Programming exercises should include debugging, testing, and practical implementation.
2. Data structures and algorithms support problem-solving and coding assessments.
3. Operating-system labs provide experience with commands, processes, and troubleshooting.
4. SQL and database-design practice help students build reliable data-driven applications.
5. Networking exercises help students understand HTTP, APIs, and application communication.
6. Version control introduces collaborative development and change tracking.
7. Automated testing helps detect defects before deployment.
8. Cloud deployment provides practical experience with application hosting and configuration.
9. Machine-learning evaluation teaches students to assess model performance using appropriate metrics.
10. NLP and LLM exercises can develop skills in language-processing applications.
11. Accessibility and usability testing encourage more inclusive software design.
12. Comparing course outcomes can reveal duplicated content and help justify REDUCE proposals.

These are curriculum-design reasons, not proof that a particular employer requires every listed skill. Employer-specific claims must be supported by real job advertisements.

## 5. Official Curriculum Comparison

The project contains two datasets:

- `data/curriculum.csv`: 22 preliminary entries consisting of 20 proposed course entries and two provisional recommendations.
- `data/official_curriculum_reference.csv`: a partial extract containing 16 entries from the published IFHE/IcfaiTech programme structure.

The preliminary dataset lists 71 credits across its numeric-credit entries. The published reference extract lists 57 credits across the 16 entries included in that extract.

Neither number should be described as the official total degree credits.

The published reference includes examples such as:

- Computer Programming — Semester I
- Data Structures — Semester II
- Object Oriented Programming Concepts — Semester III
- Operating Systems — Semester III
- Database Management System — Semester IV
- Machine Learning — Semester V
- Cloud Computing — Semester VI

These examples are taken from the project's published-structure reference extract. They do not establish that the same course structure applies to the 2023 admission batch.

Before finalizing course equivalencies, compare the applicable official syllabus, course codes, learning outcomes, semester assignments, credits, prerequisites, and academic regulations.

## 6. Industry Skill-Gap Evidence

Industry alignment must be supported by at least three real job advertisements.

Potential sources already recorded in `sources/source_log.csv` include:

1. Amazon — Software Development Engineer Intern, May 2027:
   https://www.amazon.jobs/en/jobs/10513277/software-development-engineer-intern-may-2027-2-month-amazon-university-talent-acquisition

2. Amazon — Systems Development Engineer Intern, 2027:
   https://www.amazon.jobs/en/jobs/10498158/systems-development-engineer-intern-2027

3. Microsoft student careers page:
   https://careers.microsoft.com/v2/global/en/students?id=187

The Microsoft URL is a general student-careers page, not yet a verified specific job advertisement. It must not be counted as a confirmed third posting until a specific role and its requirements are documented.

For each confirmed advertisement, record:

- Employer and exact job title.
- Publication date, if stated.
- Location and job level.
- URL and actual access date.
- Required and preferred technical skills, distinguished clearly.
- Evidence connecting those skills to a course or learning outcome.
- A proposed curriculum response and the reason for it.

Do not invent posting dates or claim that an employer requires a skill unless the advertisement supports that claim.

## 7. Proposed Curriculum Redesign

The proposed improvements focus on practical learning:

- Programming and debugging laboratories.
- SQL, database design, and secure data-access exercises.
- Linux and operating-system troubleshooting.
- Git-based teamwork and code review.
- Automated testing and software-quality assessment.
- API integration and cloud deployment.
- Data preparation and model evaluation.
- Responsible AI and LLM application evaluation where justified by evidence.

These changes should preferably update existing laboratory work before adding new courses. A new course should be proposed only when the existing curriculum does not adequately cover the intended learning outcomes.

### Credit-balance calculation

The assignment requests changes affecting approximately 20–25% of programme credits.

The calculation must use the applicable official programme total:

Percentage affected = credits affected by the proposal / official programme credits × 100

The official total and the credits affected by the final proposal are not yet verified. Therefore, a final percentage cannot responsibly be reported at this stage.

The final redesign should state:

- Verified original programme credit total.
- Courses or modules changed.
- Credits affected, without double-counting courses.
- Revised credit total.
- Prerequisites and dependencies.
- Applicable academic and regulatory conditions.

Updating laboratory exercises within an existing course should not automatically be counted as removing or replacing all of that course's credits.

## 8. Task 1 Integration

The proposed capstone is an AI-assisted curriculum-analysis and review workflow.

Potential functions include:

1. Import permitted course and learning-outcome information.
2. Compare course outcomes with documented job requirements.
3. Identify possible overlap for human review.
4. Recommend practical exercises or assessment improvements.
5. Record sources, evidence, dates, and verification results.
6. Generate a report for faculty review.
7. Display course comparisons and provisional credit calculations.

The system should use public or synthetic data where appropriate. It should not require unauthorized access to college systems or collect private student information.

The report must distinguish components implemented in Task 1 from future extensions that are only proposed.

## 9. AI-Assisted Exercises

The project records five exercises in:

`exercises/ai_assisted_exercises.md`

The subjects covered are:

1. C programming.
2. Data structures and algorithms.
3. Database management systems.
4. Operating systems.
5. Machine learning.

For each exercise, the evidence should include:

- Learning objective.
- Exact prompt.
- AI model and date of use.
- Generated output or a concise output record.
- Test inputs and expected results.
- Actual results and verification method.
- Corrections and limitations.

Only completed and documented tests should be described as executed. A logical review of code is not the same as compiling and running the code, and checking a metric calculation is not the same as training and evaluating a machine-learning model.

## 10. Faculty or Graduate Feedback

Feedback should be included only if it is genuinely received and permission is available to use it.

If faculty or graduate feedback could not be obtained, state that clearly and explain that the proposal is based on documentary research and independent analysis instead.

Do not invent quotations, participants, or endorsements.

## 11. Limitations and Verification

The main limitations are:

- The applicable 2023-batch syllabus has not been confirmed.
- The official programme reference is a partial extract.
- The listed-credit subtotals are not the official degree-credit total.
- A complete comparison of official course outcomes has not yet been established.
- At least three specific job advertisements still need fully documented evidence.
- Proposed REDUCE and ADD decisions require evidence of duplication or a genuine coverage gap.
- Faculty or graduate feedback must not be claimed unless actually obtained.
- AI-generated content and calculations require independent verification.

The project is a student proposal and does not constitute an approved change to university regulations.

## 12. Conclusion

The proposed review aims to preserve core computer-science knowledge while strengthening practical software development, testing, databases, cloud deployment, data analysis, and AI learning.

Final recommendations should be based on the applicable official syllabus, traceable job advertisements, documented exercise verification, balanced credit calculations, and transparent limitations. Until the correct admission-batch curriculum is confirmed, course mappings and credit-change percentages remain provisional.

## Official Curriculum Baseline and Verification

**Institution:** The ICFAI Foundation for Higher Education, Hyderabad  
**School:** ICFAITech  
**Degree:** B.Tech  
**Branch:** Computer Science and Engineering  
**Admission batch under review:** 2023  
**Expected graduation:** 2027  

### Official sources checked

1. [ICFAITech B.Tech programme structure](https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure)
2. [IFHE syllabus listing for ICFAITech](https://naac2020.ifheindia.org/1.1.3Syllabus%20IcfaiTech.html)

### Verification result

The publicly available programme structure provides a reference for reviewing CSE course coverage, course titles, semester placements and credits. However, the public pages reviewed do not establish that the displayed structure is the exact curriculum applicable to the 2023 admission batch.

Therefore, this report distinguishes the publicly available reference curriculum from the student's confirmed batch-specific curriculum.

The following details remain unverified:

1. The complete semester-wise course structure applicable to the 2023 admission batch.
2. The official total degree-credit requirement for that batch.
3. The exact elective options and the electives selected by the student.
4. The applicable credit-counting rules for internships, thesis, summer terms and non-credit courses.
5. Whether the curriculum or regulations changed for the 2023 cohort.

### How this affects the proposed redesign

The public curriculum may be used for a preliminary comparison of subject coverage. However, the proposed curriculum must remain separate from the official reference data.

Until the applicable batch-specific regulations are confirmed, this analysis does not claim a verified official degree-credit total or an exact percentage of degree credits changed.

The credit impact of proposed additions, reductions and updates should be recalculated against the verified batch-specific baseline when it becomes available.

### Limitation

The exact curriculum for the 2023 admission batch could not be confirmed from the public pages reviewed. This limitation is disclosed rather than filling gaps with assumed courses or credits. The analysis is a student-led proposal and does not represent an official IFHE curriculum revision.
