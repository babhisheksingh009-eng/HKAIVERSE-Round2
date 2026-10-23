# SkillBridge AI
## Task 1: Process Investigation and Improvement

### 1. Objective

Investigate the academic project submission and review workflow, identify potential inefficiencies, and propose a structured process that improves submission tracking, review management, and feedback visibility.

This investigation is based on personal experience. The current workflow and its potential problems require further verification.

### 2. People Involved

**Students**
- Prepare and submit academic projects.
- Provide required project details and report or repository links.
- Check submission status and review feedback.

**Faculty Members**
- Access submitted projects.
- Review project information and deliverables.
- Update review status and provide feedback or marks where applicable.

**System Administrator — Proposed Role**
- Maintain the application and database.
- Manage user accounts and permissions.
- Investigate technical issues and support system availability.

The administrator role is part of the proposed system design and has not been confirmed as a role in the existing institutional workflow.

### 3. Current Workflow

Based on personal experience, academic project submissions may follow these steps:

1. **Project preparation:** The student prepares the project and supporting documents.
2. **Submission:** The student submits the project through an online form, website, or direct communication with faculty.
3. **Information transfer:** The submission details are made available to the relevant faculty member.
4. **Faculty review:** The faculty member reviews the submitted work.
5. **Feedback:** The faculty member provides feedback and, where applicable, marks.
6. **Student follow-up:** The student checks for feedback or contacts faculty if clarification is needed.

**Important:** This is an initial process model based on personal experience, not a verified description of every IFHE course or department's workflow.

### 4. Workflow Handoffs and Responsibilities

| Step | Responsible person | Handoff | Information involved |
|---|---|---|---|
| Project preparation | Student | Student prepares the submission | Project files and details |
| Submission | Student | Submission is sent to the relevant faculty member or system | Title, subject, description, report or repository link |
| Submission access | Faculty member | Faculty obtains the submitted project | Submission details and deliverables |
| Review | Faculty member | Review proceeds to feedback or a decision | Project deliverables and evaluation criteria |
| Feedback | Faculty member | Feedback becomes available to the student | Comments, status, and marks where applicable |
| Follow-up | Student | Student requests clarification if necessary | Submission reference and review information |

The exact handoffs, approvals, and information-sharing methods must be verified with the relevant participants.

### 5. Initial Observations

The initial investigation suggests that submission and review practices may vary by subject or faculty member.

Potential areas to investigate include:

- Whether students receive confirmation after submitting a project.
- Whether students can check review status independently.
- How faculty members identify pending submissions.
- How missing or incorrect submission information is handled.
- How feedback is communicated to students.
- How duplicate submissions are identified.

These points are investigation questions, not confirmed institutional shortcomings.

### 6. Potential Problems and Exceptions

| Potential issue | Possible impact | Verification required |
|---|---|---|
| No consistent submission reference | Difficulty locating a particular submission | Check whether current systems provide reference numbers |
| Limited status visibility | Students may need to request updates | Ask students how they check review progress |
| Missing required information | Faculty may need clarification before reviewing | Investigate how incomplete submissions are handled |
| Duplicate submissions | Repeated records or confusion about the correct version | Ask how duplicate submissions are identified |
| Delayed feedback | Students may not know when feedback will be available | Collect appropriate process data before estimating delays |
| Unavailable submission system | Students may be unable to submit or access project information | Verify current recovery procedures |

These are potential risks. Their frequency, severity, and actual impact have not yet been measured.

### 6A. Illustrative Scale Estimate

The actual number of academic project submissions handled by the relevant department has not been collected. Therefore, the following scenarios illustrate how the potential impact could vary with submission volume. They are not estimates of actual IFHE activity.

The preliminary time-saving calculation in the evidence log assumes a possible net saving of six minutes per submission. That figure has not been measured and must be validated.

| Hypothetical submissions per month | Potential saving per submission | Illustrative total time saved per month |
|---:|---:|---:|
| 10 | 6 minutes | 60 minutes (1 hour) |
| 40 | 6 minutes | 240 minutes (4 hours) |
| 100 | 6 minutes | 600 minutes (10 hours) |

**Calculation:** Hypothetical monthly time saved = submissions per month × assumed minutes saved per submission.

