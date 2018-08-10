'''
7.2 Search Insert Position
描述
Given a sorted array and a target value, return the index if the target is found. If not, return the index
where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

class Solution(object):
	def SearchInsert(self,s,num):
		if s==[]:
			return 0
		if num<=s[0]:
			return 0
		if num >s[-1]:
			return len(s)
		start=0
		end=len(s)-1
		while start!=end-1:
			mid=int((start+end)/2+0.5)
			if s[mid]<num:
				start=mid
			else:
				end=mid
		return end

s=[5,7,7,8,9,10]
mySolu=Solution()
i=mySolu.SearchInsert(s,9)
print(i)

