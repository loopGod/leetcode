#subsets
'''
8.1 Subsets
描述
Given a set of distinct integers, S, return all possible subsets.
Note:
• Elements in a subset must be in non-descending order.
• The solution set must not contain duplicate subsets.
For example, If S = [1,2,3], a solution is:
[
[3],
[1],
[2],
[1,2,3],
[1,3],
[2,3],
[1,2],
[]
]
'''

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def __init__(self):
    	self.res=[]

    def dfs(self,depth, start, valuelist,S):
            self.res.append(valuelist)
            if depth == len(S): return
            for i in range(start, len(S)):
                self.dfs(depth+1, i+1, valuelist+[S[i]],S)

    def subsets(self, S):
        S.sort()
        self.dfs(0, 0, [], S)
        return self.res

S=[1,2,3,4]
mySolu=Solution()
res=mySolu.subsets(S)
print(res)

'''
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def __init__(self):
    	self.res=[]

    def dfs(self,depth, i,S):
    	if depth == len(S): return S
    	self.res.append(S[i])
    	self.dfs(depth+1, i+1, S)
    	self.res.pop()
    	self.dfs(depth+1, i+1, S)

S=[1,2,3,4]
mySolu=Solution()
res=mySolu.dfs(0,0,S)
print(res)
'''
