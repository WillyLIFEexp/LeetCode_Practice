import pytest
from my_sol import Solution

@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize("input_string, expected_bool", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    ("([)]", False),  
    ("((", False),  
    ("){", False),  
])
def test_validate_parentheses(solver, input_string, expected_bool):
    # Action
    result = solver.isValid(input_string)
    
    # Assertion
    assert result == expected_bool