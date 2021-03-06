'''
10.11 Word Search
描述
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed fromletters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighbouring. The same letter cell may not be used more than once.
For example, Given board =
[
["ABCE"],
["SFCS"],
["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''
class Solution:
    def __init__(self):
        self.res0=[]
    # @return a list of lists of string
    def wordSearch(self, board,word):
        def dfs(x, y, word):
            if len(word)==0: 
                return True
            #up
            if x>0 and board[x-1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x-1,y,word[1:]):
                    return True
                board[x][y]=tmp
            #down
            if x<len(board)-1 and board[x+1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x+1,y,word[1:]):
                    return True
                board[x][y]=tmp
            #left
            if y>0 and board[x][y-1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y-1,word[1:]):
                    return True
                board[x][y]=tmp
            #right
            if y<len(board[0])-1 and board[x][y+1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y+1,word[1:]):
                    return True
                board[x][y]=tmp
            return False
        
        board=list(list(i[0]) for i in board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if(dfs(i,j,word[1:])):
                        return True
        return False
        
#字符串不支持修改
board=[
["ABCE"],
["SFCS"],
["ADEE"]
]
word='ABCCEE'
mySolu=Solution()
res=mySolu.wordSearch(board,word)
print(res)


