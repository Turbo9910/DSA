# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            current = current.next
            count+=1
        if count == 1:
            return head
        middle = count //2


        i= 0
        current = head
        while i < middle -1 and current:
            current = current.next
            i+=1
        
        return current.next

        