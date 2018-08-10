#LeetCode, Remove Duplicates from Sorted Array
#时间复杂度O(log(m+n))，空间复杂度O(log(m+n))
#两排序数组所有元素的k位数

def solution(A, m, B, n):
	mid=int((m+n)/2+0.5)

def delete0(A,ai):
	del(A[0:ai])
	

def find_kth(A,m,B,n,k):
	if(k == 1): 
		print(min(A[0], B[0]))
		return min(A[0], B[0])
	if(A[int(k/2-1)]<B[int(k/2-1)]):
		if(k/2>(k/2)):ai=int(k/2)
		else:ai=int(k/2)
		print(ai)
		delete0(A,ai)
		print(A)
		find_kth(A, m-ai, B, n, k-ai)
	elif(A[int(k/2-1)]>B[int(k/2-1)]):
		if(k/2>(k/2)):ai=int(k/2)
		else:ai=int(k/2)
		print(ai)
		delete0(B,ai)
		print(B)
		find_kth(A, m, B, n-ai, k-ai)
	elif(A[int(k/2-1)]==B[int(k/2-1)]):
		print(A[int(k/2-1)])
		return A[int(k/2-1)]

A=[1,2,3,4,5,6,7]
B=[2,3,4,5,7,8,9]
find_kth(A,7,B,7,10)

