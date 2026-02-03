'''
2024. Maximize the Confusion of an Exam
Medium
Sliding window to count max number of T's or F's with at most k flips.
'''

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def sliding(target):
            left = 0
            right = 0
            best = 0

            n = len(answerKey)

            flip = 0

            for right in range(n):
                if answerKey[right] != target:
                    flip += 1
                
                while flip > k:
                    if answerKey[left] != target:
                        flip -= 1
                    left += 1

                best = max(best, right - left + 1)

            return best

        return max(sliding('T'), sliding('F'))

