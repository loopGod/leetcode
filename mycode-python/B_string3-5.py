'''
3.5 Longest Palindromic Substring
描述
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length
of S is 1000, and there exists one unique longest palindromic substring.
'''
#48,65,97
class Solution:
    def LongestPalindromic(self,s):  
        n=len(s)                       
        f=[[False for i in range(n)] for j in range(n)]
        maxLen=1
        for i in range(n):
            f[i][i]=True
            for j in range(i+1):
                if j==i-1 and s[i]==s[j]:
                    f[j][i]=True
                    maxLen=max(maxLen,2)
                if j<i-1 and s[i]==s[j] and f[j+1][i-1]:
                    f[j][i]=True
                    maxLen=max(maxLen,i-j+1)
        return maxLen
#字符串是不可变，和元祖一样
s='banama banana'
muSolu=Solution()
new_node=muSolu.LongestPalindromic(s)
print(new_node)


