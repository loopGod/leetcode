'''
10.9 Generate Parentheses
描述
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"
分析
小括号串是一个递归结构，跟单链表、二叉树等递归结构一样，首先想到用递归。
一步步构造字符串。当左括号出现次数 < n 时，就可以放置新的左括号。当右括号出现次数小
于左括号出现次数时，就可以放置新的右括号。
'''
class Solution:
    def __init__(self):
        self.res0=[]
    # @return a list of lists of string
    def generateParentheses(self, n):
        def generaterIter(res,sub,left,right):
            if left==0 and right==0:
                res.append(sub)
            if left>0:
                generaterIter(res,sub+'(', left-1, right)
            if right>0 and left<right:
                generaterIter(res,sub+')', left, right-1)
        res=[]
        generaterIter(res, '', n, n)
        return res
        

mySolu=Solution()
res=mySolu.generateParentheses(3)
print(res)
