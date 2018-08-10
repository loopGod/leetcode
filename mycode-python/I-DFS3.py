'''
10.3 Unique Paths II
描述
Follow up for ”Unique Paths”:
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example,
There is one obstacle in the middle of a 3  3 grid as illustrated below.
[
[0,0,0],
[0,1,0],
[0,0,0]
]
The total number of unique paths is 2.
Note: m and n will be at most 100.
'''
#DFS
'''
class Solution(object):

    def DFS(self,board,m,n):
        if m>=lenm or n>=lenn or board[m][n]==1 or board[m][n]==1:
            return 0
        if m==lenm-1 and n==lenn-1:
            return 1
        board1=self.DFS(board,m+1,n)
        board2=self.DFS(board,m,n+1)
        res=board1+board2
        return res

    def Mysolve(self,board):  
        m,n=0,0
        res=self.DFS(board,m,n)
        return res

board=[[0,0,0],
       [0,1,0],
       [0,0,0]]
lenm,lenn=len(board),len(board[0])
mySolu=Solution()
res=mySolu.Mysolve(board)
print(res)
'''

#动态规划，状态转移方程为dp[i][j]=dp[i-1][j]+dp[i][j-1]。
class Solution:
    # @return an integer
    def uniquePaths(self,board):
        m,n=len(board),len(board[0])
        board[0][0]=1
        for i in range(1,n):
            if board[0][i]!=1:
                board[0][i]=board[0][i-1]
            else:
                board[0][i]=0
        for j in range(1,m):
            if board[j][0]!=1:
                board[j][0]=board[j-1][0]
            else:
                board[j][0]=0
        for i in range(1,m):
            for j in range(1,n):
                if board[i][j]==1:
                    board[i][j]=0
                else:
                    board[i][j]=board[i-1][j]+board[i][j-1]
        return board[m-1][n-1]

board=[[0,0,0],
       [0,1,0],
       [0,0,0]]
mySolu=Solution()
res=mySolu.uniquePaths(board)
print(res)