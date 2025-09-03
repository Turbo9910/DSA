# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        seen = set()
        current = head
        while current.next:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False
        


        