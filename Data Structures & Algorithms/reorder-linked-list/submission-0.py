# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """

        Given:
            1 <= length <= 1k
            not unique list
            Reorder:
                [0, n - 1, 1, n - 2, 2, n - 3, ... ]
        Return:
            None = reorder the list in place

        Time: O(n)
        Space: O(n)

        Approach: 2 Pointers
            l, r = 1, n
            store all nodes in an array
            iterate through the array to create a new dummy node 

        """

        if not head:
            return

        arr = []
        dummy = head

        while dummy:
            arr.append(dummy)
            dummy = dummy.next

        l, r = 0, len(arr) - 1
        
        while l < r:
            arr[l].next = arr[r]
            l += 1
            if l >= r:
                break
            arr[r].next = arr[l]
            r -= 1
        
        arr[l].next = None

        





