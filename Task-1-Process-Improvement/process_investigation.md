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
### 14. Decision Rule: When to Change or Abandon the Proposal

SkillBridge AI should not be adopted simply because a prototype has been developed.

I would reconsider or abandon the proposed system if permission-based investigation showed that the existing submission process already provides reliable tracking, timely feedback, and an acceptable workload, leaving little or no meaningful problem to solve.

I would also reconsider the design if measured trials showed that operating the system, reviewing submissions, handling errors, and supporting users required as much or more time than the existing process.

Before recommending adoption, I would compare the existing and proposed workflows using the same representative synthetic cases and record the time, errors, recovery effort, and user feedback. Any recommendation would remain conditional on institutional approval, appropriate security controls, and evidence of a genuine improvement.

**Current position:** These are decision criteria for future evaluation, not findings from a completed field study.
## Final Evidence and Feasibility Assessment

### Existing-process investigation

This submission proposes a project-submission and faculty-review workflow.
The proposed workflow must not be interpreted as a verified description
of the current process at ICFAI.
### Independent Verification and Evidence Limitations

No completed student interview, faculty or process-owner interview, permission-based operational observation, or official-document verification is documented in this submission.

The current-process map is therefore a hypothetical walkthrough, not a verified description of ICFAI's actual process. The evidence log should distinguish prototype test results from assumptions and identify any future verification activities that are completed.

Submission-volume figures and time-saving calculations remain estimates until actual counts and recorded timings are available.
Therefore, the current-process description is a hypothetical walkthrough
used to identify possible handoffs, missing information, duplicate
submissions, authorization checks, and technical failures.

The evidence sample for actual college operations is zero. The proposed
workflow and test cases are design and prototype evidence, not proof
that the same problems occur in the institution.

Before any real deployment, the process owner would need to confirm
the existing steps, responsibilities, request volume, actual handling
time, rework rate, and approved fallback procedure.

### Permission and privacy

No access to confidential college records is required for this proposal.
Any future observation or interview must be voluntary and permission-based.
If permission is unavailable, the investigation will remain hypothetical.
Only synthetic test records and permitted evidence will be shared.

### Illustrative time-saving calculation

The following values are planning assumptions, not measured college data.

**Illustrative rework calculation:** Assume that 20% of requests require 10 additional minutes of rework. Expected rework effort per request is 0.20 × 10 = 2 minutes. For this example, the existing-process estimate of 12 minutes consists of 10 minutes of initial handling and follow-up plus 2 expected rework minutes. These assumptions are unmeasured and must be validated; they are not ICFAI operational data.

| Activity | Illustrative time per request |
|---|---:|
| Existing process, including status checking and follow-up | 12 minutes |
| Proposed submission | 3 minutes |
| Proposed status check | 1 minute |
| Additional review and support | 2 minutes |
| Proposed total | 6 minutes |

Illustrative net time saved per request:

12 - (3 + 1 + 2) = 6 minutes.

| Requests per month | Illustrative monthly time saved |
|---:|---:|
| 10 | 60 minutes |
| 40 | 240 minutes |
| 100 | 600 minutes |

These figures do not establish actual demand or savings at ICFAI.

### Implementation effort and break-even

Implementation effort has not been measured. For planning purposes only,
suppose implementation requires 6 hours, equivalent to 360 minutes.

At the illustrative saving of 6 minutes per request, the one-time
implementation effort would be recovered after:

360 / 6 = 60 requests.

This is a hypothetical break-even calculation, not a measured return
on investment. Actual feasibility depends on implementation effort,
maintenance, training, request volume, and measured time savings.

### Conditions that would change the proposal

The design should be reconsidered or abandoned if a permission-based
investigation finds that the existing process already provides reliable
submission tracking, timely reviews, acceptable workload, and effective
exception handling.

It should also be revised if implementation and support costs outweigh
the measured benefits, or if the proposed system cannot enforce
appropriate access controls and preserve an auditable approval process.
## Existing Process and Roles Map — Hypothetical Walkthrough

### 1. Investigation Status

This section presents a hypothetical walkthrough of a student project-submission and faculty-review process. It is used to identify possible handoffs, delays and exceptions before designing the proposed SkillBridge AI workflow.

The current process described below has not been independently verified at ICFAI. No faculty interview, permission-based operational observation or institutional record was available to confirm these steps. The roles and actions below are illustrative, not claims about actual ICFAI procedures.

