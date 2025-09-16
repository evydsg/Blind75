# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        pointer = head
        next_pointer = None

        while pointer:
            next_element = pointer.next
            pointer.next = next_pointer
            next_pointer = pointer
            pointer = next_element

        return next_pointer