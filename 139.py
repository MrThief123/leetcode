'''
139. Word Break
Use dynamic programming to determine if the string can be segmented into words from the dictionary.
Maintain a dp array where dp[i] indicates if s[start:i] can be segmented.
'''

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        # dp[i] = True if s[0:i] can be segmented
        dp = [True] + [False] * len(s)
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