'''
Check if two binary trees are leaf-similar
Use a stack to store the leaf values of the first tree
Traverse the second tree and compare its leaf values with the stack
If all leaf values match, return True; otherwise, return False
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        stack1 = []
        stack2 = []

        def dfs(root: Optional[TreeNode], stack):

            if not root:
                return 

            dfs(root.left, stack)
            dfs(root.right, stack)

            if not root.left and not root.right:
                stack.append(root.val)
        
        dfs(root1, stack1)
        dfs(root2, stack2)

        return stack1 == stack2