### 2. Hypothetical Current-State Steps

| Step | Hypothetical action | Responsible role | Handoff or decision | Possible issue to investigate |
|---|---|---|---|---|
| 1 | A student prepares a project submission using the instructions provided for the assignment. | Student | Student prepares the submission for the designated submission channel. | The student may misunderstand required information or the deadline. |
| 2 | The student submits the project through the designated channel. | Student | Submission is passed to the receiving person or system. | The student may not receive clear confirmation that the submission was received. |
| 3 | The submission is received and checked for required information. | Hypothetical receiving coordinator or designated reviewer | Complete submissions proceed; incomplete submissions may require clarification. | Missing information may cause additional messages and repeated work. |
| 4 | The submission is assigned or forwarded to the appropriate faculty reviewer. | Hypothetical coordinator or designated owner | The submission is handed to the authorized reviewer. | The responsible reviewer or current status may not be obvious to the student. |
| 5 | The reviewer evaluates the submission against the applicable criteria. | Authorized faculty reviewer | The reviewer decides whether to approve it, reject it or request changes, according to applicable rules. | Review may be delayed if information is missing or the submission reaches the wrong reviewer. |
| 6 | If changes are required, feedback is sent to the student. | Authorized faculty reviewer | The student receives feedback and prepares a revised submission. | Feedback and revised versions may be difficult to track if there is no consistent record. |
| 7 | The student resubmits, where permitted, and the submission is reviewed again. | Student and authorized faculty reviewer | The revised submission returns to the review stage. | Repeated corrections may increase the total handling time. |
| 8 | The outcome is communicated and the submission record is retained. | Hypothetical designated process owner or authorized reviewer | The student receives the outcome; the responsible owner retains any required record. | The student may need to ask for an update if the outcome or status is unclear. |

### 3. Roles and Responsibilities

- **Student:** Supplies the required information, submits the project and responds to requests for corrections.
- **Receiving coordinator or designated owner:** Hypothetically receives submissions, checks completeness and routes them to the appropriate reviewer. The existence of this role in the actual process must be verified.
- **Authorized faculty reviewer:** Evaluates the submission and makes academic decisions within their authority.
- **Process owner or administrator:** Hypothetically maintains the process record and handles routing or status questions where applicable. This role has not been confirmed at ICFAI.

The proposed system must not grant itself academic decision-making authority. Approval, rejection and academic exceptions must remain with the authorized human decision-maker.

### 4. Handoffs, Approvals and Exceptions

**Handoffs:** Student to receiving channel; receiving channel to designated reviewer; reviewer to student when corrections are needed; and reviewer or designated owner to the final outcome record.

**Approval boundary:** Only the appropriately authorized human reviewer may make the academic decision. Automated checks may identify missing fields, likely duplicates or unauthorized access, but they must not independently approve academic work.

**Hypothetical exceptions to investigate:**

1. A submission is missing required information.
2. A student submits the same project more than once.
3. A submission reaches the wrong reviewer or an unauthorized person attempts to access it.
4. A student resubmits after receiving feedback.
5. A submission is delayed, lost or cannot be accessed because of a technical failure.
6. The student disputes the outcome or requests clarification.

These are possible scenarios for investigation and testing, not confirmed incidents at ICFAI.

### 5. Evidence Needed to Verify the Current Process

If permission becomes available, the following questions should be asked of a willing process user or owner:

- Which channel is used to submit a project?
- Who receives and checks the submission?
- How is the authorized reviewer identified?
- What information is required before review begins?
- How are missing information, duplicates and resubmissions handled?
- Who makes the final decision?
- How is the student informed of the status and outcome?
- What happens if a submission or communication fails?
- How much time does each stage normally take, and how often does rework occur?

Only permitted, non-identifying information should be recorded. If access is unavailable or declined, the hypothetical designation must remain in the final report.

### 6. Current-State Conclusion

This hypothetical map provides a structured baseline for testing the proposed workflow. It does not establish that the described process, roles, delays or rework occur at ICFAI. Those claims require permission-based observation or confirmation from an appropriate process user or owner. Any time-saving estimate must therefore remain illustrative until actual process data can be collected.
## AI Versus Ordinary Software

The proposed SkillBridge AI workflow does not require AI for every step. Ordinary software and predefined rules are more appropriate for most administrative tasks.

