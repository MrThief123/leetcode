'''
3127. Make a Square with same color
Use a dictionary to assign a value to each color.
Then, iterate through the grid and calculate the sum of the values for each 2x2 square. 
If the absolute value of the sum is 2 or 4, then we can make a square with the same color by changing one of the colors in the square. 
If we find such a square, we return True. If we finish iterating through the grid and do not find such a square, we return False.
'''

from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        c = {'B': 1,
            'W': -1}


        n = len(grid)
        m = len(grid[0])

        if n < 2 or m < 2:
            return False 


        for i in range(n-1):
            for j in range(m-1):
                temp = c[grid[i][j]] + c[grid[i+1][j]] + c[grid[i][j+1]] + c[grid[i+1][j+1]]

                if abs(temp) in [2, 4]:
                    return True
        return False