'''
10.1 Palindrome Partitioning
描述
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
For example, given s = ”aab”, Return
[
["aa","b"],
["a","a","b"]
]
分析
在每一步都可以判断中间结果是否为合法结果，用回溯法。
一个长度为 n 的字符串，有 n   1 个地方可以砍断，每个地方可断可不断，因此复杂度为
O(2n 1
)
'''
class Solution(object):
	"""docstring for Solution"""
	def __init__(self):
		self.res=[]

	def isPalindrome(self,S):
		for i in range(int((len(S)+0.5)/2)):
			if S[i]!=S[len(S)-1-i]:return False
		return True
	
	def DFS(self,S,valuelist):
		if len(S)<=0:
			self.res.append(valuelist)
		for i in range(len(S)):
			if self.isPalindrome(S[:i+1]):
				self.DFS(S[i+1:], valuelist+[S[:i+1]])

	def get_list(self,S):
		self.DFS(S,valuelist=[])
		return self.res

S='aaabb'
mySolu=Solution()
res=mySolu.get_list(S)
print(res)

S=[1,2,3,4]
print(S[4:])
print(S[:0])
print(type(S[3:4]))
S='aabb'
print(type(S[3:4]))