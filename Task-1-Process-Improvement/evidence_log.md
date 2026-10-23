# SkillBridge AI
## Task 1: Evidence Log

### Purpose

This evidence log documents observations, potential workflow problems, design decisions, preliminary time-saving estimates, and prototype testing for the academic project submission and review workflow. Personal observations, assumptions, user-reported results, and executed test results are distinguished to avoid presenting unverified claims as established facts.

---

### Entry 1: Initial Process Observation

- **Date recorded:** 22 October 2026
- **Process investigated:** Academic project submission and review
- **Source:** Personal experience as a student
- **People involved:** Students and faculty members
- **Evidence classification:** Personal observation

**Observation:**

Based on my personal experience, students submit academic projects through online forms, websites, or directly to faculty members. Faculty members review submissions and may provide feedback and marks, depending on the assignment and institutional process.

The exact workflow may vary by subject, faculty member, and submission method.

**Limitations:**

This observation has not been independently verified. No faculty interviews, formal measurements, or official college records have been collected for this entry.

**Next action:**

Seek permission to ask students and faculty members about their current submission and review procedures.

---

### Entry 2: Potential Workflow Problem

- **Date recorded:** 22 October 2026
- **Potential issue:** Inconsistent availability of project review status information
- **Source:** Personal experience
- **Evidence classification:** Potential problem requiring verification

**Description:**

Students may not always have a consistent way to determine whether their projects have been received, are awaiting review, or have been reviewed.

If submission and feedback information is distributed across different channels, students may need to contact faculty members to obtain updates. However, the frequency and impact of this situation have not yet been measured.

**Verification plan:**

1. Ask classmates about their experiences, with their permission.
2. Ask a faculty member how submissions, reviews, and feedback are currently tracked, with their permission.
3. Record responses without collecting private or confidential information.
4. Compare the reported workflow with the proposed SkillBridge AI workflow.

**Limitations:**

The frequency, impact, and causes of the potential problem have not been established. The problem should not be presented as a confirmed institution-wide issue without additional evidence.

---

### Entry 3: Proposed Solution

- **Proposed system:** SkillBridge AI
- **Purpose:** Organize academic project submissions, review statuses, and faculty feedback
- **Evidence classification:** Proposed design

**Proposed features:**

1. Record project submissions.
2. Generate a unique reference number for each submission.
3. Display submission and review statuses.
4. Associate faculty feedback with the relevant submission.
5. Provide student and faculty views according to their roles.
6. Validate required information and detect potential duplicate submissions.
7. Display an error when the database connection fails.

**Expected benefits:**

- Improved visibility of submission status.
- Easier identification of pending reviews.
- More organized access to feedback.
- Potential reduction in manual status enquiries, if these are part of the existing workflow.

**Limitations:**

These are expected benefits, not measured improvements. No verified time savings or institution-wide impact has been established.

**Verification plan:**

Test the prototype using five scenarios: normal submission, missing information, duplicate submission, unauthorized access, and database connection failure.

---

### Entry 4: Prototype Testing Evidence

- **Testing period:** October 2026
- **System:** SkillBridge AI local prototype
- **Data:** Test accounts and synthetic project data
- **Evidence classification:** User-reported test results and executed software tests

#### Test 1: Normal Submission

**Activity:** Test a project submission with valid information.

**Result:** The user confirmed that normal submission works.

**Status:** PASS — based on user confirmation.

**Evidence reference:** Retain a screenshot of the successful submission, including its reference number and status.

**Limitation:** A screenshot should be retained to independently demonstrate the result.

#### Test 2: Missing Information

**Activity:** Submit a project with a required field missing.

**Result:** The user confirmed that required-field validation works.

**Status:** PASS — based on user confirmation.

**Evidence reference:** Retain a screenshot of the validation message and rejected submission.

**Limitation:** A screenshot should be retained to independently demonstrate the result.

#### Test 3: Duplicate Submission

**Activity:** Attempt to submit the same project more than once.

**Result:** The user confirmed that duplicate detection works.

**Status:** PASS — based on user confirmation.

**Evidence reference:** Retain a screenshot or database query result showing the duplicate-detection behavior and whether an unintended record was created.

**Limitation:** The precise duplicate-detection rule and database result should be documented using actual test evidence.

#### Test 4: Authorization Function

