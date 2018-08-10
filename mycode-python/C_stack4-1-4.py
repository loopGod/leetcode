'''
4.1.4 Evaluate Reverse Polish Notation
描述
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Some examples:
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
#显然用栈

class Solution(object):
	"""docstring for Solution"""
	def polish_Notation(self, polish):
		stack=[]
		for i in polish:
			if(i!='+' and i!='-' and i!='*' and i!='/'):
				stack.append(i)
			elif(i=='+'):
				a=int(stack.pop())
				b=int(stack.pop())
				stack.append(str(a+b))
			elif(i=='-'):
				a=int(stack.pop())
				b=int(stack.pop())
				stack.append(str(a-b))
			elif(i=='*'):
				a=int(stack.pop())
				b=int(stack.pop())
				stack.append(str(a*b))
			elif(i=='/'):
				a=int(stack.pop())
				b=int(stack.pop())
				stack.append(str(int(a/b)))
			answer=stack[0]
		return answer

polish=["2", "1", "+", "3", "*"]
mySolu=Solution()
answer=mySolu.polish_Notation(polish)
print(answer)

#print(ord('+'))
#print(chr( 43))
