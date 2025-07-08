# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         if head is None:
            print("List is Empty")
            return
     
         n = None
         ptr = head
         while ptr:
            # original next
             next_node = ptr.next
             ptr.next = n
             n = ptr
             ptr = next_node
         return n
        