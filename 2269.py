'''
Given an integer num and an integer k, 
return the number of substrings of num that are divisible by num. 
A substring is a contiguous sequence of characters in a string.
'''

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        out = 0
        num_s = str(num)

        for i in range(len(num_s) - k + 1):
            temp = int(num_s[i:i+k])
            if temp != 0 and num % temp == 0:
                out += 1

        return out
