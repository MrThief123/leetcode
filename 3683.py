'''
3683. Earliest Possible Completion Time of All Tasks
'''

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        best = float('inf')

        for start, time in tasks:
            best = min(best, start+time)
        return best