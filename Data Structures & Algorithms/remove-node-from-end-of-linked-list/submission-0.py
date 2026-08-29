# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the linked list
        # cur, prev = head, None
        # while cur:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        
        # remove n-th node
        leng = 0
        cur = head
        while cur:
            leng += 1
            cur = cur.next
        
        actualIndex = leng - n
        print("leng is: " + str(leng) + " actual is: " + str(actualIndex))
        i = 0
        prev = None
        ref = ListNode()
        ref.next = head
        cur = ref
        for _ in range(actualIndex):
            cur = cur.next
        print("the node i am deleting is: ", cur.next.val)
        cur.next = cur.next.next
        return ref.next


        