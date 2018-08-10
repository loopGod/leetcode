class Solution(object):
	def __init__(self):
		self.res=0

	def sqrt(self,first,x,last,s):
		if   abs(((first+last)/2)**2-x) < s:
			self.res=(first+last)/2
			return
		elif ((first+last)/2)**2 < x:
			first=(first+last)/2
		elif ((first+last)/2)**2 > x:
			last=(first+last)/2
		self.sqrt(first, x, last,s)
		return self.res

	def mySolve(self,x,s):
		return self.sqrt(0,x,x,s)

mySolu=Solution()
res=mySolu.mySolve(9,0.01)
print(res)