# SkillBridge AI
## Task 1: Workflow Testing

### 1. Objective

Evaluate the proposed project submission and review workflow using five scenarios and synthetic project data. The scenarios cover normal submission, missing information, duplicate submissions, unauthorized access, and database connection failure.

The tests were conducted against the local prototype and supporting test scripts. The results distinguish user-confirmed behavior, executed tests, and behavior that remains unverified.

---

### 2. Test Case 1: Normal Submission

**Scenario:** A student submits a project with all required information.

**Input:** A valid project title, subject, description, and report or repository link.

**Expected Result:**
- The submission is saved successfully.
- A unique reference number is generated.
- The submission receives the status `SUBMITTED`.
- The assigned reviewer can access the submission.

**Actual Result:** The user confirmed that normal project submission works.

**Status:** PASS — based on user testing and confirmation.

**Evidence available:** Screenshot retained at `evidence/test1_normal_submission.png`. No database-query evidence was retained.

**Recovery:** If saving fails, display an error and allow the student to retry safely. Before retrying, check whether the original submission was saved to avoid creating a duplicate.

**Remaining limitation:** The complete submission and reviewer-access flow has not been independently verified end to end.

---

### 3. Test Case 2: Missing Information

**Scenario:** A student submits a project without a required field.

**Input:** A project with a missing title or subject.

**Expected Result:**
- The system identifies the missing field.
- The incomplete submission is not accepted as complete.
- The student receives a clear validation message.

**Actual Result:** The user confirmed that required-field validation works.

**Status:** PASS — based on user testing and confirmation.

**Evidence available:** Screenshot retained at `evidence/test2_missing_information.png`. No database-query evidence was retained.

**Recovery:** The student completes the missing information and submits the project again.

**Remaining limitation:** The screenshot and user confirmation do not independently establish every aspect of the application's validation behavior.

---

### 4. Test Case 3: Duplicate Submission

**Scenario:** A student attempts to submit the same project twice.

**Input:** The same synthetic submission is entered twice.

**Expected Result:**
- The system identifies a possible duplicate using an appropriate rule.
- The student receives a warning.
- The system avoids creating an unintended duplicate record.

**Actual Result:** The user confirmed that duplicate detection works.

**Status:** PASS — based on user testing and confirmation.

**Evidence available:** Screenshot retained at `evidence/test3_duplicate_submission.png`. No database-query evidence was retained.

**Recovery:** The student can open the existing submission or follow an explicitly supported process for submitting a legitimate new version.

**Remaining limitation:** The database records were not independently inspected to verify duplicate prevention.

---

### 5. Test Case 4: Unauthorized Request

**Scenario:** A student attempts to access a faculty-only review function.

**Input:** Simulated student, faculty, and unauthenticated user sessions.

**Expected Result:**
- Unauthorized actions are denied.
- Faculty users are allowed to continue.
- Unauthenticated users are denied access to the restricted action.

**Actual Result:** The runtime authorization test executed the `require_role()` function from `app.py` using simulated session states.

The following checks passed:

1. A student was rejected from faculty-only actions.
2. A faculty user was allowed to continue.
3. An unauthenticated user was rejected.

**Status:** PASS — authorization-function tests passed.

**Evidence:** Terminal output from `python test_authorization_runtime.py`.

**Recovery:** The user returns to the permitted dashboard. An authorized reviewer performs review actions through the application's permitted workflow.

**Remaining limitation:** The test uses simulated session states. The complete login flow, browser-level behavior, and actual database review operation have not been tested end to end.

---

### 6. Test Case 5: Database Connection Failure

**Scenario:** The application encounters a database connection error.

**Input:** The standalone test `test_database_failure.py` simulates a MySQL connection error using a mock object.

**Expected Result:**
- The simulated database connection error is detected.
- The test reports that the simulated failure was handled.
- The test does not treat a failed connection as proof that a submission was saved.

**Actual Result:** Running `python test_database_failure.py` produced the following output:

- `TEST PASSED: Database connection failure was detected.`
- `TEST PASSED: The simulated failure was handled.`

**Status:** PASS — the simulated database error detection test executed successfully.

**Evidence:** Terminal output from `python test_database_failure.py`.

**Recovery:** Check the database service and configuration, restore connectivity, and verify whether the original operation succeeded before retrying it.

**Remaining limitation:** This standalone test uses a mock error. It does not independently verify application behavior during a real database outage, transaction failure, or data-recovery operation.

---

### 7. Decision Responsibility and Recovery Matrix