| Function | Recommended approach | Reason |
|---|---|---|
| Check whether required fields are filled | Ordinary software validation | Required fields can be checked using fixed rules. |
| Generate a submission ID and timestamp | Ordinary software | These values can be generated consistently without AI. |
| Check for duplicate submissions | Database constraints and matching rules | Exact duplicates can be detected using stored identifiers and file hashes. Potentially similar submissions may need human review. |
| Verify access permissions | Authentication and authorization rules | Access must be controlled by explicit permissions, not an AI prediction. |
| Track submission status | Database and workflow logic | Fixed statuses provide a consistent record of progress. |
| Notify students about status changes | Automated notifications | Notifications can be triggered by defined events. |
| Summarize long feedback or explain submission instructions | Optional AI assistance | AI may help users understand text, but its output must be checked. |
| Make the final academic decision | Authorized human reviewer | Academic approval or rejection must not be delegated to an AI model. |

### Does AI add enough value?

AI is optional in the initial version. The core workflow can operate using ordinary software, validation rules, a database and authorized human review. Adding an AI feature is justified only if a verified need exists, such as helping students understand lengthy feedback.

AI-generated explanations may omit important details or misinterpret instructions. Users must be able to consult the original feedback, and the authorized faculty reviewer remains responsible for academic decisions. No confidential student data should be sent to an external AI service without appropriate authorization.

Because the current college process has not been independently verified, the actual need for AI and its benefits remain unproven. The first implementation should prioritize reliable workflow tracking and measure whether it reduces handling time before adding optional AI features.

## Independent Verification Status

The actual project-submission and faculty-review process at ICFAI has not been independently verified for this investigation.

- Student interview documented: No
- Faculty or process-owner interview documented: No
- Permission-based operational observation documented: No
- Official college process documentation independently verified: No
- Independently verified operational requests: 0

The evidence consists of the proposed workflow, prototype tests, synthetic test cases, and illustrative calculations. The hypothetical current-process time of 12 minutes per request and estimated net saving of 6 minutes per request are planning assumptions, not measured results.

Before real deployment, the relevant process owner would need to confirm the current steps, responsibilities, request volume, handling time, rework rate, and approved fallback procedure. No student personal or confidential academic information should be included in the report.

## Final Requirement Closure — Workflow, ROI, Safety and Decision Criteria

### Fieldwork status and permission boundary

This investigation uses an explicitly hypothetical walkthrough because the actual college process has not been independently verified. No student interview, faculty/process-owner interview, permission-based operational observation, or independent verification of official process documentation is claimed. The independently verified operational request sample is zero. The walkthrough identifies possible steps and failure points for future investigation; it does not establish that these problems occur at ICFAI.

Any future fieldwork must begin with permission, stop if permission is declined, and avoid disrupting college activities. Record a participant's role only, if a voluntary conversation occurs. Do not collect names, student IDs, marks, fees, signatures, credentials, private messages, or other confidential information. Use synthetic examples for prototype testing.

### Hypothetical current workflow and accountable roles

| Step | Responsible role (proposed/hypothetical) | Action | Handoff or exception |
|---|---|---|---|
| 1 | Student/requester | Prepares a request and required information | Missing information requires correction |
| 2 | Receiving staff/process owner | Receives and checks the request | Incomplete requests are returned with a reason |
| 3 | Process owner | Records receipt and current status | Duplicate requests are flagged and linked to the existing request |
| 4 | Authorized reviewer | Reviews the request against applicable requirements | Only the authorized decision-maker may approve or reject |
| 5 | Requester and process owner | Receive the decision/status update | Failed notification or system step is escalated and logged |
| 6 | Process owner | Closes the request and retains an appropriate audit record | Unresolved cases remain open and are escalated |

This is a proposed model, not a verified map of the college's existing responsibilities.

### Effort and return-on-investment calculation

All figures below are illustrative planning assumptions, not measured college timings or request volumes.

**Hypothetical current effort per request**
- Initial handling: 6 minutes.
- Status follow-up: 4 minutes.
- Expected rework: 20% of requests require 10 additional minutes on average; expected rework per request = 0.20 × 10 = 2 minutes.
- Total expected current effort = 6 + 4 + 2 = **12 minutes per request**.

**Hypothetical proposed effort per request**
- Submission and validation: 3 minutes.
- Status check: 1 minute.
- Review/support/error-handling allowance: 2 minutes.
- Total proposed effort = 3 + 1 + 2 = **6 minutes per request**.
- Illustrative net saving = 12 − 6 = **6 minutes per request**.

