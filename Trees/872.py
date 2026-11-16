"""
872. Leaf-Similar Trees  [Easy]

Approach (DFS leaf collection):
  - Collect the leaf values of each tree left to right (the "leaf sequence").
  - The trees are leaf-similar if both sequences are equal.

Complexity: O(n + m) time, O(n + m) space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        stack1 = []  # leaf values of tree 1, in order
        stack2 = []  # leaf values of tree 2, in order

        def dfs(root: Optional[TreeNode], stack):

            if not root:
                return

            # Visit left subtree before right so leaves come out left to right
            dfs(root.left, stack)
            dfs(root.right, stack)

            # A leaf has no children
            if not root.left and not root.right:
                stack.append(root.val)

        dfs(root1, stack1)
        dfs(root2, stack2)

        return stack1 == stack2
