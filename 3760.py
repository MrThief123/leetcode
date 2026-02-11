'''
Given a string s, return the maximum number of distinct characters that can be used to make a string t such that t is a subsequence of s.
'''

class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))