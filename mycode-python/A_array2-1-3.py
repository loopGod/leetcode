#LeetCode, Remove Duplicates from Sorted Array
#时间复杂度O(logn)，空间复杂度O(1)
#旋转数组二分查找目标值

def solution(A, n,target):
	first=0
	last=n
	while(first!=last):
		mid=int((first+last)/2)
		if(A[mid]==target):
			return mid
		if(A[mid]>=A[first]):
			if(target>=A[first] and target<A[mid]):
				last=mid
			else:first=mid+1
		elif(A[mid]<A[first]):
			if(target>A[mid] and target<=A[last-1]):
				first=mid+1
			else: last=mid
	return -1
	
A=[5,6,1,2,3,4]
print(solution(A,6,6))
A=[5,6,7,8,3,4]
print(solution(A,6,6))
A=[5,6,7,8,3,4]
print(solution(A,6,8))

