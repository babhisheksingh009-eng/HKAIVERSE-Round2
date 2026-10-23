import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CSE Curriculum Analysis", layout="wide")

st.title("CSE Curriculum Analysis Dashboard")
st.caption("AI-assisted curriculum review and industry skill-gap analysis.")

# Load data
data_path = Path(__file__).parent / "data" / "curriculum.csv"
df = pd.read_csv(data_path, dtype=str).fillna("")

# Identify unverified entries
needs_verification = (
    df["verification_status"].str.strip().str.lower().ne("verified")
    | df["semester"].str.upper().eq("VERIFY")
    | df["credits"].str.upper().eq("VERIFY")
)

# Only rows with numeric credits can contribute to the subtotal
numeric_credits = pd.to_numeric(df["credits"], errors="coerce")
existing_course_rows = df["semester"].str.upper().ne("VERIFY")
listed_credit_subtotal = numeric_credits[existing_course_rows].sum()

a, b, c = st.columns(3)
a.metric("Course Entries", len(df))
b.metric("Entries Pending Verification", int(needs_verification.sum()))
c.metric("Listed-Course Credit Subtotal", f"{listed_credit_subtotal:g}")

st.warning(
    "The credit subtotal is based on listed entries only. "
    "Course details and credits still require verification against the "
    "official syllabus. This is NOT the official total degree credit."
)

# Filter
st.subheader("Explore Curriculum")
choices = ["All"] + sorted(df["proposed_decision"].unique().tolist())
choice = st.selectbox("Filter by proposed decision", choices)

view = df if choice == "All" else df[df["proposed_decision"] == choice]

query = st.text_input("Search course titles")
if query:
    view = view[
        view["course_title"].str.contains(query, case=False, na=False)
    ]

st.dataframe(view, use_container_width=True, hide_index=True)
st.caption(f"Showing {len(view)} of {len(df)} entries.")

# Course comparison
st.subheader("Compare Courses")
course_names = df["course_title"].tolist()
selected_courses = st.multiselect(
    "Choose courses to compare",
    options=course_names,
    default=course_names[:3]
)

comparison = df[df["course_title"].isin(selected_courses)].copy()
st.dataframe(
    comparison[
        [
            "course_title",
            "semester",
            "credits",
            "proposed_decision",
            "recommendation",
            "verification_status",
        ]
    ],
    use_container_width=True,
    hide_index=True,
)

# Credit calculator
st.subheader("Credit Subtotal Calculator")
st.write(
    "Select listed courses to calculate their combined numeric credits. "
    "Provisional entries with VERIFY credits are excluded."
)

credit_courses = st.multiselect(
    "Choose courses for the subtotal",
    options=df.loc[
        numeric_credits.notna() & existing_course_rows, "course_title"
    ].tolist(),
    key="credit_courses",
)

selected_rows = df[df["course_title"].isin(credit_courses)]
selected_values = pd.to_numeric(selected_rows["credits"], errors="coerce")
subtotal = selected_values.sum()

st.metric("Selected-Course Credit Subtotal", f"{subtotal:g}")
st.caption(
    "This calculator sums the credits entered in this dataset. "
    "It does not verify the credits or represent the total degree requirements."
)

# Decision guide
st.subheader("Curriculum Decision Guide")
decision_guide = {
    "KEEP": "Retain the course and its essential learning outcomes.",
    "UPDATE": "Improve existing content, practical exercises, tools, or assessments.",
    "REDUCE": "Reduce overlapping content only after confirming duplication in the official syllabus.",
    "ADD": "Introduce a new topic or learning module only when evidence supports a gap and regulations permit it.",
}
for decision, explanation in decision_guide.items():
    st.markdown(f"**{decision}:** {explanation}")

# Next actions
st.subheader("Next Actions")
st.write("1. Confirm course details against the applicable official syllabus.")
st.write("2. Validate semester and credit information.")
st.write("3. Verify job-posting evidence and access dates.")
st.write("4. Check proposed changes against existing content and prerequisites.")
st.write("5. Review credit balance and applicable academic regulations.")
