'''
3174. Remove Digits From String to Make It Good
Use a stack to keep track of the characters in the string.
Iterate through the string and for each character, if it is a digit and the top of the stack is an alphabet, pop the top of the stack. Otherwise, push the character onto the stack. 
Finally, join the characters in the stack to form the output string.
'''

class Solution:
    def clearDigits(self, s: str) -> str:
        out = []

        for i in s:
            if i.isalpha():
                out.append(i)
            else:
                if out and out[-1].isalpha():
                    out.pop()
        return ''.join(out)