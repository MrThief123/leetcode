"""
39. Combination Sum  [Medium]

Approach (backtracking, pick or skip):
  - At each index decide to take candidates[i] (and stay on i, since values may
    be reused) or move on to i + 1.
  - Stop successfully when the total hits target; stop on overshoot or running out of candidates.

Complexity: O(2^(target/min)) time worst case, O(target/min) recursion depth
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sol = []  # current combination being built
        n = len(candidates)

        def backtrack(i, total):
            # success case
            if total == target:
                result.append(sol.copy())  # copy: sol keeps changing
                return

            # failure cases
            if total > target or i == n:
                return

            # pick candidates[i]
            sol.append(candidates[i])
            backtrack(i, total + candidates[i])  # reuse same index
            sol.pop()  # undo the choice

            # don't pick candidates[i]
            backtrack(i + 1, total)

        backtrack(0, 0)
        return result
