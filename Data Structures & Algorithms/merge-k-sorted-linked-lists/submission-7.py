# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Given:
            k LL list
            each LL is sorted in ascending order
            each LL can contain duplucate number

        Return:
            merged sorted list of all K LL

        Difficult:
            how to compare values between k LLs?
                - sort and merge every 2 LLs first

        Approach: Divide and Conquer
            - Divide the big array into 2 halves
            - Sort and merge every left and right arrays until we get ta single array
        
        Time: O(n * m)
        Space: O(n + m)
        """

        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.sortAndMerge(list1, list2))
            
            lists = mergedLists

        return lists[0]


    def sortAndMerge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()

        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val > l2.val:
                dummy.next = l2
                l2 = l2.next
            else:
                dummy.next = l1
                l1 = l1.next

            dummy = dummy.next

        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2

        return res.next

