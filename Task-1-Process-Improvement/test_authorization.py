import ast
from pathlib import Path


def load_app_functions():
    source = Path("app.py").read_text()
    tree = ast.parse(source)

    functions = {
        node.name: node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    }

    return functions


def test_require_role_function_exists():
    functions = load_app_functions()
    assert "require_role" in functions


def test_update_review_function_exists():
    functions = load_app_functions()
    assert "update_review" in functions


def test_update_review_requires_faculty_role():
    functions = load_app_functions()
    assert "update_review" in functions

    update_review = functions["update_review"]

    faculty_check_found = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "require_role"
        and len(node.args) >= 1
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value == "faculty"
        for node in ast.walk(update_review)
    )

    assert faculty_check_found, (
        "update_review must call require_role('faculty')"
    )
