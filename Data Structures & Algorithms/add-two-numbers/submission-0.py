# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumRef = ListNode(None)
        sum = sumRef
        remainder = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sumNum = (num1 + num2 + remainder) % 10
            remainder = (num1 + num2 + remainder) // 10
            sum.next = ListNode(sumNum)
            sum = sum.next
            if (l1 and l2):
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l1 = l1.next
            elif l2:
                l2 = l2.next
            else:
                pass
            
        if remainder != 0:
            sum.next = ListNode(remainder)
        return sumRef.next
        