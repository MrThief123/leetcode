'''
Simulate the asteroid collisions using a stack
Iterate through each asteroid in the input list
Check the conditions for collisions and update the stack accordingly
Return the final state of the stack after all collisions
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            if (stack and stack[-1] <= 0) or (not stack) or (stack[-1] >= 0 and i >= 0):
                stack.append(i) 
            elif stack[-1] > 0 and i < 0:
                add = False
                while stack and stack[-1] > 0:
                    if stack[-1] > abs(i):
                        add = False
                        break
                    elif stack[-1] < abs(i):
                        stack.pop()
                        add = True
                    elif stack[-1] == abs(i):
                        stack.pop()
                        add = False
                        break
                if add:
                    stack.append(i)

        return stack