"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Given:
            A linkedlist, length n, each node has 2 pointers, which may point to another node or null
            0 <= n <= 100
            Node values are not unique

        Result:
            a depp copy of the list:
                - has exactly n new nodes
                - original val of the copied node
                - next pointer to new node == next pointer to org node
                - random pointer to new node == random pointer to org node


        Difficulty:
            how we create the random pointer that hasn't created yet?
        
        Approach: 2 Passes
            1. Create a hashmap 

        Time: O(n)
        Space: O(n)
        """

        # Create a hashmap to store the node object
        org_to_copy = { None: None }

        cur = head
        while cur:
            node = Node(cur.val)
            org_to_copy[cur] = node
            cur = cur.next

        # Copy the next, random pointers to node objects
        cur = head
        while cur:
            copy = org_to_copy[cur]
            copy.next = org_to_copy[cur.next]
            copy.random = org_to_copy[cur.random]
            cur = cur.next
        
        return org_to_copy[head]
        






















