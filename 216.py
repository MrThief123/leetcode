'''
Finding all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
Using Backtracking to explore all potential combinations while adhering to the constraints.'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        nums = [i for i in range(1, 10)]

        def backtrack(index, total, curr, nums):
            if index > k or total > n:
                return
            if index == k and total == n:
                result.append(curr)
                return

            if not curr:
                a = 0
            else:
                a = curr[-1]

            for i in range(a+1, 10):
                backtrack(index + 1, total + i, curr + [i], nums)

        backtrack(0, 0, [], nums)
        return result
