'''
Two pointer approach
Use a set to store characters in the current substring
Move right pointer to expand the window
If a duplicate character is found, move the left pointer to shrink the window until the duplicate is removed
Update the maximum length of the substring found so far
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0

        charSet = set()

        if len(s) <= 1:
            return len(s)

        left = 0

        for  right in range(len(s)):
            
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])

            best = max(best, right - left + 1)

        return best