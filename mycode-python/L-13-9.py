'''
13.9 Edit Distance
描述
Given two words word1 and word2, find the minimum number of steps required to convert word1 to
word2. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:

分析
设状态为 f[i][j]，表示 A[0,i]和 B[0,j]之间的最小编辑距离。设 A[0,i]的形式是 str1c，
B[0,j]的形式是 str2d，
1. 如果 c==d，则 f[i][j]=f[i-1][j-1]；
2. 如果 c!=d，
(a) 如果将 c替换成 d，则 f[i][j]=f[i-1][j-1]+1；
(b) 如果在 c后面添加一个 d，则 f[i][j]=f[i][j-1]+1；
(c) 如果将 c删除，则 f[i][j]=f[i-1][j]+1；
'''
#DP
class Solution():
    def editDistance(self, word1,word2):
        m,n = len(word1),len(word2)
        ans = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            ans[i][n] = m - i
        for i in range(n + 1):
            ans[m][i] = n - i
        m -= 1;n -= 1
        while m >= 0:
            t = n
            while t >= 0:
                if word1[m] == word2[t]:
                    ans[m][t] = ans[m + 1][t + 1]
                else:
                    ans[m][t] = min(ans[m][t+1],ans[m+1][t],ans[m+1][t+1]) + 1
                t -= 1
            m -= 1
        return ans[0][0]

word1='wordL'
word2='worldL'
mySolu=Solution()
maxV=mySolu.editDistance(word1,word2)
print(maxV)



