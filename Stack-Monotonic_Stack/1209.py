"""
1209. Remove All Adjacent Duplicates in String II  [Medium]

Approach (stack of (char, run length)):
  - Extend the run if the character matches the top; start a new run otherwise.
  - When a run reaches k, pop it (removing the k duplicates).
  - Rebuild the string from the surviving runs.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # entries of (character, consecutive count)

        for i in s:
            if not stack:
                stack.append((i, 1))
            else:
                # same as prev value
                if i == stack[-1][0]:
                    stack[-1] = (i, stack[-1][1] + 1)

                    # k in a row: remove them all
                    if stack[-1][1] == k:
                        stack.pop()
                # diff to prev
                else:
                    stack.append((i, 1))

        out = ""

        for c, i in stack:
            out += c*i

        return out
