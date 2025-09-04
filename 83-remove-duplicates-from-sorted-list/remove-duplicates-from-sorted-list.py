# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        current = head
        same = False
        while current:
            same = False
            if current.next:
                if current.val == current.next.val:
                    delete_node = current.next
                    same = True
                    if delete_node.next:
                        current.next = delete_node.next
                    else:
                        current.next = None
                        return head
            if not same:
                current = current.next
        return  head

                    
        