"""
1022. Sum of Root To Leaf Binary Numbers  [Easy]

Approach (DFS carrying the path):
  - Build the root-to-node bit string as we descend.
  - At a leaf, convert the string from base 2 and add it to the total.
  - (Passing a running integer, num*2 + val, would avoid string building.)

Complexity: O(n) time, O(h) space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0  # sum over all leaves

        def dfs(node, s):
            if not node:
                return

            s += str(node.val)  # extend the path with this bit

            # If leaf node
            if not node.left and not node.right:
                self.total += int(s, 2)
                return

            dfs(node.left, s)
            dfs(node.right, s)

        dfs(root, "")
        return self.total
