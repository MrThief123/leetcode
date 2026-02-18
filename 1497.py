'''
1497. Check If Array Pairs Are Divisible by k
Given an array of integers arr of even length n and an integer k, 
return true if it is possible to reorder arr such that 
arr[2 * i + 1] is divisible by k with arr[2 * i] for every 0 <= i < n /
'''

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import defaultdict

        count = defaultdict(int)

        # Normalize remainders to be positive
        for num in arr:
            count[num % k] += 1

        # Case 1: remainder 0 must have even count
        if count[0] % 2 != 0:
            return False

        # Case 2: for each remainder r, count[r] must match count[k-r]
        for r in range(1, k):
            if count[r] != count[k - r]:
                return False

        return True