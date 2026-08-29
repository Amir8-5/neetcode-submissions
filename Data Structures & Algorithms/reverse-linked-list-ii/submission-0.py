# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        prev = dummy
        for _ in range(left - 1):
            prev, cur = cur, cur.next
        
        leftMost = prev
        prev = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        temp = leftMost.next
        temp.next = cur
        leftMost.next = prev
        
        return dummy.next

