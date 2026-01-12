'''
1518. Water Bottles
Keep drinking from full bottles and exchanging empty bottles for full ones until you can no longer do so
'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        out = numBottles

        while numBottles // numExchange > 0:
            out += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange

        return out