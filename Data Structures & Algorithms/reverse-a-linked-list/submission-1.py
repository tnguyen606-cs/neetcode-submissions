# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """

        Given: 
            0 <= list.length <= 1000
            duplicate numbers

        Result:
            if list is empty, return empty
            else: return reversed list

        Approach: Iteration
            Traverse through a list from left to right
            For each node, we direct each node's "next" pointer to point to the node before it

        Time: O(n)
        Space: O(1)

        """

        prev = None
        res = head
        
        while res:
            tmp = res.next
            res.next = prev
            prev = res
            res = tmp

        return prev
            