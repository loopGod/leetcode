'''
10.7 Combination Sum
描述
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
• All numbers (including target) will be positive integers.
• Elements in a combination (a1; a2; :::; ak) must be in non-descending order. (ie, a1  a2  :::  ak).
• The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, A solution set is:
[7]
[2, 2, 3]
'''
class Solution:
    def __init__(self):
        self.res0=[]
    # @return a list of lists of string
    def combinationSum(self, C, T):
        def dfs(C,T,sub,res):
            if T==0:
                sub.sort()
                res.add(tuple(sub))
                return
            if T<0:
                return
            for i in range(len(C)):
                dfs(C, T-C[i], sub+[C[i]],res)
        res=set()
        dfs(C, T, [],res)
        return res
C=[1,2,3,7,6]
mySolu=Solution()
res=mySolu.combinationSum(C,7)
print(res)


#用set()去重。里面可以放元组不能放列表