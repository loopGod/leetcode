'''
10.4 N-Queens
描述
The n-queens puzzle is the problem of placing n queens on an nn chessboard such that no two queens
attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.'
oth indicate a queen and an empty space respectively.
For example, There exist two distinct solutions to the 4-queens puzzle:
[
[".Q..", // Solution 1
"...Q",
"Q...",
"..Q."],
["..Q.", // Solution 2
"Q...",
"...Q",
".Q.."]
]
'''
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k):
                if board[i]==j or abs(k-i)==abs(board[i]-j):
                    return False
            return True
        def dfs(depth, valuelist):
            if depth==n: res.append(valuelist); return
            for i in range(n):
                if check(depth,i): 
                    board[depth]=i
                    s='.'*n
                    dfs(depth+1, valuelist+[s[:i]+'Q'+s[i+1:]])
        board=[-1 for i in range(n)]
        res=[]
        dfs(0,[])
        return res

mySolu=Solution()
res=mySolu.solveNQueens(4)
print(res)