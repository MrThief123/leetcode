'''
Check neighboring for 0's
Use min and max to avoid index errors
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True
        
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0 and flowerbed[max(i-1, 0)] == 0 and flowerbed[min(i+1, len(flowerbed) - 1)] == 0:
                flowerbed[i] = 1

                n -= 1

                if n == 0:
                    return True

        return False