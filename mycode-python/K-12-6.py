'''
12.6 Container With Most Water
描述
Given n non-negative integers a1; a2; :::; an, where each represents a point at coordinate (i; ai). n verti-
cal lines are drawn such that the two endpoints of line i is at (i; ai) and (i; 0). Find two lines, which together
with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container.
分析
每个容器的面积，取决于最短的木板。
'''
def Container(A):
	left=0
	right=len(A)-1
	area=0
	while left<right:
		area=max(area, (right-left)*min(A[right], A[left]))
		if A[left]==A[right]:
			area=max(area, (right-left)*A[right])
		if A[left]<A[right]:
			left=left+1
		elif A[left]>=A[right]:
			right=right-1
	return area

A =[2,3,1,1,4]
res=Container(A)
print(res)