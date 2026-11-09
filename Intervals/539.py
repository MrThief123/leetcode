'''
539. Minimum Time Difference
Convert time points to minutes, sort them, and find the minimum difference between consecutive times, considering
'''

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []

        for t in timePoints:
            h, m = map(int, t.split(":"))
            minutes.append(h * 60 + m)

        minutes.sort()

        ans = 1440  

        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])

        ans = min(ans, 1440 - minutes[-1] + minutes[0])

        return ans
