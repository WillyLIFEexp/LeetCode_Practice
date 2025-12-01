import pytest
from my_sol import Solution

@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize("roman_string, expected_integer", [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("IV", 4),
    ("IX", 9),  
    ("XX", 20),
])
def test_roman_to_int(solver, roman_string, expected_integer):
    # Action
    result = solver.romanToInt(roman_string)
    
    # Assertion
    assert result == expected_integer