'''
2706. Buy Two Chocolates
Keep track of 2 smallest prices. 
If the sum of the 2 smallest prices is less than or equal to the money we have, 
    return the remaining money after buying the chocolates. Otherwise, 
    return the original amount of money.
'''

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a, b = float('inf'), float('inf')

        for i in prices:
            if i <= a:
                b = a
                a = i
            elif i < b:
                b = i

        if a + b <= money:
            return money - a - b
        return money