import sqlite3


def check(name, condition):
    if not condition:
        raise AssertionError(f"FAIL: {name}")
    print(f"PASS: {name}")


# 1. C programming exercise: expected even/odd logic
def classify_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


check("Even/odd: zero", classify_even_odd(0) == "Even")
check("Even/odd: positive even", classify_even_odd(2) == "Even")
check("Even/odd: negative odd", classify_even_odd(-3) == "Odd")
check("Even/odd: positive odd", classify_even_odd(7) == "Odd")


# 2. Data Structures and Algorithms: linear search
def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


check("Linear search: empty list", linear_search([], 5) == -1)
check("Linear search: one element", linear_search([5], 5) == 0)
check("Linear search: first element", linear_search([4, 8, 2], 4) == 0)
check("Linear search: last element", linear_search([4, 8, 2], 2) == 2)
check("Linear search: absent target", linear_search([4, 8, 2], 7) == -1)


# 3. DBMS: SQL filtering and aggregation with synthetic data
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE employees (name TEXT, department TEXT)"
)
cursor.executemany(
    "INSERT INTO employees VALUES (?, ?)",
    [
        ("Employee A", "HR"),
        ("Employee B", "IT"),
        ("Employee C", "IT"),
        ("Employee D", "HR"),
        ("Employee E", "IT"),
    ],
)

cursor.execute(
    "SELECT department, COUNT(*) FROM employees "
    "GROUP BY department ORDER BY department"
)
department_counts = dict(cursor.fetchall())

check(
    "SQL GROUP BY/COUNT",
    department_counts == {"HR": 2, "IT": 3},
)

cursor.execute(
    "SELECT COUNT(*) FROM employees WHERE department = ?",
    ("IT",),
)
check("SQL WHERE filter", cursor.fetchone()[0] == 3)
connection.close()


# 4. Operating Systems: Round Robin scheduling
def round_robin(bursts, quantum):
    remaining = bursts[:]
    completion = [0] * len(bursts)
    time = 0

    while any(burst > 0 for burst in remaining):
        for i in range(len(remaining)):
            if remaining[i] > 0:
                run_time = min(quantum, remaining[i])
                time += run_time
                remaining[i] -= run_time

                if remaining[i] == 0:
                    completion[i] = time

    turnaround = completion[:]
    waiting = [
        turnaround[i] - bursts[i]
        for i in range(len(bursts))
    ]
    return completion, waiting, turnaround


completion, waiting, turnaround = round_robin([5, 3, 1], 2)

check("Round Robin completion times", completion == [9, 8, 5])
check("Round Robin waiting times", waiting == [4, 5, 4])
check("Round Robin turnaround times", turnaround == [9, 8, 5])


# 5. Machine Learning: confusion matrix accuracy arithmetic
tn, fp, fn, tp = 8, 2, 1, 9
accuracy = (tp + tn) / (tp + tn + fp + fn)

check("Confusion matrix accuracy", abs(accuracy - 0.85) < 1e-9)

print("\nAll verification checks passed.")
print("Scope: logic, synthetic SQL data, scheduling, and arithmetic.")
print("No ML model was trained. The C program was compiled and tested separately; see ai_assisted_exercises.md.")
