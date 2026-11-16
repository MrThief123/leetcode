"""
23. Merge k Sorted Lists  [Hard]

Approach (min-heap of all values):
  - Push every node value from every list into a min-heap.
  - Pop in sorted order and build a fresh linked list.
  - (A heap of the k list heads would use O(k) space instead of O(N).)

Complexity: O(N log N) time, O(N) space (N = total nodes)
"""

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        mylist = []  # min-heap of values

        # Collect every value from every list
        for head in lists:
            while head:
                heapq.heappush(mylist, head.val)
                head = head.next

        start = ListNode()  # dummy head of the result

        head = start

        # Pop values in ascending order to build the merged list
        while mylist:
            val = heapq.heappop(mylist)

            head.next = ListNode()
            head = head.next

            head.val = val

        return start.next
