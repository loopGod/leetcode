'''
3.14 Simplify Path
描述
Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Corner Cases:
• Did you consider the case where path = "/../"? In this case, you should return "/".
• Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''
#48,65,97
class Solution:
    def SimplifyPath(self,s):
        sList=s.split('/')
        stack=[]
        for i in range(len(sList)):
        	if len(sList[i]) and sList[i]!='.':
        		if sList[i]=='..' and stack!=[]:
        			stack.pop()
        		elif sList[i]!='..':
        			stack.append('/'+sList[i])
        return ''.join(stack)
        
#字符串是不可变，和元祖一样
s='/a/./b/..//../../c/'
muSolu=Solution()
new_node=muSolu.SimplifyPath(s)
print(new_node)

'''
word='a1bc'
print(sorted(word))
'''


