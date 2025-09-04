# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if head is None:
            return head
        current = head
        result = 0
        i = 0
        k = 0
        a = [0] * 100000
        while current:
            a[i] = current.val
            current = current.next
            i+=1
        i-=1
        while i >=0:
            if a[i] == 1:
                result = result + pow(2,k)
            i-=1
            k+=1
        return result



        