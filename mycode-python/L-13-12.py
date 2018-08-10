'''
13.12 Word Break
描述
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.
For example, given
s = "leetcode",
dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".

分析
设状态为 f(i)，表示 s[0,i] 是否可以分词，则状态转移方程为
f(i) = any_of(f(j)&&s[j + 1; i] 2 dict); 0  j < i
'''
#DP
class Solution():
    def wordBreak(self, s, dict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]


s = "leetcode"
dict0 = ["leet", "code", 'cool']
mySolu=Solution()
maxV=mySolu.wordBreak(s,dict0)
print(maxV)




