'''
2110. Count Number of Smooth Descent Periods of a Stock
Keep track of the lengths of consecutive descending sequences.
Use monotonic stacks to identify and count all smooth descent periods.
'''

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        def helper(n):
            out = 0
            for i in range(n):
                out += 1 + i
            return out

        stack = []
        out = 0

        for price in prices:
            if not stack or stack[-1] - 1 == price:
                stack.append(price)
            else:
                n = len(stack)
                out += helper(n)
                stack = []
                stack = [price]
        if stack:
            out += helper(len(stack))
        return out