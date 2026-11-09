'''
5. Longest Palindromic Substring
Use a center expansion technique to find palindromic substrings.
For each character (and the gap between characters) in the string, expand outwards while the characters on both sides are the same.
Keep track of the longest palindrome found during the expansion process.
This approach has a time complexity of O(n^2) and a space complexity of O(1) (ignoring the space used for the output string).   
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = 0
        out = ""
        n = len(s)

        for i in range(n):
            # check odd
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > best:
                    best = right - left + 1
                    out = s[left:right+1]
                left -= 1
                right += 1

            # check even
            left = i
            right = i+1

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > best:
                    best = right - left + 1
                    out = s[left:right+1]
                left -= 1
                right += 1
       
        return out