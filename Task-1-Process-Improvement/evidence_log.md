# SkillBridge AI
## Task 1: Evidence Log

### Purpose

This evidence log documents observations, potential workflow problems, design decisions, preliminary time-saving estimates, and prototype testing for the academic project submission and review workflow. Personal observations, assumptions, user-reported results, and executed test results are distinguished to avoid presenting unverified claims as established facts.

---

### Entry 1: Initial Hypothesis and Process Model

- **Date recorded:** 22 October 2026
- **Process investigated:** Academic project submission and review
- **Source:** Personal experience as a student
- **People involved:** Students and faculty members
- **Evidence classification:** Personal experience / unverified hypothesis

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

**Evidence reference:** `evidence/test1_normal_submission.png`.

**Limitation:** The screenshot supplements the user-confirmed result; no database-query evidence was retained.

#### Test 2: Missing Information

**Activity:** Submit a project with a required field missing.

**Result:** The user confirmed that required-field validation works.

**Status:** PASS — based on user confirmation.

**Evidence reference:** `evidence/test2_missing_information.png`.

**Limitation:** The screenshot supplements the user-confirmed result; no database-query evidence was retained.

#### Test 3: Duplicate Submission

**Activity:** Attempt to submit the same project more than once.

**Result:** The user confirmed that duplicate detection works.

**Status:** PASS — based on user confirmation.

**Evidence reference:** `evidence/test3_duplicate_submission.png`.

**Limitation:** The screenshot supplements the user-confirmed result; no database-query evidence was retained to independently verify whether a duplicate record was created.

#### Test 4: Authorization Function

**Activity:** Execute `python test_authorization_runtime.py` to test the actual `require_role()` function using simulated session states.

**Result:** All three test cases passed:

- A student was rejected from faculty-only actions.
- A faculty user was allowed to continue.
- An unauthenticated user was rejected.

**Status:** PASS — authorization-function tests passed.

**Evidence reference:** `authorization_test.log`, containing the three authorization test results.

**Limitation:** The test uses simulated session states. The complete login flow, browser-level behavior, and actual database review operation have not been tested end to end.

#### Test 5: Database Connection Failure

**Activity:** Run the standalone test `python test_database_failure.py`, which uses a mock object to simulate a MySQL connection error.

**Result:** The standalone test detected the simulated connection error and reported that the simulated failure was handled.

**Status:** PASS — connection-failure handling tested.

**Evidence reference:** `database_failure_test.log`, containing the output of the simulated database-failure test.

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
5. The database-failure test used a mock object to simulate a MySQL connection error. Separately, a direct MySQL connection test succeeded; its result is saved in `database_connection_test.log`.
6. The authorization, simulated database-failure, and direct database-connection results are saved in `authorization_test.log`, `database_failure_test.log`, and `database_connection_test.log`. Screenshots for the first three user-confirmed scenarios are now saved in `evidence/`; database-query evidence for those scenarios was not retained.
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

**Illustrative rework assumption:** For planning only, assume 20% of requests require 10 additional minutes of rework. Expected rework effort per request = 0.20 × 10 = 2 minutes. The illustrative 12-minute baseline therefore assumes 10 minutes of initial handling and follow-up plus 2 expected rework minutes. This is an assumption, not a measured college result.

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

The normal submission, missing-information, and duplicate-submission results are based on user confirmation. The authorization-function test and simulated database-failure test were executed and their terminal results were saved. A separate direct MySQL connection test also succeeded. These results do not establish that the complete application has been tested end to end.

The current evidence does not establish that the identified workflow problem is widespread, that the system is production-ready, or that it produces a specific amount of time savings. The preliminary estimate of six minutes per submission is illustrative and requires validation through timed testing.

Further investigation, retained test evidence, and measured processing times are needed before making claims about actual workflow improvements.

## 23 October 2026 — Screenshots retained

Three screenshots were added to the repository under `evidence/`:

- `test1_normal_submission.png` — normal submission scenario.
- `test2_missing_information.png` — missing-information scenario.
- `test3_duplicate_submission.png` — duplicate-submission scenario.

