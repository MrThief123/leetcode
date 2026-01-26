'''
1200. Minimum Absolute Difference
Sort the array and find the minimum absolute difference between consecutive elements.
Maintain a list of pairs that have this minimum difference.
'''

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        best = float('inf')
        out = []
        arr.sort()

        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i+1])

            if diff < best:
                best = diff
                out = [[arr[i], arr[i+1]]]
            elif diff == best:
                out.append([arr[i], arr[i+1]])

        return out