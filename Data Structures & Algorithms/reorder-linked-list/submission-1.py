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

        Approach1: 2 Pointers
            l, r = 1, n
            store all nodes in an array
            iterate through the array to create a new reorder node using 2 pointers
        Time: O(n)
        Space: O(n)

        Approach2: Reversing + Merge
            Reverse the 2nd half 
            Merge the first half with the 2nd reverse half
        Time: O(n)
        Space: O(1)

        """

        if not head:
            return

        ## Find the middle using slow, fast
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        print(f"middle: {s.val}")

        ## Reverse the 2nd half 
        second = s.next
        dummy = s.next = None
        while second:
            print(f"second: {second.val}")
            temp = second.next
            second.next = dummy
            dummy = second
            second = temp

        ## Merge first and second
        first, second = head, dummy
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            

        





