'''
503. Next Greater Element II
Maintain a monotonic stack of indices (value, index). Iterate through the array twice to simulate circularity.
When we find a number greater than the number at the index stored at the top of the stack,
we pop from the stack and set the result for that index.
'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        out = [-1 for i in range(n)]

        stack = []

        for n, i in enumerate(nums):
            curr = (i, n)

            while stack and curr[0] > stack[-1][0]:
                prev = stack.pop()
                out[prev[1]] = curr[0]

            stack.append(curr)
            
        for n, i in enumerate(nums):
            curr = (i, n)

            while stack and curr[0] > stack[-1][0]:
                prev = stack.pop()
                out[prev[1]] = curr[0]

            stack.append(curr)
                
        return out