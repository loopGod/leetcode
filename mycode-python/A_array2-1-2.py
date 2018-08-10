#LeetCode, Remove Duplicates from Sorted Array
#时间复杂度O(n)，空间复杂度O(1)
#最多重复2次

def removeDuplicates(A, n):
	if n==0:
		return 0
	B=[0]
	B[0]=A[0]
	if n<=2:
		return 1
	A.append(A[n-1]+1)
	print(A)
	for i in range(n-1):
		if A[i]!=A[i+1] :
			B.append(A[i+1])
		elif A[i]==A[i+1] and A[i]!=A[i+2] :
			B.append(A[i+1])
	return len(B),B
A=[1,2,2,3,3,3]
print(removeDuplicates(A, 6))
