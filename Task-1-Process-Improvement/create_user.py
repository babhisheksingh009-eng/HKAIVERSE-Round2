
import argparse
import getpass
import hashlib
import secrets
import os

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "database": os.getenv("DB_NAME", "skillbridge_ai"),
    "user": os.getenv("DB_USER", "skillbridge_app"),
    "password": os.getenv("DB_PASSWORD", ""),
    "connection_timeout": 10,
}


def get_connection():
    if not DB_CONFIG["password"]:
        raise RuntimeError(
            "DB_PASSWORD is missing. Check your .env file."
        )

    return mysql.connector.connect(**DB_CONFIG)


def hash_password(password):
    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600_000,
    ).hex()

    return (
        f"pbkdf2_sha256$600000$"
        f"{salt.hex()}${password_hash}"
    )


def create_user(username, role):
    username = username.strip()

    if not username:
        print("Error: Username cannot be empty.")
        return

    if len(username) > 100:
        print("Error: Username cannot exceed 100 characters.")
        return

    if role not in ("student", "faculty"):
        print("Error: Role must be student or faculty.")
        return

    password = getpass.getpass("Enter password: ")

    if len(password) < 12:
        print("Error: Password must contain at least 12 characters.")
        return

    confirm_password = getpass.getpass("Confirm password: ")

    if password != confirm_password:
        print("Error: Passwords do not match.")
        return

    password_hash = hash_password(password)
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(100) PRIMARY KEY,
                password_hash VARCHAR(255) NOT NULL,
                role ENUM('student', 'faculty') NOT NULL,
                created_at DATETIME NOT NULL
                    DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB
            """
        )

        cursor.execute(
            """
            INSERT INTO users (
                username,
                password_hash,
                role
            )
            VALUES (%s, %s, %s)
            """,
            (username, password_hash, role),
        )

        # Save the account permanently in MySQL.
        conn.commit()

        print(
            f"Successfully created {role} account: {username}"
        )

    except Error as error:
        if conn is not None:
            conn.rollback()

        if error.errno == 1062:
            print("Error: That username already exists.")
        else:
            print(f"Database error: {error}")

    except RuntimeError as error:
        print(f"Configuration error: {error}")

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a SkillBridge AI user account."
    )

    parser.add_argument("--username", required=True)

    parser.add_argument(
        "--role",
        required=True,
        choices=["student", "faculty"],
    )

    args = parser.parse_args()

    create_user(args.username, args.role)
