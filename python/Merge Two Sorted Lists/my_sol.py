from deps import ListNode, create_linked_list

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i1 = list1
        i2 = list2
        rslt = ListNode(0)
        check_point = rslt
        if (not list1) or (not list2):
            return list1 or list2

        while i1 or i2:
            if i1 is None:
                rslt.next = ListNode(i2.val)
                i2 = i2.next
            elif i2 is None:
                rslt.next = ListNode(i1.val)
                i1 = i1.next
            else:

                if i1.val <= i2.val:
                    rslt.next = ListNode(i1.val)
                    i1 = i1.next
                else:
                    rslt.next = ListNode(i2.val)
                    i2 = i2.next
            rslt = rslt.next
        return check_point.next
