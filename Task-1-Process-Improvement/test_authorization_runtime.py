
import ast
from pathlib import Path

# Read app.py without executing the entire Streamlit application
source = Path("app.py").read_text()
tree = ast.parse(source)

# Find the actual require_role function
require_role_function = next(
    (
        node for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and node.name == "require_role"
    ),
    None,
)

if require_role_function is None:
    raise AssertionError("TEST FAILED: require_role function not found.")

# Compile only the actual require_role function
module = ast.Module(
    body=[require_role_function],
    type_ignores=[]
)
ast.fix_missing_locations(module)


# Simulate Streamlit session state
class FakeStreamlit:
    def __init__(self, user=None):
        self.session_state = {}

        if user is not None:
            self.session_state["user"] = user


namespace = {
    "st": FakeStreamlit(),
    "PermissionError": PermissionError,
}

exec(compile(module, "app.py", "exec"), namespace)

require_role = namespace["require_role"]


# TEST 1: Student attempts a faculty-only action
namespace["st"] = FakeStreamlit(
    {"username": "student1", "role": "student"}
)

try:
    require_role("faculty")
except PermissionError:
    print("PASS: Student is rejected from faculty-only actions.")
else:
    raise AssertionError("FAIL: Student was incorrectly allowed.")


# TEST 2: Faculty attempts a faculty-only action
faculty = {"username": "faculty1", "role": "faculty"}
namespace["st"] = FakeStreamlit(faculty)

result = require_role("faculty")

assert result == faculty
print("PASS: Faculty is allowed to continue.")


# TEST 3: Unauthenticated user attempts a faculty-only action
namespace["st"] = FakeStreamlit()

try:
    require_role("faculty")
except PermissionError:
    print("PASS: Unauthenticated user is rejected.")
else:
    raise AssertionError(
        "FAIL: Unauthenticated user was incorrectly allowed."
    )
