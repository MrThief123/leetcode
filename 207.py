'''
207. Course Schedule
Use topological sort (Kahn's algorithm) to determine if all courses can be finished.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        
        # Build the graph and indegree array
        graph = defaultdict(list)
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

        taken = 0

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

        return taken == numCourses
