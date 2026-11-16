"""
841. Keys and Rooms  [Medium]

Approach (iterative DFS):
  - Start in room 0; the stack holds rooms whose keys we've collected.
  - Visit rooms, picking up their keys. All rooms are reachable if we visit len(rooms).

Complexity: O(rooms + keys) time, O(rooms) space
"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        stack = []  # rooms we know the key for but haven't entered

        # Keys found in room 0
        for i in rooms[0]:
            stack.append(i)

        visited.add(0)

        while stack:
            room = stack.pop()
            visited.add(room)

            # Collect this room's keys
            for i in rooms[room]:
                if i not in visited:
                    stack.append(i)

        return len(visited) == len(rooms)
