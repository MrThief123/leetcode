'''
Remove stars from a string by removing the closest non-star character to the left of each star
Use a stack to simulate the process
For each character in the string:
- If it's a star, pop from the stack (removing the closest non-star character to the left)
- Otherwise, push it onto the stack
Return the final string after processing all characters
'''

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)