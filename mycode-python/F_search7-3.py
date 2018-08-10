'''
7.3 Search a 2D Matrix
描述
Write an efficient algorithm that searches for a value in an mn matrix. This matrix has the following
properties:
• Integers in each row are sorted from left to right.
• The first integer of each row is greater than the last integer of the previous row.
For example, Consider the following matrix:
[
[1, 3, 5, 7],
[10, 11, 16, 20],
[23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution(object):
	def Search2Dmatrix(self,mat,num):
		if mat==[]:
			return False
		m=len(mat)
		n=len(mat[0])
		start=0
		end=m*n
		while end>start:
			mid=int((start+end)/2)
			val=mat[int(mid/n)][mid%n]
			if val==num:
				return True
			elif val<num:
				start=mid+1
			else:
				end=mid-1
		return False

s=[[1, 3, 5, 7 ],
   [10,11,16,20],
   [23,30,34,50]]
mySolu=Solution()
i=mySolu.Search2Dmatrix(s,2)
print(i)

