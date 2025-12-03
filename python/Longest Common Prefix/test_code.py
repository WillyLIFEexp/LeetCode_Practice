import pytest
from my_sol import Solution

@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize("input_lst, expected_str", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["interspecies", "interstellar", "interstate"], "inters"),
    (["throne", "throne"], "throne"),
    (["check"], "check"),
    (["c", "acc", "ccc"], ""), 
    ([], "") # This works now because of the added check
])
def test_roman_to_int(solver, input_lst, expected_str):
    # Action
    result = solver.longestCommonPrefix(input_lst)
    
    # Assertion
    assert result == expected_str