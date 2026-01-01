'''
Docstring for 1465
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
Sort the horizontal and vertical cuts
Calculate the maximum distance between consecutive horizontal cuts
Calculate the maximum distance between consecutive vertical cuts
Multiply the two maximum distances to get the area of the largest piece
Return the area 
'''

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        max_w = 0
        max_h = 0

        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i-1])

        return max_w*max_h % (pow(10, 9) + 7)