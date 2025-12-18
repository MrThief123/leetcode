'''Generate all permutations of a list of numbers'''

class Solution:
    from itertools import permutations
    def permute(self, nums: List[int]) -> List[List[int]]:

        out = []

        for perm in permutations(nums, len(nums)):
            out.append(perm)

        return out
        