'''
13.7 Scramble String
描述
Given a string s1, we may represent it as a binary tree by pa
recursively.
Below is one possible representation of s1 = ”great”:
great
/ \
gr eat
/ \ / \
g r e at
/ \
a t
To scramble the string, we may choose any non-leaf node and swap its two children.
For example, if we choose the node ”gr” and swap its two children, it produces a scrambled string
”rgeat”.
rgeat
/ \
rg eat
/ \ / \
r g e at
/ \
a t
We say that ”rgeat” is a scrambled string of ”great”.
Similarly, if we continue to swap the children of nodes ”eat” and ”at”, it produces a scrambled string
”rgtae”.
rgtae
/ \
rg tae
/ \ / \
r g ta e
/ \
t a
We say that ”rgtae” is a scrambled string of ”great”.
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
解题思路：解码有多少种方法。一般求“多少”我们考虑使用dp。状态方程如下：

　　　　　当s[i-2:i]这两个字符是10~26但不包括10和20这两个数时，比如21，那么可以有两种编码方式（BA，U），所以dp[i]=dp[i-1]+dp[i-2]

　　　　　当s[i-2:i]等于10或者20时，由于10和20只有一种编码方式，所以dp[i]=dp[i-2]

　　　　   当s[i-2:i]不在以上两个范围时，如09这种，编码方式为0，而31这种，dp[i]=dp[i-1]。

　　　　   注意初始化时：dp[0]=1,dp[1]=1
'''
#递归法
class Solution():
    def isScramble(self, s1, s2):
        if s1==s2: return True
        if sorted(s1) != sorted(s2): return False  # "abcd", "bdac" are not scramble string
        length=len(s1)
        for i in range(1,length):
            if self.isScramble(s1[:i],s2[:i])        and self.isScramble(s1[i:],s2[i:]):        return True
            if self.isScramble(s1[:i],s2[length-i:]) and self.isScramble(s1[i:],s2[:length-i]): return True
        return False

A='great'
B = 'tearg'
mySolu=Solution()
maxV=mySolu.isScramble(A,B)
print(maxV)



