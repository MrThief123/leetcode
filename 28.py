'''
Use two-pointer technique to find the first occurrence of needle in haystack
Initialize two pointers, one for haystack and one for needle
Slide the haystack pointer and check for matches with needle
If a complete match is found, return the starting index
If no match is found, return -1
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left = 0
        right = 0

        h_len = len(haystack)
        n_len = len(needle)

        while left <= h_len - n_len:
            
            while right < n_len and haystack[left+right] == needle[right]:
                right += 1

            if right == n_len:
                return left
            else:
                right = 0
                left+=1
        return -1