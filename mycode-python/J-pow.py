class Solution(object):
	def __init__(self):
		self.res=0

	def pow(self,x,n):
		if n == 0:
			return 1
		if n<0:
			return 1.0/self.pow(x,-n)
		if n%2==1:
			return x*self.pow(x*x, int(n/2))
		else:
			return self.pow(x*x, int(n/2))

mySolu=Solution()
res=mySolu.pow(2,4)
print(res)