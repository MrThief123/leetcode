'''
1209. Remove All Adjacent Duplicates in String II
Use a stack to keep track of characters and their counts. When the count reaches k, pop the character from the stack.
'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in s:
            if not stack:
                stack.append((i, 1))
            else:
                # same as prev value
                if i == stack[-1][0]:
                    stack[-1] = (i, stack[-1][1] + 1)

                    if stack[-1][1] == k:
                        stack.pop()
                # diff to prev
                else:
                    stack.append((i, 1))

        out = ""

        for c, i in stack:
            out += c*i
        
        return out
                    