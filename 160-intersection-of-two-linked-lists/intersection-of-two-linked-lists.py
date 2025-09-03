# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        currentA = headA
        currentB = headB
        seen = set()
        while currentA:
            if currentA in seen:
                return currentA
            seen.add(currentA)
            currentA = currentA.next
        while currentB:
            if currentB in seen:
                return currentB
            seen.add(currentB)
            currentB = currentB.next
        return None

        
        