# SkillBridge AI
## Task 1: Proposed Workflow

### 1. Purpose

SkillBridge AI is a student-designed prototype intended to organize academic project submissions, faculty reviews, and feedback.

The proposed workflow aims to improve submission tracking, information validation, role-based access, and visibility of review status.

This is a prototype and is not an official IFHE system.

### 2. Existing Workflow

Based on personal experience, academic project submissions may follow these steps:

1. A student completes an academic project.
2. The student submits the project through an online form, website, or directly to a faculty member.
3. The relevant faculty member receives and reviews the project.
4. The faculty member provides feedback and awards marks where applicable.
5. The student checks the feedback or contacts the faculty member for clarification.

**Limitation:** This is an initial process model based on personal experience. The exact institutional workflow and the extent of any tracking problems have not been independently verified.

### 3. Proposed Improved Workflow

#### Step 1: Student Login

The student signs in using an authorized account.

The application identifies the user's role and provides access to the appropriate dashboard.

#### Step 2: Project Submission

The student provides the required project information:

- Project title
- Subject
- Project description
- Report or repository link, where required

#### Step 3: Input Validation

The application checks whether the required information is present.

If a required field is missing, the application displays a validation message and asks the student to correct the information.

#### Step 4: Duplicate Detection

The application checks for potential duplicate submissions according to its configured detection rules.

If a duplicate is detected, the student receives an appropriate warning or rejection.

The precise duplicate-detection rule should be documented according to the implementation.

#### Step 5: Submission Registration

After validation, the application records the submission in the database and generates a unique reference number.

The initial submission status is `SUBMITTED`.

If saving fails, the application must not report the submission as successful.

#### Step 6: Faculty Review

An authorized faculty member accesses the submissions available through the faculty workflow.

The faculty member reviews the project and records the review outcome.

Faculty-only actions must be protected by role-based authorization checks.

#### Step 7: Status and Feedback Update

The faculty member updates the review status and provides feedback when appropriate.

Possible workflow statuses include:

- `SUBMITTED`
- `UNDER_REVIEW`
- `CHANGES_REQUIRED`
- `APPROVED`

These are proposed workflow states. Only statuses supported by the actual application should be described as implemented features.

#### Step 8: Student Progress Check

The student accesses the student dashboard to view their own submissions and the available review information.

Students must not be permitted to change faculty-only review decisions.

#### Step 9: Exception Handling

If an error occurs, the application displays an understandable message and provides a safe recovery path where possible.

Examples include missing information, duplicate submissions, unauthorized actions, and database connection failures.

#### Proposed Status Transitions

| Current status | Action | Next status | Responsible role |
|---|---|---|---|
| Not submitted | Student submits complete information | SUBMITTED | Student |
| SUBMITTED | Faculty begins reviewing | UNDER_REVIEW | Faculty reviewer |
| UNDER_REVIEW | More information is needed | CHANGES_REQUIRED | Faculty reviewer |
| CHANGES_REQUIRED | Student submits the requested changes | SUBMITTED | Student |
| UNDER_REVIEW | Faculty accepts the project | APPROVED | Faculty reviewer |

These transitions describe the proposed workflow. They must not be presented as implemented functionality unless they have been verified in the prototype.

### 4. Roles and Responsibilities

#### Student

- Submit project information.
- Correct incomplete submissions.
- View their own submissions.
- Check available status information and feedback.

#### Faculty Reviewer

- Access submissions through the authorized faculty workflow.
- Review project deliverables.
- Update permitted review statuses.
- Provide feedback.

#### Authorized Administrator — Proposed Future Role

- Manage reviewer assignment rules.
- Resolve unassigned submissions.
- Support system maintenance and recovery.

**Implementation note:** The administrator responsibilities are proposed design elements and must not be presented as implemented capabilities unless an administrator role has actually been developed and tested.

**Approval boundary:** Students may submit projects and respond to requested changes, but only authorized faculty reviewers may record official review decisions. Any exceptional administrative override must follow an approved policy and be logged.

### 5. Workflow Exceptions and Recovery

| Exception | Expected system response | Recovery |
|---|---|---|
| Missing required information | Display a validation message | Student corrects the information |
| Potential duplicate submission | Apply the configured duplicate-detection rule | Student checks the existing submission or follows the permitted resubmission process |
| Unauthorized review action | Reject the action | User returns to the appropriate dashboard |
| Database connection failure | Display a readable error and stop normal database-dependent processing | Restore the connection and retry safely |
| Submission not yet reviewed | Retain an appropriate pending status | Authorized faculty member reviews the submission |
| No reviewer assigned | Flag for authorized follow-up, if assignment functionality is implemented | Authorized personnel assign a reviewer |

These are the intended responses. Each implemented behavior should be verified through testing.

### 6. AI Assistance

AI assistance is a possible future extension of SkillBridge AI.

Potential uses include:

- Suggesting improvements to project descriptions.
- Helping organize project documentation.
- Drafting preliminary feedback for faculty review.

Any AI-generated suggestions must be checked by a faculty member before use.

AI should not independently award official marks, approve academic projects, or make final academic decisions.

**Current scope:** AI-assisted feedback is a proposed extension unless the functionality has actually been implemented and tested in the prototype.

### 7. Expected Benefits

The proposed workflow aims to provide:

- A consistent record of project submissions.
- Unique submission reference numbers.
- Better visibility of submission and review status.
- Feedback associated with the relevant submission.
- Clearer separation between student and faculty actions.
- Validation of required information.
- More understandable handling of database connection failures.

These are expected benefits, not measured results.

### 8. Evaluation Plan

The proposed workflow should be evaluated using the following measures:

1. Submission completion time.
2. Time spent checking submission status.
3. Review turnaround time.
4. Number of incomplete submissions.
5. Number of unintended duplicate records.
6. Net time saved after accounting for additional review and support effort.

Where possible, collect baseline measurements of the existing process and compare them with measurements from the prototype.

Net time saved should be calculated only when sufficient timing data is available.

### 9. Limitations and Future Work

- The existing institutional workflow has not been independently verified.
- The frequency and impact of the potential problems have not been measured.
- The prototype is not an official IFHE system.
- The authorization-function test uses simulated session states and does not verify the complete application end to end.
- Database connection-failure testing does not cover every possible database error.
- Automatic reviewer assignment and AI-assisted feedback should be treated as proposed extensions unless implemented and tested.
- Time savings and workflow improvements have not yet been established through measured results.

A real deployment would require institutional approval, secure authentication, appropriate access controls, privacy protection, database backup and recovery procedures, and operational support.

### 10. Conclusion

SkillBridge AI proposes a structured approach to academic project submission and review through submission registration, input validation, status tracking, faculty feedback, role-based authorization, and exception handling.

The prototype provides a basis for evaluating the proposed workflow. Further investigation, documented evidence, end-to-end testing, and measured comparisons are necessary before claiming institution-wide benefits or quantified time savings.