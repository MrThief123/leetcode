class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        
        while len(s) > k:
            nex = ""

            i = 0

            while i < len(s):
                temp = 0
                for _ in range(k):
                    if i >= len(s):
                        break
                    else:
                        temp += int(s[i])
                        i += 1
                nex += str(temp)

            s = nex
                    
        return s

        