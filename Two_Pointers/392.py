'''
Use two-pointer technique to check if string s is a subsequence of string t
Initialize a pointer for s and iterate through t
When characters match, move the pointer for s
If the pointer for s reaches the end, s is a subsequence of t
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        curr = 0
        i = 0

        while i < len(t):
            if s[curr] == t[i]:
                curr += 1
                if curr == n:
                    return True
            i += 1
        return False
