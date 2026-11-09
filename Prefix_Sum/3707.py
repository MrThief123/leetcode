'''
3707. Equal Score Substrings
Use prefix sum to calculate the score
'''

class Solution:
    def scoreBalance(self, s: str) -> bool:
        BUFFER = 96
        n = len(s)

        prefix_sum = [0 for i in range(n+1)]

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + ord(s[i]) - BUFFER

        for i in range(n):
            if prefix_sum[-1] - prefix_sum[i] == prefix_sum[i]:
                return True
        return False