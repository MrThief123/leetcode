"""
1887. Reduction Operations to Make Array Elements Equal  [Medium]

Approach:
  - Each element must step down through every smaller distinct value.
  - So an element's cost is the rank of its value among the sorted distinct values.
  - Sum the ranks of all elements.

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        temp = sorted(list(set(nums)))  # distinct values, ascending
        out = 0
        mydict = {}  # value -> rank (0 = smallest)

        for i, n in enumerate(temp):
            mydict[n] = i

        # Each element needs `rank` reductions to reach the minimum
        for i in nums:
            out += mydict[i]

        return out
