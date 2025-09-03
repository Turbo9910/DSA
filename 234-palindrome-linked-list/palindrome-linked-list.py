# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        current = head

        if current.next is None:
            return True
        r = list()
        while current:
            r.append(current.val)
            current = current.next
        if r[::-1] == r:
            return True
        else:
            return False

        