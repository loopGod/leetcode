'''
13.13 Word Break II
描述
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word
is a valid dictionary word.
Return all such possible sentences.
For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].
A solution is ["cats and dog", "cat sand dog"].
'''
#DP
class Solution():
    
    def check(self, s, dict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(0, i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]
        
    def dfs(self, s, dict, stringlist):
        if self.check(s, dict):
            if len(s) == 0: Solution.res.append(stringlist[1:].strip())
            for i in range(1, len(s)+1):
                if s[:i] in dict:
                	print(stringlist+' '+s[:i])
                	self.dfs(s[i:], dict, stringlist+' '+s[:i])
    
    def wordBreak2(self, s, dict):
        Solution.res = []
        self.dfs(s, dict, '')
        return Solution.res


s = "catsanddog"
dict0 = ["cat", "cats", "and", "sand", "dog"]
mySolu=Solution()
maxV=mySolu.wordBreak2(s,dict0)
print(maxV)



