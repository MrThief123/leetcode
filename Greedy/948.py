"""
948. Bag of Tokens  [Medium]

Approach (greedy with a deque, two ends):
  - Sorted tokens: spend power on the cheapest token (face up, +1 score) and
    gain power by trading score for the most expensive token (face down).
  - `temp` is the current score; `out` is the best score seen at any moment.
  - Stop if we'd need to play face down with no score left (temp would be -1).

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        from collections import deque
        tokens.sort()

        out = 0   # best score achieved
        temp = 0  # current score

        tokens = deque(tokens)

        while tokens:
            if temp == -1:
                break  # played face down with no score: invalid, stop
            if power >= tokens[0]:
                # Play the cheapest token face up
                temp += 1
                out = max(out, temp)
                cost = tokens.popleft()
                power -= cost
            else:
                # Can't afford anything: sell score for the biggest token's power
                temp -= 1
                cost = tokens.pop()
                power += cost

        return out
