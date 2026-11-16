"""
77. Combinations  [Medium]

Approach:
  - Choose k numbers from 1..n with itertools.combinations and convert each tuple to a list.

Complexity: O(C(n, k) * k) time and space
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return [list(c) for c in combinations(range(1, n + 1), k)]