**Activity:** Execute `python test_authorization_runtime.py` to test the actual `require_role()` function using simulated session states.

**Result:** All three test cases passed:

- A student was rejected from faculty-only actions.
- A faculty user was allowed to continue.
- An unauthenticated user was rejected.

**Status:** PASS — authorization-function tests passed.

**Evidence reference:** Terminal output from `python test_authorization_runtime.py`.

**Limitation:** The test uses simulated session states. The complete login flow, browser-level behavior, and actual database review operation have not been tested end to end.

#### Test 5: Database Connection Failure

**Activity:** Temporarily configure the application to use an unavailable MySQL port and observe its error handling.

**Result:** The application displayed a readable connection error and explained that the database connection failed.

**Status:** PASS — connection-failure handling tested.

**Evidence reference:** Retain the application or terminal output showing the connection error.

**Limitation:** This test verifies handling of a connection failure, not every possible database error or transaction failure.

---

### Entry 5: Evidence Quality and Remaining Investigation

- **Date recorded:** 23 October 2026
- **Activity:** Review of evidence and prototype test documentation
- **Source:** Personal observations, user-reported test outcomes, and executed test output
- **Evidence classification:** Documentation review

**Findings:**

1. The potential workflow problem remains unverified through independent interviews or institutional records.
2. The prototype has five documented testing scenarios.
3. The normal submission, missing-information, and duplicate-submission results are based on user confirmation.
4. The authorization-function test was executed successfully using simulated session states.
5. The database connection-failure behavior was tested using an unavailable MySQL port.
6. Evidence screenshots and logs should be retained alongside the relevant test results.
7. Actual time savings have not been measured.

**Next actions:**

- Collect permission-based feedback from students or faculty, if available.
- Save screenshots and test logs for the five scenarios.
- Document the existing workflow and its handoffs, approvals, and exceptions.
- Measure baseline processing time and prototype processing time before claiming actual time savings.
- Update the preliminary time-saving calculation when supporting measurements are available.
- Record limitations and unresolved issues in the final report.

---

### Entry 6: Preliminary Time-Saving Estimate

- **Date recorded:** 23 October 2026
- **Activity:** Preliminary comparison of the existing and proposed project-submission workflows
- **Evidence classification:** Illustrative estimates, not measured results

**Purpose:**

Estimate the potential time required to process one academic project submission using the existing workflow and the proposed SkillBridge AI workflow.

**Illustrative estimates:**

| Activity | Estimated time |
|---|---:|
| Existing manual process, including recording, status checking, and follow-up | 12 minutes |
| Entering and submitting project details using SkillBridge AI | 3 minutes |
| Checking submission status using SkillBridge AI | 1 minute |
| Additional review and support effort | 2 minutes |
| **Total improved process time, including support** | **6 minutes** |

**Calculation:**

Net time saved = Existing process time − Improved submission time − Status-checking time − Additional review and support time

Net time saved = 12 − 3 − 1 − 2

**Estimated net time saved = 6 minutes per submission.**

**Interpretation:**

Under these illustrative assumptions, the proposed workflow could save approximately six minutes per submission. This estimate is a preliminary planning calculation and does not establish that SkillBridge AI actually saves six minutes.

**Limitations:**

The 12-minute baseline and the two-minute additional review/support estimate have not been independently measured. The three-minute submission time and one-minute status-checking time are planning estimates. Actual timings may vary depending on the submission, user, and review requirements.

The estimate is not based on a controlled experiment, a college-wide study, or verified stopwatch measurements. It should not be presented as a proven result.

**Next action:**

Conduct timed tests using synthetic project data. Compare the existing workflow with the prototype, record the results, and update the calculation if measured results become available.

---

### Overall Evidence Statement

SkillBridge AI is a prototype intended to improve the organization and visibility of academic project submissions and reviews. Its documented test scenarios provide initial evidence of functionality, including authorization-function behavior and database connection-failure handling.

The normal submission, missing-information, and duplicate-submission results are based on user confirmation. The authorization-function and database connection-failure tests were executed, subject to the limitations documented above.

The current evidence does not establish that the identified workflow problem is widespread, that the system is production-ready, or that it produces a specific amount of time savings. The preliminary estimate of six minutes per submission is illustrative and requires validation through timed testing.

Further investigation, retained test evidence, and measured processing times are needed before making claims about actual workflow improvements.