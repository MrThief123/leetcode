"""
2269. Find the K-Beauty of a Number  [Easy]

Approach:
  - Convert num to a string and slide a window of length k.
  - Count windows whose integer value is non-zero and divides num.

Complexity: O(n * k) time (n = digits), O(n) space
"""

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        out = 0
        num_s = str(num)

        for i in range(len(num_s) - k + 1):
            temp = int(num_s[i:i+k])  # current window as an integer
            if temp != 0 and num % temp == 0:  # skip 0 to avoid division by zero
                out += 1

        return out