For example, 40 × 6 = 240 minutes, or four hours per month.

**Limitations:** Submission volumes are hypothetical, and the six-minute saving is an unmeasured planning assumption. These calculations do not demonstrate actual demand, actual time savings, or college-wide impact. To estimate the real scale, obtain permission to collect an appropriate submission count and conduct timed comparisons of the existing and proposed workflows.

### 7. Proposed Improved Workflow

SkillBridge AI proposes a structured workflow for project submission and review.

1. **Student login:** The student signs in using an authorized account.
2. **Submission form:** The student enters the project title, subject, description, and report or repository link.
3. **Validation:** The application checks that required information is present.
4. **Duplicate detection:** The application checks for potential duplicate submissions according to its configured rules.
5. **Submission recording:** The application saves the submission and generates a unique reference number.
6. **Status assignment:** The submission receives the initial status `SUBMITTED`.
7. **Faculty access:** An authorized faculty member accesses the submission.
8. **Review:** Faculty members update the review status and provide feedback.
9. **Student notification or status check:** The student checks the available submission status and feedback.
10. **Exception handling:** The application displays suitable errors for invalid information, unauthorized actions, or database connection failures.

This workflow describes the intended prototype behavior. Actual implementation details and successful operation should be verified through testing.

### 8. Exception Handling and Controls

| Exception | Proposed response |
|---|---|
| Missing required information | Display a validation message and request correction |
| Potential duplicate submission | Warn the user or prevent an unintended duplicate according to the configured rule |
| Unauthorized review action | Reject the action and preserve role restrictions |
| Database connection failure | Display a readable error and avoid falsely reporting success |
| Review not yet completed | Keep the submission in an appropriate pending status |
| Invalid or unavailable repository link | Ask the student to correct the link if link validation is implemented |

### 9. Proposed Performance Measures

The following measures can help evaluate whether the proposed workflow improves the existing process:

- **Submission completion time:** Time required to complete and record a valid submission.
- **Status enquiry effort:** Time spent by students and faculty answering status-related enquiries.
- **Review turnaround time:** Time between submission and review completion.
- **Incomplete submission rate:** Number of incomplete submissions divided by total submissions.
- **Duplicate submission rate:** Number of duplicate records divided by total submissions.
- **Net time saved:** Baseline processing time minus the improved process's processing time and additional review or support effort.

These measures require actual observations or test data. No verified time-saving result is claimed at this stage.

### 10. Evidence Collection Plan

Further investigation should include:

1. Permission-based discussions with students and faculty members.
2. Documentation of the current submission and review process.
3. Recording of observed facts separately from assumptions and estimates.
4. Synthetic test cases for normal submission, missing information, duplicate submission, unauthorized access, and database failure.
5. Baseline and prototype timing measurements where feasible.
6. Evidence references, observation dates, and limitations for each finding.

No private student information, confidential institutional records, or unauthorized data should be collected.

### 11. Proposed Solution: SkillBridge AI

SkillBridge AI is a prototype intended to organize academic project submissions and reviews.

Its proposed capabilities include:

- Project submission management.
- Unique submission reference numbers.
- Status tracking.
- Faculty feedback management.
- Role-based access controls.
- Input validation and duplicate detection.
- Submission and review statistics.

The prototype demonstrates a possible approach to improving workflow organization. Its actual benefits must be evaluated using documented evidence and suitable measurements.

### 12. Limitations

- The initial investigation is based on personal experience.
- The current institutional workflow has not been independently verified.
- Faculty and student interviews have not yet been documented.
- The frequency and impact of the potential problems remain unknown.
- Time savings and performance improvements have not been measured.
- Authorization-function tests use simulated session states and do not verify the entire application end to end.
- Database connection-failure testing does not cover every possible database error.
- The prototype is not an official IFHE system.

A real deployment would require appropriate institutional approval, secure account management, access controls, data protection, and operational support.

### 13. Conclusion

SkillBridge AI proposes a structured approach to academic project submission and review. It introduces validation, submission references, review statuses, faculty feedback, role-based access checks, and error handling.

The next stage is to verify the current workflow, collect appropriate evidence, and measure the prototype against defined performance indicators before claiming measurable improvements.