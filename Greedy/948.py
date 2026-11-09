'''
948. Bag of Tokens
You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).
Your goal is to maximize your total score by potentially playing any number of tokens. Each token can be played at most once and in one of two ways:
- If you have at least tokens[i] power, you can play the ith token face up, losing tokens[i] power and gaining 1 score.
- If you have at least 1 score, you can play the ith token face down, gaining tokens[i] power and losing 1 score.
Return the largest possible score you can achieve after playing any number of tokens.
'''

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        from collections import deque
        tokens.sort()

        out = 0
        temp = 0

        tokens = deque(tokens)

        while tokens:
            if temp == -1:
                break
            if power >= tokens[0]:
                temp += 1
                out = max(out, temp)
                cost = tokens.popleft()
                power -= cost
            else:
                temp -= 1
                cost = tokens.pop()
                power += cost
        
        return out
