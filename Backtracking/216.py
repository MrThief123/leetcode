"""
216. Combination Sum III  [Medium]

Approach (backtracking with increasing digits):
  - Choose exactly k distinct digits from 1..9 that sum to n.
  - Build combinations in increasing order (next digit > last digit) to avoid
    duplicates and permutations.
  - Prune when we've used too many digits or the total exceeds n.

Complexity: O(C(9, k) * k) time, O(k) recursion depth
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        nums = [i for i in range(1, 10)]  # unused; digits come from range(a+1, 10) below

        # index = how many digits chosen, total = their sum, curr = the digits
        def backtrack(index, total, curr, nums):
            # Pruning: too many digits or overshoot
            if index > k or total > n:
                return
            if index == k and total == n:
                result.append(curr)
                return

            # Next digit must exceed the last one chosen
            if not curr:
                a = 0
            else:
                a = curr[-1]

            for i in range(a+1, 10):
                backtrack(index + 1, total + i, curr + [i], nums)

        backtrack(0, 0, [], nums)
        return result
