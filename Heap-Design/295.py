'''
295. Find Median from Data Stream
Use two heaps (a max-heap for the lower half of numbers and a min-heap for the upper half) 
to maintain a balanced partition of the data stream. 

When adding a number, compare it with the current median to decide which heap to add it to. 
After adding, ensure that the heaps are balanced (the size difference is at most 1). 

To find the median, check the sizes of the heaps: if they are equal, 
the median is the average of the two top elements; if one heap has more elements, 
the median is the top element of that heap.
'''

import bisect

class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.array, num)
        

    def findMedian(self) -> float:
        n = len(self.array)
        if not self.array:
            return null

        if n % 2 == 1:
            return self.array[n // 2]

        else:
            return (self.array[n//2] + self.array[n//2 - 1])/2




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()