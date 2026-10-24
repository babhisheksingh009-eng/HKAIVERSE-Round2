# HKAIVERSE Round 2 Assignment

This repository contains two projects prepared for the HKAIVERSE Round 2 assignment.

## Task 1: Process Improvement

**Folder:** `Task-1-Process-Improvement/`

This project investigates a review workflow and proposes improvements to role-based authorization, error handling, and process reliability.

Key files:
- `app.py` — application.
- `process_investigation.md` — process investigation.
- `proposed_workflow.md` — proposed improved workflow.
- `test_cases.md` — test cases and results.
- `evidence_log.md` — evidence and verification notes.
- `requirements.txt` — Python dependencies.

### Run Task 1

Follow the setup instructions in the Task 1 folder. Keep local environment variables and database files out of version control.

### Test results

- The runtime authorization test passed for simulated student, faculty, and unauthenticated sessions.
- The simulated database-failure test detected a mocked MySQL connection error.
- A separate direct MySQL connection test succeeded; its output is saved in `database_connection_test.log`.
- Screenshots for the normal submission, missing-information validation, and duplicate-submission scenarios are retained in `Task-1-Process-Improvement/evidence/`. These screenshots supplement the user's test observations; no database-query evidence was retained for these three cases. The full login and database workflow has not been independently verified end to end.

These results do not establish that the complete application was tested end to end. See `test_cases.md` and `evidence_log.md` for evidence and limitations.

## Task 2: CSE Curriculum Analysis

**Folder:** `Task-2-Curriculum-Analysis/`

This project provides a preliminary curriculum review, industry skill-gap analysis, AI-assisted exercise verification, and an interactive Streamlit dashboard.

Key features:
- Course search, filtering, and comparison.
- Selected-course credit subtotal calculator.
- Proposed KEEP, UPDATE, REDUCE, and ADD decisions.
- Industry skill-gap analysis using selected job descriptions.
- Documentation of AI-assisted exercises and verification limitations.

### Run Task 2

From the Task 2 folder:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Important Verification Limitations

The curriculum dataset is provisional. The exact official syllabus and credit structure applicable to the 2023 B.Tech Computer Science and Engineering admission batch at IFHE/IcfaiTech Hyderabad have not been confirmed.

The listed 71-credit subtotal is not the official total degree-credit requirement. Course titles, semester assignments, credits, and regulations must be verified against the applicable official syllabus.

The industry analysis uses a limited sample of job descriptions. AI-assisted exercise results are documented with their test methods and limitations.

These projects are student proposals and analyses, not official university policy changes.

## Repository Safety

Environment files, credentials, local databases, virtual environments, and other generated files should remain excluded from version control. Only appropriate project source code, documentation, and evidence should be published.

## Submission Details

- **GitHub repository:** https://github.com/babhisheksingh009-eng/HKAIVERSE-Round2
- **Release:** https://github.com/babhisheksingh009-eng/HKAIVERSE-Round2/releases/tag/v1.0.0
- **Project commit:** https://github.com/babhisheksingh009-eng/HKAIVERSE-Round2/commit/ff582b8cd7a01caa371d61fd9eb21c0e5196e185

## Personal Contribution

My contribution includes preparing project documentation, developing and testing project components, analyzing the proposed workflow and curriculum, and recording verification results and limitations. The task-specific reports identify assumptions and areas that still require independent verification.
