from deps import ListNode
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        # handle edge cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
        extra_list = list1 if list1 else list2
        while extra_list:
            cur.next = ListNode(extra_list.val)
            extra_list = extra_list.next
            cur = cur.next
        return head.next