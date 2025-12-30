'''
1052. Grumpy Bookstore Owner
Use a sliding window to find the optimal time to apply the technique
Calculate the base satisfaction from non-grumpy minutes
Iterate through the customers array, adjusting the extra satisfaction within the window
Keep track of the maximum extra satisfaction achievable
'''

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
                
        extra = 0
        best = 0

        for i in range(n):
            if grumpy[i] == 1:
                extra += customers[i]

            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    extra -= customers[i - minutes]

            best = max(best, extra)

        return base + best
