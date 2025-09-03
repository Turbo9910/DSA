# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if head is None:
            return head
        if current.next is None:
            return head
        count = 0
        r = list()
        while current:
            r.append(current.val)
            current = current.next
            count +=1
        current = head
        while current:
            current.val = r[count -1]
            current = current.next
            count-=1
        return head


        