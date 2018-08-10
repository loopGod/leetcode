'''
4.1.2 Longest Valid Parentheses
描述
Given a string containing just the characters ’(’ and ’)’, find the length of the longest valid (wellformed)
parentheses substring.
For ”(()”, the longest valid parentheses substring is ”()”, which has length = 2.
Another example is ”)()())”, where the longest valid parentheses substring is ”()()”, which has
length = 4.
'''
#主要记住有效段前一个的索引
class Solution(object):
	"""docstring for Solution"""
	def stack_longest_validS(self, s):
		if(len(s)<=1):
			return 0
		stack=[]
		maxlen=0
		last=0
		for i in range(len(s)):
			if(s[i]=='('):
				stack.append(i)
			else:
				if(stack==[]):
					last=i
				else:
					print(stack)
					stack.pop()
					if(stack==[]):
						maxlen=max(maxlen,i-last)
					else:
						maxlen=max(maxlen,i-stack[-1])
		return maxlen

s='))()())('
s2='((()())('
mySolu=Solution()
maxlen=mySolu.stack_longest_validS(s2)
print(maxlen)



