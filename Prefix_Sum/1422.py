'''
1422. Maximum Score After Splitting a String
Use prefix sums to count 0s on the left and 1s on the right for each split point.
'''

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefix_left = [0 for i in range(n-1)]
        prefix_right = [0 for i in range(n-1)]
        count = int(s[-1])

        if s[0] == '0':
            prefix_left[0] = 1
        else:
            prefix_right[0] = 1

        for i in range(1, n-1, 1):
            prefix_left[i] = prefix_left[i-1]
            prefix_right[i] = prefix_right[i-1]

            if s[i] == '0':
                prefix_left[i] += 1
            else:
                prefix_right[i] += 1

        count += prefix_right[-1]

        out = 0

        for i in range(len(prefix_right)):
            out = max(out, prefix_left[i] + count - prefix_right[i])

        return out