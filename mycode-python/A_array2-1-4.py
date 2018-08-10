#LeetCode, Remove Duplicates from Sorted Array
#时间复杂度O(logn)，空间复杂度O(1)
#旋转数组二分查找目标值（元素可重复）

def solution(A, n,target):
	first=0
	last=n
	while(first!=last):
		mid=int((first+last)/2)
		if(A[mid]==target):
			#主要的区别在下面，需要追溯到重复元素的首元素#
			i_last=mid
			if(i_last==0): return i_last
			while (A[i_last]==A[i_last-1]):
			 	i_last=i_last-1 
			 	if(i_last==0): return i_last
			return i_last
			##############################################
		if(A[mid]>=A[first]):
			if(target>=A[first] and target<A[mid]):
				last=mid
			else:first=mid+1
		elif(A[mid]<A[first]):
			if(target>A[mid] and target<=A[last-1]):
				first=mid+1
			else: last=mid
	return -1
	
A=[5,6,1,1,1,1]
print(solution(A,6,6))
A=[5,6,6,6,1,1]
print(solution(A,6,6))
A=[5,6,8,8,8,8]
print(solution(A,6,8))
A=[8,8,8,8,8,8]
print(solution(A,6,8))

