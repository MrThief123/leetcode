'''
+Calculate the largest altitude reached during the trip using prefix sums
+Initialize a prefix sum array with the starting altitude of 0
+Iterate through the gain array to compute the altitude at each point
+Return the maximum altitude from the prefix sum array
'''

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [0 for i in range(len(gain)+1)]

        for i in range(len(gain)):
            prefix_sum[i+1] = prefix_sum[i] + gain[i]
            
        return max(prefix_sum)