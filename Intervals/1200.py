"""
1200. Minimum Absolute Difference  [Easy]

Approach:
  - After sorting, the minimum difference must be between adjacent elements.
  - Track the smallest difference, resetting the result list whenever a smaller one appears.

Complexity: O(n log n) time, O(1) extra space (excluding output)
"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        best = float('inf')  # smallest gap so far
        out = []             # pairs achieving that gap
        arr.sort()

        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i+1])

            if diff < best:
                best = diff
                out = [[arr[i], arr[i+1]]]  # new best: discard earlier pairs
            elif diff == best:
                out.append([arr[i], arr[i+1]])

        return out
