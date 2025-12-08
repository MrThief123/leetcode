'''
Use two-pointer technique to find the maximum area of water container
Initialize two pointers at the beginning and end of the height array
Calculate the area formed by the lines at the two pointers
Move the shorter line inward to potentially find a taller line
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        point1 = 0
        point2 = len(height) - 1

        max_cap = 0 

        while point1 < point2:
            area = (point2 - point1) * min(height[point1], height[point2])
            max_cap = max(area, max_cap)

            if height[point1] < height[point2]:
                point1 += 1
            else:
                point2 -= 1

        return max_cap