| Scenario | Expected system response | Responsible person or role | Recovery or next step |
|---|---|---|---|
| Normal submission | Validate required fields, save the submission, and assign a reference number. | Student submits; authorized faculty member reviews. | If saving fails, display an error. Check whether the original submission was saved before retrying. |
| Missing information | Identify missing fields and prevent incomplete submission. | Student corrects the information. | Complete the required fields and submit again. |
| Duplicate submission | Flag a possible duplicate and prevent an unintended second record. | Student clarifies whether the new submission is intentional; an authorized reviewer resolves ambiguity if required by policy. | Open the existing record or follow an explicitly supported new-submission process. |
| Unauthorized request | Deny the restricted action without changing the review record. | The application enforces permissions; an authorized administrator investigates repeated access problems if necessary. | Return to the permitted dashboard or request access through an approved process. |
| Database connection failure | Detect the failure and avoid reporting an unsuccessful save as successful. | Designated technical support restores service; the student checks submission status before retrying. | Restore connectivity, verify the original operation's outcome, and retry safely. |

**Approval boundary:** Students may submit and correct their own project information. Only authorized faculty members may perform faculty-only review actions. Technical support may restore service but must not make academic review decisions.

**Audit record:** Where implemented, record the submission reference, timestamp, action, authorized actor role, previous and new status, and success or failure outcome. Do not record passwords, authentication tokens, or unnecessary personal information.

**Fallback:** If the application is unavailable, students should follow the institution's existing approved submission procedure. This is a proposed fallback and must not be represented as an existing official policy without verification.

**Testing limitation:** The matrix describes intended behavior. Each behavior must be tested before it can be claimed as implemented. Safe retry, audit-record creation, and recovery from a real database outage have not been independently demonstrated by the tests described here.

---

### 8. Testing Record Summary

| Test | Scenario | Result | Evidence |
|---|---|---|---|
| 1 | Normal submission | PASS — user-confirmed | `evidence/test1_normal_submission.png`; no database-query evidence |
| 2 | Missing information | PASS — user-confirmed | `evidence/test2_missing_information.png`; no database-query evidence |
| 3 | Duplicate submission | PASS — user-confirmed | `evidence/test3_duplicate_submission.png`; no database-query evidence |
| 4 | Unauthorized request | PASS — authorization-function test | Terminal output from `python test_authorization_runtime.py` |
| 5 | Database connection failure | PASS — mocked connection-failure test | Terminal output from `python test_database_failure.py`; real outage recovery not verified |

### 9. Test Environment

- **Project:** SkillBridge AI
- **Environment:** Local prototype
- **Data:** Synthetic project data and simulated test sessions
- **Testing period:** October 2026
- **Testing scope:** User-confirmed submission behavior, authorization-function checks, and mocked database connection-failure handling

### 10. Overall Testing Summary

All five required scenarios are documented.

Tests 1–3 are marked PASS based on user testing and confirmation, with screenshots retained in the repository. Test 4 has runtime authorization-function test output, and Test 5 has output from a mocked database connection-failure test.

These results do not establish that the complete application has passed end-to-end testing. The complete login flow, database review operation, audit-record creation, safe retry behavior, and recovery from a real database outage remain unverified.

### 11. Evidence and Integrity Note

A test should be described as independently evidenced only when its corresponding screenshot, log, or database result has been retained and can be inspected. User confirmation, executed test output, and proposed but untested behavior must remain clearly distinguished.

The test results describe the local prototype and its supporting test scripts. They do not establish that SkillBridge AI has been deployed or approved by ICFAI, or that the proposed workflow has improved the institution's actual process.

## Test Coverage, Expected Recovery and Limitations Addendum

| Scenario | Expected result | Recovery | Current evidence boundary |
|---|---|---|---|
| Normal submission | Valid request is accepted and assigned a reference/status | Authorized reviewer processes it; requester checks status | Existing prototype screenshot/user-confirmed outcome; not a live college deployment |
| Missing information | Missing required fields are identified and approval does not proceed | Requester corrects fields and resubmits | Synthetic scenario |
| Duplicate submission | Matching request is flagged to prevent silent duplicate processing | Show existing reference; process owner resolves ambiguous matches | Synthetic scenario; no real duplicate-rate measurement |
| Unauthorized request | Unauthenticated/unauthorized action is denied | Sign in with permitted role or escalate to the authorized owner | Runtime authorization script completed with exit code 0; no claim about real institutional policy |
| Database or step failure | Failure is visible and is not reported as successful completion | Retry safely or escalate; verify persistence before retrying | Database failure script completed with exit code 0; mocked/scripted failure, not a real outage |

**Verification date:** 2026-10-24. The local runtime authorization and database-failure scripts both completed with exit code 0 when run in the terminal. The Task 2 exercise verifier separately reported 14 passing checks; it is not a Task 1 test. A successful script exit is evidence of script completion, not proof that every live-system condition has been tested.
