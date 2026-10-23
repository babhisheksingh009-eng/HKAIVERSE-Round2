import ast
from pathlib import Path

# Read app.py without importing or executing it
source = Path("app.py").read_text()
tree = ast.parse(source)

# Find the require_role function
require_role_function = None
update_review_function = None

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        if node.name == "require_role":
            require_role_function = node
        elif node.name == "update_review":
            update_review_function = node

# Check that both functions exist
assert require_role_function is not None, (
    "TEST FAILED: require_role function not found."
)

assert update_review_function is not None, (
    "TEST FAILED: update_review function not found."
)

# Check that update_review calls require_role("faculty")
faculty_check_found = any(
    isinstance(node, ast.Call)
    and isinstance(node.func, ast.Name)
    and node.func.id == "require_role"
    and len(node.args) >= 1
    and isinstance(node.args[0], ast.Constant)
    and node.args[0].value == "faculty"
    for node in ast.walk(update_review_function)
)

if faculty_check_found:
    print("TEST PASSED: update_review requires the faculty role.")
    print("TEST PASSED: The authorization check is present.")
else:
    print("TEST FAILED: Faculty authorization check not found.")