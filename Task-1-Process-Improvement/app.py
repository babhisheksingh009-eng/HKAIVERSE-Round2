import hashlib
import hmac
import os
from datetime import datetime
from urllib.parse import urlparse

import mysql.connector
from mysql.connector import Error as MySQLError
import pandas as pd
import streamlit as st
from dotenv import load_dotenv


# ==================================================
# 1. CONFIGURATION
# ==================================================

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "database": os.getenv("DB_NAME", "skillbridge_ai"),
    "user": os.getenv("DB_USER", "skillbridge_app"),
    "password": os.getenv("DB_PASSWORD", ""),
    "connection_timeout": 10,
}

STATUSES = [
    "SUBMITTED",
    "UNDER_REVIEW",
    "CHANGES_REQUIRED",
    "APPROVED",
]

SUBJECTS = [
    "Computer Programming",
    "Data Structures",
    "Database Management Systems",
    "Operating Systems",
    "Software Engineering",
    "Cloud Computing",
    "Deep Learning",
    "Natural Language Processing",
    "Other",
]

st.set_page_config(
    page_title="SkillBridge AI",
    page_icon="📚",
    layout="wide",
)


# ==================================================
# 2. DATABASE CONNECTION
# ==================================================

def get_connection():
    """Connect to MySQL."""

    if not DB_CONFIG["password"]:
        raise RuntimeError(
            "DB_PASSWORD is missing. Configure your .env file."
        )

    return mysql.connector.connect(**DB_CONFIG)


def initialize_database():
    """Create database tables if they do not exist."""

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(100) PRIMARY KEY,
                password_hash VARCHAR(255) NOT NULL,
                role ENUM('student', 'faculty') NOT NULL,
                created_at DATETIME NOT NULL
                    DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS submissions (
                id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                reference_id VARCHAR(30) UNIQUE,
                student_name VARCHAR(100) NOT NULL,
                title VARCHAR(150) NOT NULL,
                subject VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                project_link VARCHAR(1000) NOT NULL DEFAULT '',
                status ENUM(
                    'SUBMITTED',
                    'UNDER_REVIEW',
                    'CHANGES_REQUIRED',
                    'APPROVED'
                ) NOT NULL DEFAULT 'SUBMITTED',
                feedback TEXT NOT NULL,
                created_at DATETIME NOT NULL,
                updated_at DATETIME NOT NULL,
                owner_username VARCHAR(100) NULL,
                reviewer_username VARCHAR(100) NULL,

                CONSTRAINT fk_submission_owner
                    FOREIGN KEY (owner_username)
                    REFERENCES users(username)
                    ON UPDATE CASCADE
                    ON DELETE SET NULL,

                CONSTRAINT fk_submission_reviewer
                    FOREIGN KEY (reviewer_username)
                    REFERENCES users(username)
                    ON UPDATE CASCADE
                    ON DELETE SET NULL,

                INDEX idx_submission_owner (owner_username),
                INDEX idx_submission_status (status)
            ) ENGINE=InnoDB
        """)

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()


# ==================================================
# 3. PASSWORD SECURITY
# ==================================================

PBKDF2_ITERATIONS = 600_000


def verify_password(password, stored_hash):
    """Verify a PBKDF2-SHA256 password hash."""

    try:
        algorithm, iterations_text, salt_hex, expected_hex = (
            stored_hash.split("$", 3)
        )

        if algorithm != "pbkdf2_sha256":
            return False

        iterations = int(iterations_text)

        if not 100_000 <= iterations <= 2_000_000:
            return False

        salt = bytes.fromhex(salt_hex)
        expected_hash = bytes.fromhex(expected_hex)

        actual_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            iterations,
        )

        return hmac.compare_digest(
            actual_hash,
            expected_hash,
        )

    except (ValueError, AttributeError, TypeError):
        return False


def authenticate(username, password):
    """Authenticate a user from MySQL."""

    username = username.strip()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT username, password_hash, role
            FROM users
            WHERE username = %s
            """,
            (username,),
        )

        user = cursor.fetchone()

    finally:
        cursor.close()
        conn.close()

    if not user:
        return None

    if not verify_password(password, user["password_hash"]):
        return None

    return {
        "username": user["username"],
        "role": user["role"],
    }


# ==================================================
# 4. ROLE-BASED AUTHORIZATION
# ==================================================

