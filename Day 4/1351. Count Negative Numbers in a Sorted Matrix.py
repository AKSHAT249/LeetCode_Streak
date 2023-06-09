class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])

        count_neg = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j]<0:
                    count_neg+=1
        return count_neg
