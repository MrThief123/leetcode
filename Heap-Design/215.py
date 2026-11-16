"""
215. Kth Largest Element in an Array  [Medium]

Approach (size-k min-heap):
  - Keep the k largest values seen so far in a min-heap; its root is the kth largest.
  - For each remaining number, if it beats the root, replace the root.

Complexity: O(n log k) time, O(k) space
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        heap = nums[:k]       # start with the first k values
        heapq.heapify(heap)   # min-heap: heap[0] is the smallest of the k

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                # Larger than the current kth largest: swap it in
                heapq.heapreplace(heap, nums[i])

        return heap[0]
