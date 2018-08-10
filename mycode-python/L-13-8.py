'''
13.8 Minimum Path Sum
描述
Given a m  n grid filled with non-negative numbers, find a path from top left to bottom right which
minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time
'''
#递归法
class Solution():
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        ans = [[0 for i in range(n)] for j in range(m)]
        ans[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i !=0 and j == 0:
                    ans[i][j] = ans[i-1][j] + grid[i][j]
                elif i == 0 and j != 0:
                    ans[i][j] = ans[i][j - 1] + grid[i][j]
                elif i != 0 and j != 0:
                    ans[i][j] = min(ans[i - 1][j],ans[i][j - 1]) + grid[i][j]
        return ans[m - 1][n - 1]

grid=[[2,4,8],
	  [4,2,6],
      [7,5,4]]
mySolu=Solution()
maxV=mySolu.minPathSum(grid)
print(maxV)



