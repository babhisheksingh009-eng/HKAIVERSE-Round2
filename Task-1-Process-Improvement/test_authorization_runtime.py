import ast
from pathlib import Path
import pytest


def load_require_role():
    source = Path("app.py").read_text()
    tree = ast.parse(source)

    function = next(
        (
            node for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
            and node.name == "require_role"
        ),
        None,
    )

    if function is None:
        raise AssertionError("require_role function not found in app.py")

    module = ast.Module(body=[function], type_ignores=[])
    ast.fix_missing_locations(module)

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
    return namespace, FakeStreamlit


def test_student_is_rejected_from_faculty_action():
    namespace, FakeStreamlit = load_require_role()
    namespace["st"] = FakeStreamlit(
        {"username": "student1", "role": "student"}
    )

    with pytest.raises(PermissionError):
        namespace["require_role"]("faculty")


def test_faculty_is_allowed_for_faculty_action():
    namespace, FakeStreamlit = load_require_role()
    faculty = {"username": "faculty1", "role": "faculty"}
    namespace["st"] = FakeStreamlit(faculty)

    assert namespace["require_role"]("faculty") == faculty


def test_unauthenticated_user_is_rejected():
    namespace, FakeStreamlit = load_require_role()
    namespace["st"] = FakeStreamlit()

    with pytest.raises(PermissionError):
        namespace["require_role"]("faculty")
