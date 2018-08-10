#LeetCode, Remove Duplicates from Sorted Array
#时间复杂度O(n)，空间复杂度O(1)
#不重复
def removeDuplicates(A, n):
	if n==0:
		return 0
	B=[0]
	B[0]=A[0]
	if n==1:
		return 1
	for i in range(n-1):
		if A[i+1]!=A[i] :
			B.append(A[i+1])
	return len(B),B
A=[1,2,2,3,3,4]
print(removeDuplicates(A, 6))
