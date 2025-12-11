import pytest
from deps import create_linked_list, ListNode
from my_sol import Solution  # Assuming your Solution class is in my_sol.py

# --- Helper Function for Assertions ---
def linked_list_to_list(head: ListNode) -> list:
    """Converts a linked list back to a Python list for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# --- Pytest Fixtures and Tests ---

@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize("list1_arr, list2_arr, expected_arr", [
    # Case 1: Standard merge of two sorted lists
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    
    # Case 2: Both lists are empty
    ([], [], []),
    
    # Case 3: First list is empty
    ([], [0], [0]),
    
    # Case 4: Second list is empty
    ([1], [], [1]),
    
    # Case 5: Different lengths
    ([1, 2, 5], [3, 4], [1, 2, 3, 4, 5]),
    
    # Case 6: One list has all smaller values
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
])
def test_merge_two_lists(solver, list1_arr, list2_arr, expected_arr):
    # Setup: Convert input arrays to Linked Lists
    l1 = create_linked_list(list1_arr)
    l2 = create_linked_list(list2_arr)
    
    # Action
    result_head = solver.mergeTwoLists(l1, l2)
    
    # Transformation: Convert result LL back to list for comparison
    result_list = linked_list_to_list(result_head)
    
    # Assertion
    assert result_list == expected_arr