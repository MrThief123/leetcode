"""
1207. Unique Number of Occurrences  [Easy]

Approach (count the counts):
  - Count how often each value appears.
  - Occurrences are unique iff the set of counts is as large as the dict of counts.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        counts = Counter(arr)  # value -> occurrences

        # Duplicate counts collapse in a set, shrinking its size
        return len(set(counts.values())) == len(counts.keys())
