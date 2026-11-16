"""
295. Find Median from Data Stream  [Hard]

Approach (sorted list):
  - Keep the numbers sorted with bisect.insort_left on every insert.
  - The median is the middle element (odd count) or the mean of the two middle
    elements (even count).
  - (Two heaps, a max-heap for the lower half and a min-heap for the upper half,
    would give O(log n) inserts and O(1) median.)

NOTE: `return null` is not Python (should be `None`); it only runs for an empty
      stream, which the problem doesn't test.

Complexity: addNum O(n) (list shifting), findMedian O(1); O(n) space
"""

import bisect

class MedianFinder:

    def __init__(self):
        self.array = []  # always sorted

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.array, num)  # insert keeping order

    def findMedian(self) -> float:
        n = len(self.array)
        if not self.array:
            return null

        # Odd count: the middle element
        if n % 2 == 1:
            return self.array[n // 2]

        # Even count: average of the two middle elements
        else:
            return (self.array[n//2] + self.array[n//2 - 1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