def require_role(required_role):
    """Allow an operation only for the required role."""

    user = st.session_state.get("user")

    if not user:
        raise PermissionError("Please log in first.")

    if user.get("role") != required_role:
        raise PermissionError(
            f"Access denied. The {required_role} role is required."
        )

    return user


# ==================================================
# 5. CREATE PROJECT SUBMISSION
# ==================================================

def create_submission(
    username,
    student_name,
    title,
    subject,
    description,
    project_link,
):
    """Validate and save a project, rejecting duplicates."""

    user = require_role("student")

    if user["username"] != username:
        raise PermissionError(
            "You cannot submit a project for another account."
        )

    student_name = student_name.strip()
    title = title.strip()
    description = description.strip()
    project_link = project_link.strip()

    # Required field validation
    if not student_name or not title or not description:
        raise ValueError(
            "Display name, project title, and description are required."
        )

    # Length validation
    if len(student_name) > 100:
        raise ValueError(
            "Display name must be 100 characters or fewer."
        )

    if len(title) > 150:
        raise ValueError(
            "Project title must be 150 characters or fewer."
        )

    if len(description) > 5000:
        raise ValueError(
            "Description must be 5000 characters or fewer."
        )

    if len(project_link) > 1000:
        raise ValueError("Repository link is too long.")

    if subject not in SUBJECTS:
        raise ValueError("Please select a valid subject.")

    # Validate repository URL
    if project_link:
        parsed_link = urlparse(project_link)

        if (
            parsed_link.scheme not in ("http", "https")
            or not parsed_link.netloc
        ):
            raise ValueError(
                "Repository link must be a valid HTTP or HTTPS URL."
            )

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # DUPLICATE CHECK
        # Same student + same title + same repository link.
        # If the link is empty, a repeated title is also detected.

        cursor.execute(
            """
            SELECT reference_id
            FROM submissions
            WHERE owner_username = %s
              AND LOWER(TRIM(title)) = LOWER(TRIM(%s))
              AND LOWER(TRIM(project_link)) = LOWER(TRIM(%s))
            LIMIT 1
            """,
            (username, title, project_link),
        )

        existing_submission = cursor.fetchone()

        if existing_submission:
            old_reference = (
                existing_submission[0] or "existing submission"
            )

            raise ValueError(
                "Duplicate submission detected! "
                f"You already submitted this project. "
                f"Reference: {old_reference}. "
                "Please check My Submissions."
            )

        now = datetime.now().replace(microsecond=0)

        # Insert new submission
        cursor.execute(
            """
            INSERT INTO submissions (
                student_name,
                title,
                subject,
                description,
                project_link,
                status,
                feedback,
                created_at,
                updated_at,
                owner_username
            )
            VALUES (
                %s, %s, %s, %s, %s,
                'SUBMITTED', '', %s, %s, %s
            )
            """,
            (
                student_name,
                title,
                subject,
                description,
                project_link,
                now,
                now,
                username,
            ),
        )

        row_id = cursor.lastrowid

        reference_id = f"SB-{now:%Y}-{row_id:05d}"

        cursor.execute(
            """
            UPDATE submissions
            SET reference_id = %s
            WHERE id = %s
            """,
            (reference_id, row_id),
        )

        # Save changes to MySQL
        conn.commit()

        return reference_id

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()


# ==================================================
# 6. STUDENT SUBMISSIONS
# ==================================================

def get_student_submissions(username):
    """Return submissions belonging to the logged-in student."""

    user = require_role("student")

    if user["username"] != username:
        raise PermissionError(
            "You cannot view another student's projects."
        )

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
                reference_id,
                title,
                subject,
                description,
                project_link,
                status,
                feedback,
                created_at,
                updated_at
            FROM submissions
            WHERE owner_username = %s
            ORDER BY id DESC
            """,
            (username,),
        )

        rows = cursor.fetchall()

    finally:
        cursor.close()
        conn.close()

    return pd.DataFrame(rows)


# ==================================================
# 7. FACULTY SUBMISSIONS
# ==================================================

def get_faculty_submissions():
    """Return submissions to authenticated faculty."""

    require_role("faculty")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
                reference_id,
                student_name,
                owner_username,
                title,
                subject,
                description,
                project_link,
                status,
                feedback,
                created_at,
                updated_at,
                reviewer_username
            FROM submissions
            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

    finally:
        cursor.close()
        conn.close()

    return pd.DataFrame(rows)


# ==================================================
# 8. FACULTY REVIEW
# ==================================================

def update_review(reference_id, status, feedback):
    """Update submission status and faculty feedback."""

    user = require_role("faculty")

    if status not in STATUSES:
        raise ValueError("Invalid review status.")

    feedback = feedback.strip()

    if len(feedback) > 5000:
        raise ValueError(
            "Feedback must be 5000 characters or fewer."
        )

    now = datetime.now().replace(microsecond=0)

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            UPDATE submissions
            SET
                status = %s,
                feedback = %s,
                updated_at = %s,
                reviewer_username = %s
            WHERE reference_id = %s
            """,
            (
                status,
                feedback,
                now,
                user["username"],
                reference_id,
            ),
        )

        if cursor.rowcount != 1:
            raise ValueError("Submission not found.")

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()


