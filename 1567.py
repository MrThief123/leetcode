'''
1567. Maximum Length of Subarray With Positive Product
Split the array into subarrays separated by zeros
For each subarray, count the number of positive and negative numbers
If the count of negative numbers is even, the entire subarray has a positive product
If odd, exclude elements from the start or end up to the first negative number to maximize length
'''

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        out = 0
        queue, temp = []

        for num in nums:
            if num != 0:
                temp.append(num)
            else:
                if temp:
                    queue.append(temp)
                temp = []

        if nums[-1] != 0:
            queue.append(temp)

        for sub in queue:
            pos, neg = 0, 0

            for i in sub:
                if i > 0:
                    pos += 1
                else:
                    neg += 1

            if neg % 2 == 0:
                out = max(out, pos + neg)
            else:
                i = 0 
                while sub[i] > 0:
                    i += 1
                out = max(out, pos+neg-i-1)

                i = pos + neg - 1
                while sub[i] > 0:
                    i -= 1
                out = max(out, i)

        return out

