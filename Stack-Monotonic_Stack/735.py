"""
735. Asteroid Collision  [Medium]

Approach (stack simulation):
  - Positive asteroids move right, negative move left; only (+ then -) collide.
  - Push when no collision is possible.
  - For an incoming negative hitting a positive top: pop smaller ones, destroy
    both on a tie, or discard the incoming one if the top is larger.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            # No collision: empty stack, top moving left, or both moving right
            if (stack and stack[-1] <= 0) or (not stack) or (stack[-1] >= 0 and i >= 0):
                stack.append(i)
            # Collision: top moves right, incoming moves left
            elif stack[-1] > 0 and i < 0:
                add = False  # does the incoming asteroid survive?
                while stack and stack[-1] > 0:
                    if stack[-1] > abs(i):
                        add = False  # incoming is destroyed
                        break
                    elif stack[-1] < abs(i):
                        stack.pop()  # top destroyed, keep checking
                        add = True
                    elif stack[-1] == abs(i):
                        stack.pop()  # both destroyed
                        add = False
                        break
                if add:
                    stack.append(i)

        return stack
