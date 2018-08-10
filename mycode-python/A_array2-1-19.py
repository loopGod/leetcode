'''
2.1.19 Gray Code
描述
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of
gray code. A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2
Note:
• For a given n, a gray code sequence is not uniquely defined.
• For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
• For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
'''
class Solution:
    def GrayCode(self, n):
    	GC=[]
    	for i in range(2**n):
    		GC.append((i>>1)^i)
    	return GC

mySolu=Solution()
result=mySolu.GrayCode(3)
print(result)

print(int('11', 2))
#进制转换
'''
print(bin(int('15', 10)))
for i in bin(int('15', 10)):
	print(i)
'''


