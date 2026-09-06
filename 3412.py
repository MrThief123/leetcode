'''
a: [1, 6,10]
etc

check if we have seen the flip and add the score
'''

class Solution:
    def calculateScore(self, s: str) -> int:
        def fliper(c):
            return chr(122 - ord(c) + 97)

        from collections import defaultdict

        score = 0
        mydict = defaultdict(list)

        for i, c in enumerate(s):
            flip = fliper(c)
            if flip in mydict and mydict[flip]:
                score += i - mydict[flip].pop()
            else:
                mydict[c].append(i)
        
        return score