# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Given:
            1 <= k <= n <= 5k
            Reverse k nodes
            if n - m * k <= k: keep it
            Only allow to modify the node's next pointers

        Result:
            new list after reserving m * k nodes

        Approach1:

            Time: O(n)
            Space: O(1)

        """
        
        # Iterate through LL to reverse 
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # Reverse
            curr = groupPrev.next
            prev = kth.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Append the remaning
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next
    
    def getKth(self, cur, k):
        while cur and k > 0:
            k -= 1
            cur = cur.next
        return cur
            
            

            