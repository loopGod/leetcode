'''
4.1.1 Valid Parentheses
描述
Given a string containing just the characters ’(’, ’)’, ’{’, ’}’, ’[’ and ’]’, determine if the
input string is valid.
The brackets must close in the correct order, ”()” and ”()[]” are all valid but ”(]” and ”([)]” are
not.
'''
class Solution(object):
	
	def stack_Parentheses(self,str):
		parmap={']':'[','}':'{',')':'('}
		par=[]
		for i in str:
			if(i in parmap):
				if(parmap[i]!=par.pop()):
					return 'false'
			else:
				par.append(i)
		return 'true'

str='[]{}()(])'
mySolu=Solution()
res=mySolu.stack_Parentheses(str)
print(res)