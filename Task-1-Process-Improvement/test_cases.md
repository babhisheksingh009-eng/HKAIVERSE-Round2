# SkillBridge AI
## Task 1: Workflow Testing

### Objective
Test the proposed project submission and review workflow using five scenarios. Testing is performed using synthetic project data and test accounts in the prototype.

---

### Test Case 1: Normal Submission

**Scenario:** A student submits a project with all required information.

**Input:** Valid project title, subject, description, and report or repository link.

**Expected Result:**
- The submission is saved successfully.
- A unique reference number is generated.
- The submission receives the status `SUBMITTED`.
- The assigned reviewer can access the submission.

**Actual Result:** The user confirmed that normal project submission works.

**Status:** PASS — based on user testing and confirmation.

**Evidence available:** User confirmation that normal submission works. No screenshot was retained for this test.

**Recovery:** If saving fails, display an error and allow the student to retry safely.

---

### Test Case 2: Missing Information

**Scenario:** A student submits a project without a required field.

**Input:** A project with a missing title or subject.

**Expected Result:**
- The system identifies the missing field.
- The submission is not accepted as complete.
- The student receives a clear validation message.

**Actual Result:** The user confirmed that required-field validation works.

**Status:** PASS — based on user testing and confirmation.

**Evidence available:** User confirmation that required-field validation works. No screenshot was retained for this test.

**Recovery:** The student completes the missing information and resubmits.

---

### Test Case 3: Duplicate Submission

**Scenario:** A student attempts to submit the same project twice.

**Input:** The same synthetic submission is entered twice.

**Expected Result:**
- The system identifies a possible duplicate using an appropriate rule.
- The student receives a warning.
- The system avoids creating an unintended duplicate record.

**Actual Result:** The user confirmed that duplicate detection works.

**Status:** PASS — based on user testing and confirmation.

**Evidence available:** User confirmation that duplicate detection works. No screenshot or database query result was retained for this test.

**Recovery:** The student can open the existing submission or explicitly confirm a legitimate new submission, if supported by the application.

---

### Test Case 4: Unauthorized Request

**Scenario:** A student attempts to access a faculty-only review function.

**Input:** Simulated student, faculty, and unauthenticated user sessions.

**Expected Result:**
- The system denies unauthorized actions.
- Faculty users are allowed to continue.
- Unauthorized users cannot pass the faculty-role check.

**Actual Result:**
The runtime authorization test executed the actual `require_role()` function from `app.py` using simulated session states.

All three test cases passed:
1. A student was rejected from faculty-only actions.
2. A faculty user was allowed to continue.
3. An unauthenticated user was rejected.

**Status:** PASS — authorization-function tests passed.

**Evidence:** Terminal output from `python test_authorization_runtime.py`.

**Limitation:** The test uses simulated session states. The complete login flow, browser-level behavior, and actual database review operation have not been tested end to end.

**Recovery:** The user can return to the student dashboard. An authorized reviewer can perform the review action through the application's permitted workflow.

---

### Test Case 5: Database Connection Failure

**Scenario:** The application encounters a database connection error.

**Input:** The standalone test `test_database_failure.py` simulates a MySQL connection error using a mock object.

**Expected Result:**
- The simulated database connection error is detected.
- The test reports that the simulated failure was handled.

**Actual Result:** Running `python test_database_failure.py` produced:
- `TEST PASSED: Database connection failure was detected.`
- `TEST PASSED: The simulated failure was handled.`

**Status:** PASS — simulated database error detection test executed successfully.

**Evidence:** The terminal output from `python test_database_failure.py`.

**Limitation:** This standalone test uses a mock error. It does not independently verify the application's behavior during a real database outage, nor does it test every possible database or transaction failure.

**Recovery:** Check the database service and configuration, restore connectivity, and retry the operation safely.
---

## Testing Record Summary

| Test | Scenario | Result | Evidence |
|---|---|---|---|
| 1 | Normal submission | PASS — user-confirmed | User confirmation; screenshot not retained |
| 2 | Missing information | PASS — user-confirmed | User confirmation; screenshot not retained |
| 3 | Duplicate submission | PASS — user-confirmed | User confirmation; screenshot/database evidence not retained |
| 4 | Unauthorized request | PASS — authorization-function test | Runtime test output |
| 5 | Database connection failure | PASS — connection-failure handling | Application or terminal error output |

### Test Environment
- **Project:** SkillBridge AI
- **Environment:** Local prototype
- **Data:** Synthetic project data and test accounts
- **Testing period:** October 2026

### Overall Testing Summary

The five required scenarios have been reported as working or have supporting test results. The normal submission, missing-information, and duplicate-submission results are based on user confirmation. The authorization-function test and database connection-failure test have been executed and have supporting results.

The complete login flow and actual database review operation remain unverified end to end. The database failure test covers a connection failure, not every possible database error. Evidence screenshots and logs should be retained with the final submission.

### Evidence and Integrity Note

A test should be marked as fully evidenced only when its corresponding screenshot, log, or database result has been saved. User confirmation and executed test output should be distinguished from independently retained evidence.
