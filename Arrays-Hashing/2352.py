'''
Count the number of pairs of rows and columns in a grid that are equal
Use a hash map to count occurrences of each row. The key is a tuple representing the row, and the value is the count of that row.
For each column, construct the column as a tuple and check if it exists in the row hash map
If it exists, add the count from the row hash map to the result
'''

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        row_hash = defaultdict(int)
        n = len(grid)
        out = 0

        for i in grid:
            row_hash[tuple(i)] += 1

        temp_list = [0 for i in range(n)]

        for x in range(n):
            for y in range(n):
                temp_list[y] = grid[y][x] 
            if tuple(temp_list) in row_hash:
                out += row_hash[tuple(temp_list)]
        return out