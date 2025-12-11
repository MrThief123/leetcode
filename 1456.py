'''
Use sliding window technique to find maximum number of vowels in any substring of length k
Maintain a count of vowels in the current window
Slide the window by adding the next character and removing the first character of the previous window
Update the maximum count of vowels found so far
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = 0
        out = 0

        for i in range(k-1):
            if s[i] in vowels:
                count += 1
        
        out = count

        left = 0
        right = k - 1

        while right < n:
            if s[right] in vowels:
                count += 1

            out = max(out, count)

            if s[left] in vowels:
                count -= 1
            left += 1
            right += 1

        return out