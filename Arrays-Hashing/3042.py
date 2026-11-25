"""
3042. Count Prefix and Suffix Pairs I  [Easy]

Approach (brute force):
  - words[i] is a prefix-and-suffix pair with words[j] (i < j) when
    words[j] starts with and ends with words[i].
  - Check every pair with str.startswith / str.endswith.

Complexity: O(n^2 * m) time (m = max word length), O(1) extra space
"""

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(i, j):
            if j.startswith(i) and j.endswith(i):
                return True
            return False

        out = 0
        n = len(words)
        for i in range(n-1):
            for j in range(i+1,n):
                if isPrefixAndSuffix(words[i], words[j]):
                    out +=1

        return out