The screenshots supplement the previously recorded user-confirmed results. No database-query evidence was retained for these three scenarios, so the screenshots should not be treated as independent proof of database contents or complete end-to-end behavior. Authorization and simulated database-failure results remain documented in their respective test logs; a separate direct MySQL connection test also succeeded.

**Remaining limitations:** The complete application login and review workflow has not been independently verified end to end. Time savings and process-volume figures remain illustrative estimates, not measured college-wide results.
## Final evidence-status clarification — 24 October 2026

- Actual college process independently verified: No.
- Permission-based operational observation claimed: No.
- Faculty or process-owner interview claimed: No.
- Actual operational sample size: Zero verified requests.
- Evidence available: Proposed workflow, documented prototype tests,
  synthetic test cases, and explicitly illustrative time calculations.
- Limitation: Prototype tests do not establish that the existing
  college process has the identified problems.
- Next verification step: Obtain permission from a suitable process
  owner and confirm the current workflow, request volume, handling
  time, exceptions, and approval responsibilities.
- Privacy boundary: Do not collect or publish personal identifiers,
  credentials, private messages, or confidential college records.

The time-saving and break-even figures are planning assumptions.
They must not be reported as measured institutional results.
## Final Evidence-Status Clarification — 24 October 2026

### Investigation Status

- Actual college process independently verified: No.
- Permission-based operational observation documented: No.
- Faculty or process-owner interview documented: No.
- Actual operational sample size: Zero independently verified requests.
- Evidence available: Proposed workflow diagram, documented prototype tests, synthetic test cases, and illustrative time calculations.

### Evidence Limitations

The prototype tests demonstrate the behavior of the tested features under the documented conditions. They do not establish that the existing college process has the identified problems or that the proposed workflow would produce the estimated savings in actual operations.

The existing-process description is a hypothetical walkthrough. No unverified observation, interview, request count, or processing time is presented as a measured fact.

### Next Verification Step

If permission becomes available, request a voluntary discussion or walkthrough with an appropriate process owner. Confirm the current steps, responsibilities, request volume, handling time, exceptions, and approval procedures. Record only permitted, non-identifying information.

If access is unavailable or declined, retain the hypothetical designation and state this limitation in the final report.

### Privacy and Safety

Use synthetic data for demonstrations and tests. Do not collect or publish student identifiers, staff names, marks, fees, signatures, credentials, private messages, or confidential college records.

### Time-Saving Estimates

The proposed six-minute saving per request and the monthly scenarios are illustrative calculations, not measured institutional results. Implementation effort, maintenance costs, request volume, and actual time savings remain unverified.

## Dated Evidence and Verification Addendum

**Documentation/test record date:** 2026-10-24
**Scope:** Local prototype and synthetic test evidence only.

| Evidence item | Recorded result | What it supports | What it does not establish |
|---|---|---|---|
| Runtime authorization script (`test_authorization_runtime.py`) | Command exited with code 0 on 2026-10-24 | The script completed successfully | Real institutional authorization policy or live-system security |
| Database failure script (`test_database_failure.py`) | Command exited with code 0 on 2026-10-24 | The scripted failure test completed successfully | Recovery from an actual production database outage |
| Task 2 exercise verifier | All 14 displayed checks passed on 2026-10-24 | The listed logic, synthetic SQL, scheduling and arithmetic checks | Training or validation of an ML model |
| Git whitespace check (`git diff --check`) | No output; command chain continued | No whitespace errors were reported by that check | Content correctness or assignment completeness |
| Normal, missing-information and duplicate-request cases | Existing screenshots/user-confirmed prototype outcomes are documented in the test-case/evidence materials | Illustrative prototype behavior as recorded | Independent database-state verification or real college operation |
| Actual college process | Zero independently verified operational requests; no completed interview, permission-based operational observation or independently verified official process document is claimed | Explicit access limitation | Any claim that the hypothetical process is the actual ICFAI process |

The command exit codes and check results above were reported from the local terminal. Screenshot capture dates and independent database-query evidence are not inferred where they have not been recorded. The request volume, current effort, rework rate, proposed effort and break-even calculations in the report are planning assumptions, not measured observations.

Future evidence must record the date, method, synthetic/authorized sample size, result, and limitations. If access is refused, preserve the hypothetical walkthrough and do not invent interviews or observations.
