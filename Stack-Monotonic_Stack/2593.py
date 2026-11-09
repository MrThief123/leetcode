'''
2593. Find Score of an Array After Marking All Elements
Sort the array of numbers along with their indices. eg (1,1), (2,0), (2,5), (3,2), (4,3), (5,4)
Then, iterate through the sorted array and for each unvisited index, 
add the value to the score and mark the index and its neighbors as visited. 
Finally, return the score.
'''

class Solution:
    def findScore(self, nums: List[int]) -> int:
        pairs = sorted((v, i) for i, v in enumerate(nums))
        visited = [False] * len(nums)
        
        score = 0
        
        for val, idx in pairs:
            if visited[idx]:
                continue
            
            score += val
            
            visited[idx] = True
            if idx - 1 >= 0:
                visited[idx - 1] = True
            if idx + 1 < len(nums):
                visited[idx + 1] = True
        
        return score