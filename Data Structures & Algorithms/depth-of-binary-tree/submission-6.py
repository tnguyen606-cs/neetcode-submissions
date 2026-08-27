# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given: root of a BT
            depth: number of nodes of the longest path from root

        Return: depth

        Approach 1: Recursion DFS
            Idea: depth = 1 + max(left, right)
            - if root is none: return 0
            - Recursively compute the depth of the left subtree
            - Recursively compute the depth of the right subtree.
            - return max(left, right) + 1
            - Time: O(n)
            - Space: O(n) for recursion stack

        Approach 2: Iterative DFS
            Idea: depth = 1 + max(lef, right)
            - if root is none: return 0
            - stack store a pair of the current node and its depth in the tree
            - while stack is not empty:
                - pop a node
                - we update the max depth of the current node
                - we push its left and right onto the stack if they exists
            - Time: O(n)
            - Space: O(n)

        Approach 3: Interative BFS
            - Every iteration of BFS processes one entire level of the tree
            - Each completed level corresponds to increasing the depth by 1
            - Count how many levels we traverse within the tree until the queue is empty
            - Time: O(n)
            - Space: O(n)
        """

        if not root:
            return 0

        level = 0
        queue = deque()
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return level