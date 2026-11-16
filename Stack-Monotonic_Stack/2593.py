"""
2593. Find Score of an Array After Marking Elements  [Medium]

Approach (sort + visited array):
  - Sort (value, index) pairs, e.g. (1,1), (2,0), (2,5), (3,2), (4,3), (5,4).
    Ties break by smaller index automatically.
  - Take each unmarked element, add its value, and mark it and both neighbours.

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def findScore(self, nums: List[int]) -> int:
        pairs = sorted((v, i) for i, v in enumerate(nums))  # (value, original index)
        visited = [False] * len(nums)

        score = 0

        for val, idx in pairs:
            if visited[idx]:
                continue  # already marked by a smaller neighbour

            score += val

            # Mark the chosen element and its neighbours
            visited[idx] = True
            if idx - 1 >= 0:
                visited[idx - 1] = True
            if idx + 1 < len(nums):
                visited[idx + 1] = True

        return score
