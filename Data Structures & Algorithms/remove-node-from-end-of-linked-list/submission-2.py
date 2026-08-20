# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given: 
            head of a linkedlist
            remove nth node from the end of the list
            1 <= sz <= 30
            1 <= n <= sz

        Result:
            head of linkedlist

        Time: O(n)
        Space: O(1)
        """

        dummy = ListNode(0, head)

        # find the total length
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        if length == n:
            return head.next

        prev = head
        for _ in range(length - n - 1):
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next

