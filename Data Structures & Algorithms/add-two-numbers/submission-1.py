# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        carry = 0

        dummy = ListNode()
        cur = dummy

        while cur1 or cur2 or carry:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            total = val1 + val2 + carry
            cur.next = ListNode(total % 10)
            cur = cur.next
            carry = total // 10 

            if cur1: cur1 = cur1.next
            if cur2: cur2 = cur2.next
        
        return dummy.next
