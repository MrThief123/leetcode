'''
Use stack to validate parentheses
Push opening brackets onto the stack
For closing brackets, check if the top of the stack matches the corresponding opening bracket
If it matches, pop the stack; otherwise, return false
At the end, if the stack is empty, all brackets were matched correctly
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        lookup = {

            ')': '(',
            '}': '{',
            ']': '['
        }

        count = 0

        for i in s:
            # opening bracket
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if stack and lookup[i] == stack[-1]:
                    stack.pop()
                    count += 1
                else:
                    return False
                
        if len(s) / 2.0 == count:
            return True 
            
        return False
        