# ==================================================
# 9. APPLICATION STARTUP
# ==================================================

if "user" not in st.session_state:
    st.session_state.user = None

st.title("📚 SkillBridge AI")

st.caption(
    "Academic Project Submission and Review Workflow"
)

try:
    initialize_database()

except (MySQLError, RuntimeError) as error:
    st.error(
        "Could not connect to MySQL or initialize the database."
    )

    st.code(str(error))

    st.info(
        "Check that MySQL is running, the skillbridge_ai "
        "database exists, and your DB_* settings in .env are correct."
    )

    st.stop()


# ==================================================
# 10. LOGIN PAGE
# ==================================================

if st.session_state.user is None:

    st.subheader("Secure Login")

    st.write(
        "Sign in with an account created using create_user.py."
    )

    with st.form("login_form"):

        username_input = st.text_input("Username")

        password_input = st.text_input(
            "Password",
            type="password",
        )

        login_clicked = st.form_submit_button("Login")

    if login_clicked:

        if not username_input.strip() or not password_input:
            st.error("Enter your username and password.")

        else:
            try:
                account = authenticate(
                    username_input,
                    password_input,
                )

                if account:
                    st.session_state.user = account
                    st.rerun()

                else:
                    st.error("Invalid username or password.")

            except (MySQLError, RuntimeError) as error:
                st.error("Unable to authenticate against MySQL.")
                st.code(str(error))

    st.info(
        "Accounts must be created separately using create_user.py."
    )

    st.stop()


# ==================================================
# 11. SESSION AND LOGOUT
# ==================================================

user = st.session_state.user
username = user["username"]
role = user["role"]

left, right = st.columns([4, 1])

with left:
    st.success(
        f"Logged in as {username} | Role: {role.title()}"
    )

with right:
    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()


# ==================================================
# 12. STUDENT DASHBOARD
# ==================================================

if role == "student":

    st.header("🎓 Student Dashboard")

    submission_tab, tracking_tab = st.tabs(
        ["Submit Project", "My Submissions"]
    )

    # ----------------------------------------------
    # Submit project
    # ----------------------------------------------

    with submission_tab:

        st.subheader("Submit a Project")

        with st.form("student_submission_form"):

            student_name = st.text_input(
                "Display name",
                value=username,
                max_chars=100,
            )

            title = st.text_input(
                "Project title",
                max_chars=150,
            )

            subject = st.selectbox(
                "Subject",
                SUBJECTS,
            )

            description = st.text_area(
                "Project description",
                max_chars=5000,
            )

            project_link = st.text_input(
                "Repository link (optional)",
                max_chars=1000,
            )

            submit_clicked = st.form_submit_button(
                "Submit Project"
            )

        if submit_clicked:

            try:
                reference_id = create_submission(
                    username,
                    student_name,
                    title,
                    subject,
                    description,
                    project_link,
                )

                st.success(
                    "Project submitted successfully!"
                )

                st.write("Your submission reference:")
                st.code(reference_id)

                st.caption(
                    "Your submission is now available to the "
                    "faculty review dashboard."
                )

            except (ValueError, PermissionError) as error:
                st.error(str(error))

            except (MySQLError, RuntimeError) as error:
                st.error(
                    "The submission could not be saved. "
                    "Check the MySQL connection and try again."
                )

                st.code(str(error))

    # ----------------------------------------------
    # Track submissions
    # ----------------------------------------------

    with tracking_tab:

        st.subheader("My Project Submissions")

        try:
            data = get_student_submissions(username)

            if data.empty:
                st.info(
                    "You have not submitted any projects yet."
                )

            else:
                display_data = data.copy()

                for column in ("created_at", "updated_at"):
                    display_data[column] = (
                        display_data[column].astype(str)
                    )

                st.dataframe(
                    display_data[
                        [
                            "reference_id",
                            "title",
                            "subject",
                            "status",
                            "updated_at",
                        ]
                    ],
                    use_container_width=True,
                    hide_index=True,
                )

                selected_id = st.selectbox(
                    "Select one of your submissions",
                    data["reference_id"].tolist(),
                )

                record = data[
                    data["reference_id"] == selected_id
                ].iloc[0]

                st.write("**Project:**", record["title"])
                st.write("**Subject:**", record["subject"])
                st.write("**Status:**", record["status"])

                st.write(
                    "**Faculty feedback:**",
                    record["feedback"] or "No feedback yet.",
                )

                if record["project_link"]:
                    st.write(
                        "**Repository:**",
                        record["project_link"],
                    )

                st.caption(
                    "Students can view their own submissions, "
                    "but cannot change faculty reviews."
                )

        except PermissionError as error:
            st.error(str(error))

        except (MySQLError, RuntimeError) as error:
            st.error("Unable to load your submissions.")
            st.code(str(error))


