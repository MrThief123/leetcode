"""
207. Course Schedule  [Medium]

Approach (Kahn's topological sort):
  - Edge prereq -> course; track each course's indegree (unmet prerequisites).
  - Repeatedly take courses with indegree 0 and release the courses depending on them.
  - If every course gets taken there is no cycle.

Complexity: O(V + E) time, O(V + E) space
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque

        # Build the graph and indegree array
        graph = defaultdict(list)  # prereq -> courses that depend on it
        indegree = [0] * numCourses

        # Populate the graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Initialize the queue with courses having no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        taken = 0  # courses completed

        # Process the courses
        while queue:
            curr = queue.popleft()
            taken += 1

            # Decrease the indegree of neighboring courses
            for nxt in graph[curr]:
                indegree[nxt] -= 1
                # If indegree becomes zero, add to queue
                if indegree[nxt] == 0:
                    queue.append(nxt)

        # Courses left over are stuck in a cycle
        return taken == numCourses
