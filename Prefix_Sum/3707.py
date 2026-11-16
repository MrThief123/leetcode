"""
3707. Equal Score Substrings  [Easy]

Approach (prefix sum):
  - Score each letter as its alphabet position (a=1 ... z=26; ord('a') - 96).
  - A split works when the prefix sum equals the remaining sum.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def scoreBalance(self, s: str) -> bool:
        BUFFER = 96  # ord('a') - 1, so 'a' scores 1
        n = len(s)

        prefix_sum = [0 for i in range(n+1)]

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + ord(s[i]) - BUFFER

        # Left sum == total - left sum
        for i in range(n):
            if prefix_sum[-1] - prefix_sum[i] == prefix_sum[i]:
                return True
        return False
