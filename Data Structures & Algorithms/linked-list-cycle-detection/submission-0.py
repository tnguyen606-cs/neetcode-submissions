# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """

        Given: 
            0 <= list.length <= 1k
            not unique list
            index determines the first node of the cycle
                - index = -1: no cycle

        Result:
            return true if a cycle, 
            othwerwise, false

        Approach: Two pointers
            Using fast and slow pointer, if there is a cycle, 2 pointers will finally meet

        Time: O(n)
        Space: O(1)
        """

        slow, fast = head, head

        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False