# ==================================================
# 13. FACULTY DASHBOARD
# ==================================================

elif role == "faculty":

    st.header("👨‍🏫 Faculty Review Dashboard")

    st.info(
        "Review submissions, provide feedback, and update "
        "project statuses."
    )

    try:
        data = get_faculty_submissions()

        if data.empty:
            st.info(
                "No project submissions are available yet."
            )

        else:
            st.subheader("Submission Queue")

            display_data = data[
                [
                    "reference_id",
                    "student_name",
                    "title",
                    "subject",
                    "status",
                    "created_at",
                ]
            ].copy()

            display_data["created_at"] = (
                display_data["created_at"].astype(str)
            )

            st.dataframe(
                display_data,
                use_container_width=True,
                hide_index=True,
            )

            selected_id = st.selectbox(
                "Select a project to review",
                data["reference_id"].tolist(),
            )

            record = data[
                data["reference_id"] == selected_id
            ].iloc[0]

            st.write("**Student:**", record["student_name"])
            st.write("**Project:**", record["title"])
            st.write("**Subject:**", record["subject"])
            st.write("**Description:**", record["description"])

            st.write(
                "**Repository link:**",
                record["project_link"] or "Not provided",
            )

            with st.form("faculty_review_form"):

                new_status = st.selectbox(
                    "Review status",
                    STATUSES,
                    index=STATUSES.index(record["status"]),
                )

                feedback = st.text_area(
                    "Faculty feedback",
                    value=record["feedback"],
                    max_chars=5000,
                )

                save_review = st.form_submit_button(
                    "Save Faculty Review"
                )

            if save_review:

                try:
                    update_review(
                        selected_id,
                        new_status,
                        feedback,
                    )

                    st.success(
                        "Faculty review saved successfully."
                    )

                    st.rerun()

                except (ValueError, PermissionError) as error:
                    st.error(str(error))

                except (MySQLError, RuntimeError) as error:
                    st.error(
                        "Unable to save the review. "
                        "Check the MySQL connection and try again."
                    )

                    st.code(str(error))

    except PermissionError as error:
        st.error(str(error))

    except (MySQLError, RuntimeError) as error:
        st.error("Unable to load the faculty review dashboard.")
        st.code(str(error))


# ==================================================
# 14. FACULTY STATISTICS
# ==================================================

if role == "faculty":

    st.divider()
    st.header("📊 Submission Statistics")

    try:
        data = get_faculty_submissions()

        if data.empty:
            st.info(
                "Statistics will appear after submissions arrive."
            )

        else:
            total = len(data)

            pending = data["status"].isin(
                ["SUBMITTED", "UNDER_REVIEW"]
            ).sum()

            changes_requested = (
                data["status"] == "CHANGES_REQUIRED"
            ).sum()

            approved = (
                data["status"] == "APPROVED"
            ).sum()

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Total submissions", total)
            col2.metric("Pending review", int(pending))

            col3.metric(
                "Changes requested",
                int(changes_requested),
            )

            col4.metric("Approved", int(approved))

            st.subheader("Projects by Status")

            st.bar_chart(
                data["status"].value_counts()
            )

    except (MySQLError, RuntimeError, PermissionError) as error:
        st.error("Unable to calculate submission statistics.")
        st.code(str(error))


# ==================================================
# 15. FOOTER
# ==================================================

st.divider()

st.caption(
    "SkillBridge AI | Educational prototype for HKAIVERSE Task 1. "
    "Not an official IFHE system."
)