'''
3100. Maximum Bottles Drunk
Keep drinking from full bottles and exchanging empty bottles for full ones until you can no longer do so
'''

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        out = numBottles
        
        while numBottles >= numExchange:
            temp = 0
            while numBottles >= numExchange:
                temp += 1
                out += 1
                numBottles = numBottles - numExchange
                numExchange += 1
        
            numBottles += temp

        return out
        