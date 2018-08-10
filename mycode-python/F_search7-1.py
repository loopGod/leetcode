'''
7.1 Search for a Range
描述
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example, Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].
'''

class Solution(object):
	def searchForRange(self,s,num):
		#start1=int((len(s))/2+0.5)
		if s[-1]<num:
			return -1
		start=0
		end=len(s)-1
		start2=0
		end2=len(s)-1

		while start!=end-1:
				mid=int((start+end)/2+0.5)
				if s[mid]<num:
					start=mid
				if s[mid]>=num:
					end=mid
		
		while start2!=end2-1:
				mid2=int((start2+end2)/2+0.5)
				if s[mid2]<=num:
					start2=mid2
				if s[mid2]>num:
					end2=mid2
		
		return [end,start2]

s=[5,7,7,8,8,10]
mySolu=Solution()
i=mySolu.searchForRange(s,8)
print(i)

