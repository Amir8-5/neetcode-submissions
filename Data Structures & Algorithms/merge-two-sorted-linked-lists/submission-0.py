# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sort = ListNode()
        temp = sort
        if list1 is not None and list2 is not None:
            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    sort.next = list1
                    list1 = list1.next
                    sort = sort.next
                else:
                    sort.next = list2
                    list2 = list2.next
                    sort = sort.next
            if list1 is None:
                while list2 is not None:
                    sort.next = list2
                    sort = sort.next
                    list2 = list2.next
            else:
                while list1 is not None:
                    sort.next = list1
                    sort = sort.next
                    list1 = list1.next
            return temp.next
        else:
            if list1 is None:
                return list2
            elif list2 is None:
                return list1
            else:
                return None