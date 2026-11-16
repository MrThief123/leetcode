"""
2024. Maximize the Confusion of an Exam  [Medium]

Approach (sliding window, run once per target letter):
  - For a target letter, the window may contain at most k answers that differ
    (those get flipped to the target).
  - Answer = best of the 'T' run and the 'F' run.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def sliding(target):
            left = 0
            right = 0
            best = 0

            n = len(answerKey)

            flip = 0  # answers in the window that differ from target

            for right in range(n):
                if answerKey[right] != target:
                    flip += 1

                # Too many flips needed: shrink from the left
                while flip > k:
                    if answerKey[left] != target:
                        flip -= 1
                    left += 1

                best = max(best, right - left + 1)

            return best

        return max(sliding('T'), sliding('F'))
