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
    def combinationSum2(self, C, T):
        def dfs(C,T,sub,res):
            if T==0:
                res.append(sub)
                return
            if T<0:
                return
            for i in range(len(C)):
                dfs(C[i+1:], T-C[i], sub+[C[i]],res)
        res=[]
        dfs(C, T, [],res)
        res2=[]
        res3=[]
        for i in res:
            i=sorted(i)
            res2.append(i)
        for j in range(len(res2)):
            if res2[j] not in res2[j+1:]:
                res3.append(res2[j])
        return res
C=[10,1,2,7,6,1,5]
mySolu=Solution()
res=mySolu.combinationSum2(C,8)
print(res)
