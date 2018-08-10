'''
2.1.14 Valid Sudoku
描述
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules
http://sudoku.com.au/TheRules.aspx .
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''

#康托编码
import math

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def ValidSudoku(self, Sudo):
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


sudu=[[5  ,3  ,'.','.',7  ,'.','.','.','.'],
      [6  ,'.','.',1  ,9  ,5  ,'.','.','.'],
      ['.',9  ,8  ,'.','.','.','.',6  ,'.'],
      [8  ,'.','.','.',6  ,'.','.','.',3  ],
      [4  ,'.','.',8  ,'.',3  ,'.','.',1  ],
      [7  ,'.','.','.',2  ,'.','.','.',6  ],
      ['.',6  ,'.','.','.','.',2  ,8  ,'.'],
      ['.','.','.',4  ,1  ,9  ,'.','.',5  ],
      ['.','.','.','.',8  ,'.','.',7  ,9  ]]
muSolu=Solution()
new_num=muSolu.ValidSudoku(sudu)
print(new_num) 

