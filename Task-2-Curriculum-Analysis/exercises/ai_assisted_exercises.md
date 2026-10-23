# AI-Assisted Exercises and Verification Record

**Record date:** 23 October 2026
**AI assistance disclosure:** ChatGPT (GPT-6) assisted in drafting the exercise prompts and verification plan.

## 1. C Programming

**Topic:** Integer input, validation, and even/odd classification.

**Prompt:**
"Create a beginner-level C programming exercise that reads an integer, validates the input, and determines whether the number is even or odd. Explain the expected behaviour and provide test cases."

**Output summary:** An exercise covering integer input, modulo, and even/odd classification.

**Verification performed:**
- Tested the even/odd logic using Python for inputs 0, 2, -3, and 7; all expected classifications passed.
- Compiled `exercises/even_odd.c` using GCC with `-Wall -Wextra -Werror`; compilation succeeded without reported warnings or errors.
- Ran the compiled program with inputs `2`, `-3`, and `abc`. The program correctly classified 2 as even, -3 as odd, and rejected `abc` as invalid input.

**Result:** PASS for the documented tests. The C program's tested inputs and invalid-input handling behaved as expected. Additional edge cases, such as integer values outside the supported range, have not been tested.

## 2. Data Structures and Algorithms

**Topic:** Linear search.

**Prompt:**
"Create a beginner-level exercise to implement linear search in an integer array. Explain the algorithm, provide sample inputs and outputs, and state its time complexity."

**Output summary:** A linear-search exercise with expected results and complexity discussion.

**Verification performed:** Tested empty input, a one-element list, targets at the beginning and end, and an absent target using a Python implementation.

**Result:** PASS for the tested cases. Worst-case time complexity is O(n), because the algorithm may inspect every element.

## 3. Database Management Systems

**Topic:** SQL filtering and aggregation.

**Prompt:**
"Create a SQL exercise using a small synthetic employee table. Ask the learner to filter records by department and count employees in each department. Provide expected results and explain the query."

**Output summary:** A SQL exercise using WHERE, GROUP BY, and COUNT.

**Verification performed:** Executed a GROUP BY/COUNT query in an in-memory SQLite database using five synthetic employee records.

**Observed result:** HR = 2 employees; IT = 3 employees.

**Result:** PASS for the tested SQL aggregation. The test used synthetic data, not a production database.

## 4. Operating Systems

**Topic:** Round Robin CPU scheduling.

**Prompt:**
"Create a beginner-level Round Robin CPU scheduling problem with three processes, arrival times, burst times, and a specified time quantum. Ask the learner to draw the Gantt chart and calculate waiting time and turnaround time."

**Test inputs:** P1 burst time = 5, P2 = 3, P3 = 1; all arrival times = 0; time quantum = 2.

**Verification performed:** Independently simulated the Round Robin sequence and checked each process's completion time, waiting time, and turnaround time.

**Observed completion times:** P1 = 9, P2 = 8, P3 = 5.
**Observed waiting times:** P1 = 4, P2 = 5, P3 = 4.
**Turnaround times:** P1 = 9, P2 = 8, P3 = 5.

**Result:** PASS for this scheduling scenario. Waiting time was calculated as turnaround time minus burst time.

## 5. Machine Learning

**Topic:** Confusion matrix and classification accuracy.

**Prompt:**
"Create a beginner-level machine learning exercise using a small synthetic classification dataset. Explain why the data should be divided into training and test sets, and ask the learner to calculate accuracy from a confusion matrix."

**Test values:** TN = 8, FP = 2, FN = 1, TP = 9.

**Verification performed:** Calculated accuracy independently as (TP + TN) / (TP + TN + FP + FN).

**Calculation:** (9 + 8) / (8 + 2 + 1 + 9) = 17/20 = 85%.

**Result:** PASS for the arithmetic. No machine-learning model was trained; this check does not validate model performance or data-splitting methodology.

## Overall Reflection

AI can help draft exercises and propose verification steps, but its outputs must be checked. The checks recorded here cover Python implementations of basic logic and linear search, SQL execution with synthetic data, a Round Robin scheduling calculation, and confusion-matrix arithmetic.

**Limitations:** The C program still needs compilation and invalid-input tests. The ML exercise still needs a separate practical experiment if model training and train-test separation are to be demonstrated. These checks do not verify the official programme syllabus.

**Reproducibility:** A verification script was run locally on 23 October 2026. The results above describe the checks performed and their limitations.
