class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast, slow = head, dummy

        # Move fast ahead by n
        for _ in range(n):
            fast = fast.next

        # Move both until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the target node
        slow.next = slow.next.next

        return dummy.next