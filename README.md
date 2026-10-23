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

The authorization and database-failure test scripts were run individually. Their documented results and limitations are in the test and evidence files. The mocked database-failure test does not establish that a real database outage was tested end to end.

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

- **GitHub repository:** Add the final repository URL after publishing.
- **Release:** Add the release URL after creating a release.
- **Final commit:** Add the commit URL after the final commit.

## Personal Contribution

Describe only the analysis, implementation, testing, documentation, and verification work personally completed for these projects.