# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Intuition:
            - All node values are unique
            - 2 nodes from p and q returns LCA
            - LCA is the lowest node in a tree T where p and q are descendants
            - A node can be a descendant/ancestor of itself.
            - 2 <= # nodes <= 100
            - p != q
            - p, q exists in tree
            - All values in the left subtree < the node's value
            - All values in the right subtree > the ndoe's value

        Approach 1: Recursion
            For both p and q:
                - if both values > current node:
                    go to the right subtree
                - elif both values < current node:
                    go to the left subtree
                - else, either value == current node or the current node is a split point 
                    return the current node
            Time: O(h), h is the height of the tree
            Space: O(h)

        """

        if not root or not q or not p:
            return None
        
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root