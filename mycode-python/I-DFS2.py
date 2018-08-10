'''
10.2 Unique Paths
描述
A robot is located at the top-left corner of a m  n grid (marked ’Start’ in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid (marked ’Finish’ in the diagram below).
How many possible unique paths are there?
图 10-1 Above is a 3  7 grid. How many possible unique paths are there?
Note: m and n will be at most 100.
'''
#DFS
'''
class Solution(object):
	"""docstring for Solution"""
	def __init__(self):
		pass

	def DFS(self,m,n):
		if m<=0 or n<=0:
			return 0
		if m==1 and n==1:
			return 1
		res=self.DFS(m-1, n)+self.DFS(m, n-1)
		return res

mySolu=Solution()
res=mySolu.DFS(3, 3)
print(res)
'''
#动态规划，状态转移方程为dp[i][j]=dp[i-1][j]+dp[i][j-1]。
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 and n == 1:
            list = [[1]]
        elif m == 1 and n > 1:
            list = [[1 for i in range(n)]]
        elif m > 1 and n == 1:
            list = [[1] for i in range(m)]
        else:
            list = [[0 for i in range(n)] for i in range(m)]
            for i in range(0, n):
                list[0][i] = 1
            for i in range(0, m):
                list[i][0] = 1
            for i in range(1, m):
                for j in range(1, n):
                    list[i][j] = list[i-1][j] + list[i][j-1]
        return list[m-1][n-1]
		