"""
1376. Time Needed to Inform All Employees  [Medium]

Approach (BFS down the management tree):
  - Build manager -> direct-subordinates lists.
  - BFS from headID, tracking the cumulative time at which each manager
    finishes informing everyone below them (parent's cumulative time +
    that manager's own informTime).
  - The answer is the max cumulative time seen; leaf employees (who have
    informTime == 0, per the problem's guarantee) never push the max past
    what their manager already contributed, so only managers (keys in
    the subordinates map) need to be expanded/tracked.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        from collections import deque, defaultdict

        # manger: [staff, staff, staff]

        staff = defaultdict(list)


        for i in range(n):
            staff[manager[i]].append(i)

        out = informTime[headID]

        queue = deque([(headID, informTime[headID])])

        while queue:
            curr, time = queue.popleft()


            for i in staff[curr]:
                if i in staff:
                    new_time = informTime[i] + time
                    out = max(out, new_time)
                    queue.append((i, new_time))

        return out
