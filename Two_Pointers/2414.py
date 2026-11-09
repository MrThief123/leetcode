'''
2414. Length of the Longest Alphabetical Continuous Substring
Use a sliding window approach to find the longest continuous substring where each character is exactly one greater than the previous character.
Maintain a variable to keep track of the current substring and its length.
Iterate through the string character by character, comparing each character with the last character of the current substring.
If the current character is one greater than the last character of the substring, append it to the substring.
If not, reset the substring to start from the current character.
Keep track of the maximum length of the substring throughout the process.
'''

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        out = 0
        substring = "" 

        for i in s:
            while substring and ord(i) - ord(substring[-1]) != 1:
                substring = substring[:-1]
            substring += i
            out = max(out, len(substring))
                    
        return out