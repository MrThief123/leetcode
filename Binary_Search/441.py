'''
441. Arranging Coins
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:        
        i=0
        while n>=0:
            i+=1
            n=n-i
        return i-1
