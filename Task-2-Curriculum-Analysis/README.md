# Task 2: CSE Curriculum Analysis

## Objective

This project presents a preliminary review of computer science courses, practical learning improvements, and skills mentioned in selected entry-level technology job descriptions. It includes an interactive dashboard for exploring courses and calculating selected-course credit subtotals.

**Important:** The curriculum data is provisional. The exact official syllabus and credit structure applicable to the 2023 B.Tech CSE admission batch at IFHE/IcfaiTech Hyderabad have not yet been confirmed.

## Project Structure

- `data/curriculum.csv` — proposed course list, recommendations, and verification notes.
- `data/curriculum_before_verification.csv` — backup of the curriculum dataset before verification-related changes.
- `analysis/curriculum_review.md` — preliminary course review and recommendations.
- `analysis/industry_skill_gap.md` — comparison of skills identified in selected job descriptions.
- `analysis/revised_curriculum.md` — proposed practical learning improvements and curriculum changes.
- `exercises/ai_assisted_exercises.md` — AI-assisted exercises, test cases, results, and limitations.
- `sources/source_log.csv` — source URLs, access dates, and verification notes.
- `app.py` — interactive Streamlit dashboard.
- `requirements.txt` — Python dependencies.

## Requirements

- Python 3.10 or later recommended.
- pip.
- A terminal and web browser.

## Setup

From this directory, create and activate a virtual environment if you do not already have one:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Dashboard

Start the application:

```bash
streamlit run app.py
```

Open the local address displayed in the terminal.

The dashboard supports:

- Exploring and searching the proposed course list.
- Filtering courses by proposed decision.
- Comparing selected courses.
- Calculating the combined credits of selected entries.
- Reviewing next steps for curriculum verification.

## Credit Calculation and Verification

The displayed 71-credit subtotal is the sum of numeric credits in the current listed-course dataset. It is **not** the official total degree-credit requirement.

Provisional proposals with `VERIFY` credits are excluded from the numeric credit calculation. Course titles, semester assignments, credits, equivalencies, and regulations must be checked against the official syllabus applicable to the 2023 admission batch before definitive conclusions are made.

Official references consulted:

- IFHE/IcfaiTech B.Tech Programme Structure: https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure
- IFHE/IcfaiTech Syllabus Archive: https://naac2020.ifheindia.org/1.1.3Syllabus%20IcfaiTech.html

The exact applicability of the published structure to the 2023 admission batch remains unconfirmed.

## Industry Skill-Gap Analysis

The industry analysis uses selected software engineering and systems development job-description sources. The sample is limited and does not represent the entire technology job market. Locations, posting dates, and the continuing availability of listings should be checked before drawing broader conclusions.

Refer to `analysis/industry_skill_gap.md` and `sources/source_log.csv` for the documented evidence and limitations.

## AI-Assisted Exercise Verification

The exercise report documents the prompts, AI tool disclosure, test inputs, expected or observed results, and verification methods for five subject areas.

Passing a logic or arithmetic check does not necessarily establish that a complete application or real machine-learning model works. The limitations of each exercise are recorded in the report.

## Limitations

- This is a preliminary student analysis, not an official university curriculum revision.
- The exact 2023-batch syllabus and regulations remain to be verified.
- Proposed course decisions require comparison with existing content, prerequisites, credit rules, and academic requirements.
- Job-description analysis uses a limited sample.
- AI-generated material requires independent verification.
- Proposed additions and reductions require appropriate academic review and approval.

## Personal Contribution

This project combines curriculum-data organization, source documentation, industry skill-gap analysis, AI-assisted exercise verification, and Streamlit dashboard development.

Only work personally completed and verified should be claimed as an individual contribution.

## Final Checklist

- [ ] Verify the official syllabus applicable to the 2023 admission batch.
- [ ] Confirm course titles, semester assignments, credits, and regulations.
- [ ] Recheck the dashboard and credit calculations.
- [ ] Review the industry sources and access dates.
- [ ] Confirm that the AI-assisted exercise report accurately describes the tests performed.
- [ ] Check that no credentials, environment files, or local databases are included in the repository.