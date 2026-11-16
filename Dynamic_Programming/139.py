"""
139. Word Break  [Medium]

Approach (DP over prefixes):
  - dp[i] is True if the first i characters can be segmented into dictionary words.
  - dp[i] is True if some word ends at i and dp[i - len(word)] is already True.

Complexity: O(n * w * L) time (w words, L max word length), O(n) space
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        # dp[i] = True if s[0:i] can be segmented
        dp = [True] + [False] * len(s)  # empty prefix is trivially valid
        for i in range(1, len(s) + 1):
            for word in wordDict:
                start = i - len(word)
                # check if the word fits and previous segment is valid
                if start >= 0 and dp[start] and s[start:i] == word:
                    dp[i] = True
                    break
        #                   l  e  e  t  c  o  d  e
        # example: dp = [T, F, F, F, T, F, F, F, T] for s = "leetcode" and wordDict = ["leet", "code"]

        return dp[-1]
