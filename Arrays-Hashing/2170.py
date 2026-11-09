class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        from collections import defaultdict

        # key: even, odd
        mydict = defaultdict(lambda: [0, 0])


        for i, n in enumerate(nums):
            mydict[n][i%2] += 1

            
        best_even = (0, 0)
        best_odd = (0, 0)

        best2_even = (0, 0)
        best2_odd = (0, 0)

        # Get top 2 scores for even and odd positions in a single pass
        for key, value in mydict.items():
            even_val, odd_val = value[0], value[1]

            # 1. Update even rankings
            if even_val > best_even[1]:
                best2_even = best_even        # The old best becomes second best
                best_even = (key, even_val)   # Current becomes the new best
            elif even_val > best2_even[1]:
                best2_even = (key, even_val)  # Current beats second best only

            # 2. Update odd rankings
            if odd_val > best_odd[1]:
                best2_odd = best_odd          # The old best becomes second best
                best_odd = (key, odd_val)     # Current becomes the new best
            elif odd_val > best2_odd[1]:
                best2_odd = (key, odd_val)    # Current beats second best only


        n = len(nums)

        # if same key ie [2 2 2 2 2 2 2 2 2 1]
        if best_even[0] == best_odd[0]:
            best = max(best_even[1]+best2_odd[1], best_odd[1]+best2_even[1])
            return n - best
        else:
            return n - best_even[1] - best_odd[1]
