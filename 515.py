'''
515. Find Largest Value in Each Tree Row
Perform a level-order traversal (BFS) of the binary tree
At each level, track the maximum value among all nodes
Append the maximum value of each level to the result list   
'''

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

        out = []

        # BFS
        while queue:
            next_row = []
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