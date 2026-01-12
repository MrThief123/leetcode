'''
3663. Least Frequent Digit in an Integer
Count the frequency of each digit in the integer. Return the digit with the lowest frequency. If multiple digits have the same lowest frequency, return the smallest digit among them.
'''

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        from collections import defaultdict

        count = defaultdict(int)

        for i in str(n):
            count[i] += 1

        out = (float('inf'), float('inf'))  

        for key, value in count.items():
            out = min(out, (value, int(key)))

        return out[1]   