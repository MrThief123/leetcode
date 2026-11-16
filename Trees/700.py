"""
700. Search in a Binary Search Tree  [Easy]

Approach (iterative BST descent):
  - Go right if the node's value is smaller than the target, left if larger.
  - Stop when the value matches or we fall off the tree (None).

Complexity: O(h) time, O(1) space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left

        return root  # the matching node, or None if absent
