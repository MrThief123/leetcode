'''
Split the string into words
Apped each word at the front of the output string (like a stack)
Strip the trailing space
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()

        out = ""

        for word in words:

            out = word + " " + out

        return out.strip()