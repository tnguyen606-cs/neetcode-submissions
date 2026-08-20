# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given:
            - 2 non-empty LL, non-neg integers
            - The digits is in reverse order: 321 == 1 -> 2 -> 3
            - Each node has a digit
            - No leading zero, except the number 0 itself
            - 1 <= l1.length, l2.legnth <= 100

        Result:
            - Sum of 2 numbers as a linkedlist

        Clarification:
            EX:
                L1: 1 -> 2 -> 3 -> 7
                L2: 5 -> 7 -> 9
                Output: 6 -> 9 -> 2 -> 8 (8296)

                L1: 1 -> 2
                L2: 5 -> 7 -> 9
                Output: 6 -> 9 -> 9 (996)

            - 2 LLs are not guaranteed to have same length

        Approach: Two Pointers
        Traverse through both LLs until we reach the null in either list
            - Sum 2 numbers of the 2 LLs
            - If the sum > 10, bring the carry to the next sum
            - Append new node contain digit

        Time: O(n + m)
        Space: O(1)
        """
        # Create a node to store the answer
        ans = dummy = ListNode()

        # 2 pointers for l1, l2
        p1, p2 = l1, l2
        carry = 0
        digit = -1

        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            res = val1 + val2 + carry
            carry = res // 10
            digit = res % 10
            dummy.next = ListNode(digit)
            dummy = dummy.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        return ans.next


