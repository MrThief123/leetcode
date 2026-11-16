"""
2344. Minimum Deletions to Make Array Divisible  [Hard]

Approach:
  - We need the smallest value in nums that divides every element of numsDivide.
  - Delete all smaller values first, so the answer is how many elements are smaller.
  - Count occurrences, scan candidates in ascending order, and accumulate the
    counts of those that fail.

Complexity: O(n log n + u * m) time (u = distinct values, m = len(numsDivide)),
            O(n) space
"""

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        from collections import Counter

        counts = Counter(nums)  # value -> occurrences

        numsDivide = list(set(numsDivide))  # duplicates add no information

        out = 0  # deletions made so far

        # A divisor can't exceed the smallest target, so filter then sort ascending
        possible = sorted([i for i in counts.keys() if i <= min(numsDivide)])

        for i in possible:
            p = True
            for j in numsDivide:
                if j%i != 0:
                    p = False
                    break

            if p:
                return out
            else:
                # i is unusable: it and its copies must be deleted
                out += counts[i]

        return -1
