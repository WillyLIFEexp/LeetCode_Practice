
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None
    
    # Create the head node
    head = ListNode(arr[0])
    current = head
    
    # Iterate through the rest of the array
    for value in arr[1:]:
        current.next = ListNode(value) # Create new node and link it
        current = current.next         # Move pointer forward
        
    return head