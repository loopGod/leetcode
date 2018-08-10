'''
9.3 Surrounded Regions
描述
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region .
For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
分析
广搜。从上下左右四个边界往里走，凡是能碰到的'O'，都是跟边界接壤的，应该保留。
代码
'''
class Solution(object):
    def solve(self, board):
 
        def fill(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or board[x][y] != 'O':
                return
            queue.append((x, y))
            board[x][y] = 'D'

        def bfs(x, y):
            if board[x][y] == 'O':
                fill(x, y)
            while queue:
                cur = queue.pop(0)
                i = cur[0]
                j = cur[1]
                fill(i + 1, j)
                fill(i - 1, j)
                fill(i, j + 1)
                fill(i, j - 1)

        if len(board) == 0:
            return
        m = len(board)
        n = len(board[0])
        queue = []

        for i in range(n):
            bfs(0, i)
            bfs(m - 1, i)
        for j in range(1, m - 1):
            bfs(j, 0)
            bfs(j, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

board=[ ['X','X','X','X'],
        ['X','O','O','X'],
        ['X','X','O','X'],
        ['X','O','X','X'] ]
mySolu=Solution()
mySolu.solve(board)
print(board)
