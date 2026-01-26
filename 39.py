'''
39. Combination Sum
Use backtracking to explore all combinations of candidates that sum up to the target.
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sol = []
        n = len(candidates)

        def backtrack(i, total):
            # success case
            if total == target:
                result.append(sol.copy())
                return
            
            # failure cases
            if total > target or i == n:
                return
            
            # pick candidates[i]
            sol.append(candidates[i])
            backtrack(i, total + candidates[i])  # reuse same index
            sol.pop()
            
            # don't pick candidates[i]
            backtrack(i + 1, total)

        backtrack(0, 0)
        return result
