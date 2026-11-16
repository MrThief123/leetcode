"""
515. Find Largest Value in Each Tree Row  [Medium]

Approach (BFS level by level):
  - Process one whole level at a time from the queue.
  - Track the maximum value on the level while gathering the next level's nodes.

Complexity: O(n) time, O(w) space (w = max tree width)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        queue = deque()

        if not root:
            return []

        queue.append(root)

        out = []  # one maximum per level

        # BFS
        while queue:
            next_row = []  # children, i.e. the next level
            maxx = float('-inf')

            # Process current level
            while queue:
                curr = queue.popleft()
                maxx = max(maxx, curr.val)

                if curr.left:
                    next_row.append(curr.left)
                if curr.right:
                    next_row.append(curr.right)

            out.append(maxx)
            queue.extend(next_row)

        return out
