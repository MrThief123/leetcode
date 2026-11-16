"""
104. Maximum Depth of Binary Tree  [Easy]

Approach (recursion):
  - Depth of a node = 1 + max(depth of left, depth of right); an empty node has depth 0.

Complexity: O(n) time, O(h) space (recursion stack, h = height)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(root: Optional[TreeNode]):
            if root is None:
                return 0  # base case: empty subtree

            left_depth = depth(root.left)
            right_depth = depth(root.right)
            return 1 + max(left_depth, right_depth)
        return depth(root)
