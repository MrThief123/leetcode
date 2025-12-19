'''
Determine if all rooms can be visited starting from room 0
Use a stack to perform depth-first search (DFS) through the rooms
Keep track of visited rooms using a set
Return true if all rooms have been visited, otherwise false
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        stack = []

        for i in rooms[0]:
            stack.append(i)

        visited.add(0)

        while stack:
            room = stack.pop()
            visited.add(room)

            for i in rooms[room]:
                if i not in visited:
                    stack.append(i)
                    
        return len(visited) == len(rooms)