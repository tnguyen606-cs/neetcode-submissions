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

        # Find the total of nodes
        curr = head
        num = 0
        while curr:
            curr = curr.next
            num += 1

        if num == n:
            return head.next

        node = head
        idx = 1
        while node:
            if idx == (num - n):
                node.next = node.next.next
                break
            node = node.next
            idx += 1
            
        return head

