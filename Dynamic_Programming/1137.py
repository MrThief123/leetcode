'''
Calculate the n-th Tribonacci number using dynamic programming
Initialize a list to store Tribonacci numbers up to n
Set the base cases for T(0), T(1), and T(2)
Iteratively compute Tribonacci numbers from T(3) to T(n) using the relation T(n) = T(n-1) + T(n-2) + T(n-3) 
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0 for i in range(38)]

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]