| Assumed requests per month | Current effort | Proposed effort | Illustrative net saving |
|---:|---:|---:|---:|
| 20 | 240 minutes (4 hours) | 120 minutes (2 hours) | 120 minutes (2 hours) |
| 60 | 720 minutes (12 hours) | 360 minutes (6 hours) | 360 minutes (6 hours) |
| 100 | 1,200 minutes (20 hours) | 600 minutes (10 hours) | 600 minutes (10 hours) |

Assume a one-time implementation effort of 6 hours (360 minutes). At an illustrative saving of 6 minutes per request, simple break-even is 360 ÷ 6 = **60 requests**. This excludes unmeasured recurring maintenance and any costs not represented in the per-request allowance. If real support/maintenance costs increase or net savings are lower, break-even will occur later or may never occur. The monthly request range of 20–100 is a scenario for sensitivity analysis, not an observed volume.

### Proposed workflow controls

1. **Inputs:** request category, required fields, non-sensitive description, and a generated request reference.
2. **Statuses:** Draft → Submitted → Needs Information / Under Review → Approved or Rejected by an authorized human → Closed. A system failure is recorded as Failed/Needs Recovery, not silently treated as approval.
3. **Accountable owner:** a designated process owner monitors unresolved requests and escalations; the institution must confirm the actual role before implementation.
4. **Approval boundary:** ordinary software can validate fields, detect duplicates, track status and enforce role checks. Only the authorized human decision-maker may make the substantive approval/rejection decision.
5. **Audit record:** record the request reference, status changes, timestamps, action type and authorized role, while limiting access and retention appropriately. Avoid unnecessary personal or confidential data.
6. **Fallback:** if storage, notification or another step fails, show a clear error, avoid claiming success, preserve or safely retry the request where possible, log the failure without exposing secrets, and route unresolved cases to the process owner. Do not create a duplicate during retry.

### Five synthetic cases and recovery

| Case | Expected result | Recovery and decision authority | Evidence limitation |
|---|---|---|---|
| Normal request | Required fields pass validation; request receives a reference and Submitted status | Authorized reviewer handles the request; requester can check status | Screenshot/user-confirmed prototype result; not proof of live college use |
| Missing information | Validation identifies missing fields; request is not sent for approval | Requester supplies missing information and resubmits; reviewer decides only when complete | Synthetic prototype case |
| Duplicate request | Existing matching request is flagged; no silent second processing | Show the existing reference and let the process owner resolve uncertain matches | Synthetic prototype case; real duplicate rate is unknown |
| Unauthorized request | Role check denies an unauthenticated or unauthorized action and logs the denial | User signs in or contacts the authorized owner; no approval is granted by the test | Runtime authorization test passed; this does not establish institutional authorization policy |
| Database/step failure | Clear failure state; no false success message and no approval inferred from a failed operation | Retry safely or escalate to the process owner; check persistence before retrying | Mocked database-failure test passed; a real production outage/recovery was not tested |

### Ordinary software versus AI

The core workflow does not require AI. Field validation, duplicate checks, role-based authorization, status tracking, audit logging and failure handling should use ordinary software and deterministic rules. AI could be considered later for optional plain-language explanations of non-confidential instructions, but only if an evidenced need exists. AI must not decide academic approvals, override access controls or receive confidential student information without explicit authorization and appropriate safeguards. Human reviewers remain responsible for decisions.

### Risks, unknowns and design-abandonment criterion

Key unknowns include the actual existing workflow, accountable roles, request volume, current handling time, rework rate, acceptable retention policy, user needs and whether a new system is warranted. Risks include unauthorized access, duplicate records, data loss, misleading status messages, excessive support work and unnecessary AI complexity.

**Change/abandonment criterion:** after permission and approval, conduct a small pilot using synthetic or appropriately authorized data and compare representative requests using the same timing method. If the proposed process produces no positive net time saving after review, support, rework and maintenance—or increases serious errors or unauthorized actions—do not recommend adoption in its current form. Rework the design or retain the existing process until evidence supports a change.

### Final evidence boundary

Prototype test success supports only the behavior exercised by those tests. It does not prove real college adoption, actual request volume, measured time savings, or institutional approval. The report's time figures and volume scenarios are illustrative and must remain labelled as assumptions until permission-based evidence exists.
