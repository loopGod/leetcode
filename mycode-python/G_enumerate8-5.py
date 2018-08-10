#subsets
'''
8.5 Combinations
描述
Given two integers n and k, return all possible combinations of k numbers out of 1:::n.
For example, If n = 4 and k = 2, a solution is:
[
[2,4],
[3,4],
[2,3],
[1,2],
[1,3],
[1,4],
]
'''
'''
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        def dfs(start, valuelist):
            if self.count == k: ret.append(valuelist); return
            for i in range(start, n + 1):
                self.count += 1
                dfs(i + 1, valuelist + [i])
                self.count -= 1
        ret = []; self.count = 0
        dfs(1, [])
        return ret
'''
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def __init__(self):
        self.res=[]
        self.last_sub=-1
        self.count=0

    def dfs(self,depth, start, valuelist,S,k):
        
        if self.count == k: 
            self.res.append(valuelist)
            return
        for i in range(start, len(S)):
            if(self.last_sub!=S[i]):
                self.count+=1
                self.dfs(depth+1, i+1, valuelist+[S[i]],S,k)
                self.count-=1
            self.last_sub=S[i]

    def subsets(self, S,k):
        S.sort()
        self.dfs(0, 0, [], S,k)
        return self.res

S=[1,2,2,3,4]
mySolu=Solution()
res=mySolu.subsets(S,2)
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
