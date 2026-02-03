'''
3583. Count Special Triplets
Medium
Use a dictionary to store indices of each value, then for each nums[i], count valid j and k using binary search.
'''

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        from collections import defaultdict
        from bisect import bisect_left, bisect_right

        pos = defaultdict(list)
        n = len(nums)
        out = 0

        # store indices for each value
        for i, num in enumerate(nums):
            pos[num].append(i)

        for i in range(1, n - 1):
            target = nums[i] * 2
            if target not in pos:
                continue

            indices = pos[target]

            # count j < i
            left = bisect_left(indices, i)

            # count k > i
            right = len(indices) - bisect_right(indices, i)

            out += left * right

        return out % (pow(10,9) + 7)
