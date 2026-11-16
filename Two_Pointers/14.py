"""
14. Longest Common Prefix  [Easy]

Approach:
  - Start with the first word (cut to the shortest length) as the candidate prefix.
  - Compare every word to it; on a mismatch, shrink the prefix to the matching part.

Complexity: O(S) time (S = total characters), O(1) extra space
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # The prefix can't be longer than the shortest word (200 = problem max length)
        maxLen = 200
        for word in strs:
            maxLen = min(maxLen, len(word))

        best = strs[0][:maxLen]  # current candidate prefix
        for word in strs:
            if not best:
                break
            for i in range(maxLen):
                if word[i] != best[i]:
                    # Mismatch: keep only the part that still matches
                    best = word[:i]
                    maxLen = len(best)
                    break
        return best
