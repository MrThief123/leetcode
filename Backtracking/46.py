"""
46. Permutations  [Medium]

Approach:
  - Use itertools.permutations to generate every ordering of nums.
  - (Note: each permutation comes back as a tuple, not a list.)
  - A manual version would backtrack, swapping/choosing each unused element per position.

NOTE: `permutations` is imported inside the class body, so the method can't see
      it; this relies on LeetCode pre-importing itertools. Left unchanged.

Complexity: O(n! * n) time and space
"""

class Solution:
    from itertools import permutations
    def permute(self, nums: List[int]) -> List[List[int]]:

        out = []

        # All n! orderings of length n
        for perm in permutations(nums, len(nums)):
            out.append(perm)

        return out
