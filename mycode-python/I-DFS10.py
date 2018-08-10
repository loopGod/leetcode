'''
10.10 Sudoku Solver
描述
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.
'''
class Solution:
    def __init__(self):
        self.res0=[]
    # @return a list of lists of string
    def sudokuSolver(self, board):
       
        def isValid(Sudo):
            lin=[[False for i in range(9)] for i in range(9)]
            col=[[False for i in range(9)] for i in range(9)]
            blo=[[False for i in range(9)] for i in range(9)]
            for i in range(9):
                for j in range(9):
                    if Sudo[i][j]!='.':
                        num=Sudo[i][j]-1
                        k=int(i/3)*3+int(j/3)
                        if lin[i][num] or col[j][num] or blo[k][num]:
                            return False
                        lin[i][num]=col[j][num]=blo[k][num]=True
            return True
        def dfs(board,res):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        #print(board)
                        for k in [1,2,3,4,5,6,7,8,9]:
                            board[i][j]=k
                            if isValid(board) and dfs(board,res):
                                if res!=[]:
                                    res.pop()
                                res.append(board)
                                return True
                            board[i][j]='.'
                        return False
            return True
        res=[]
        dfs(board,res)
        return res[0]

board=[[5  ,3  ,'.','.',7  ,'.','.','.','.'],
       [6  ,'.','.',1  ,9  ,5  ,'.','.','.'],
       ['.',9  ,8  ,'.','.','.','.',6  ,'.'],
       [8  ,'.','.','.',6  ,'.','.','.',3  ],
       [4  ,'.','.',8  ,'.',3  ,'.','.',1  ],
       [7  ,'.','.','.',2  ,'.','.','.',6  ],
       ['.',6  ,'.','.','.','.',2  ,8  ,'.'],
       ['.','.','.',4  ,1  ,9  ,'.','.',5  ],
       ['.','.','.','.',8  ,'.','.',7  ,9  ]]
mySolu=Solution()
res=mySolu.sudokuSolver(board)
print(res)

