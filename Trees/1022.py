'''
1022. Sum of Root To Leaf Binary Numbers
Use DFS to traverse the tree and keep track of the path from root to leaf as a string. 
When we reach a leaf node, we convert the string to an integer using base 2 and add it to the total sum.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def dfs(node, s):
            if not node:
                return
            
            s += str(node.val)
            
            # If leaf node
            if not node.left and not node.right:
                self.total += int(s, 2)
                return
            
            dfs(node.left, s)
            dfs(node.right, s)
        
        dfs(root, "")
        return self.total