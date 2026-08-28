# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        nodes = []

        while cur:
            nodes.append(cur)
            cur = cur.next
        
        n = len(nodes)

        left, right = 0, n - 1

        while left < right:
            nodes[left].next = nodes[right]
            if left + 1 < right:
                nodes[right].next = nodes[left + 1]
            else:
                nodes[right].next = None

            left += 1
            right -= 1
        
        if left == right:
            nodes[right].next = None