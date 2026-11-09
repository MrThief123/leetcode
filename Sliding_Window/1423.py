'''
Using Prefix Sums to find the maximum score from card points
Calculate prefix sums to efficiently compute the sum of points from both ends of the array
Iterate through all possible distributions of k picks from the start and end of the array
Keep track of the maximum score encountered during the iterations
'''

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        left = k
        right = n
        out = float('-inf')

        prefix_sum = [0 for i in range(n+1)]

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + cardPoints[i]

        for i in range(k+1):
            total = prefix_sum[left] + prefix_sum[-1] - prefix_sum[right]
            out = max(out, total)
            left -= 1
            right -= 1

        return out