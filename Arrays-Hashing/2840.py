"""
2840. Check if Strings Can Be Made Equal With Operations II  [Medium]

Approach:
  - A swap only moves characters between positions of the same parity.
  - So the letters at even positions must match as a multiset, same for odd.
  - Add counts from s1 and subtract counts from s2 per parity; all must be zero.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        even = defaultdict(int)  # net letter counts at even indices
        odd = defaultdict(int)   # net letter counts at odd indices

        for i in range(len(s1)):
            if i%2 == 0:
                even[s1[i]] += 1
                even[s2[i]] -= 1
            else:
                odd[s1[i]] += 1
                odd[s2[i]] -= 1

        # Any non-zero entry means the multisets differ
        for i in even.values():
            if i != 0:
                return False
        for i in odd.values():
            if i != 0:
                return False
        return True
