'''
2486. Append Characters to String to Make Subsequence
Use two pointers to check how many characters of t are already a subsequence of s, then return the remaining characters needed.
'''

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        i = 0
        j = 0

        while i < n and j < m:
            if s[i] == t[j]:
                j += 1
            i +=1 
        
        return m - j