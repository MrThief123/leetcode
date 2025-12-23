'''
Minimum Eating Speed
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during that hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        high = max(piles)

        if n == h:
            return high

        def valid(n):
            total = 0
            for i in piles:
                total += (i + n - 1) // n

            return total <= h

        low = 1

        while low != high:
            mid = (low+high)//2
            if valid(mid):
                high = mid
            else:
                low = mid + 1

        mid = (low+high)//2

        return mid
        

        
        
            
