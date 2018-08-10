'''
6.1 Merge Sorted Array
描述
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note: You may assume that A has enough space to hold additional elements from B. The number of
elements initialized in A and B are m and n respectively.
'''
class Solution(object):
	def merge_sorted(self,A,p,B,q):
		m=p-1
		n=q-1
		k=m+n+1
		print(m,n,k)
		while m>=0 and n>=0:
			if(A[m]>B[n]):
				B[k]=A[m]
				m,k=m-1,k-1
			elif(A[m]<B[n]):
				B[k]=B[n]
				n,k=n-1,k-1
			elif(A[m]==B[n]):
				B[k],B[k-1]=B[n],B[n]
				m,n,k=m-1,n-1,k-2
		if(m==-1 and n!=-1):
			B[0:k+1]=B[0:n+1]
		if(m!=-1 and n==-1):
			B[0:k+1]=A[0:m+1]
		return B

A=[1,2,3,5,9,11,13]
B=[2,4,6,7,8,12,0,0,0,0,0,0,0]
mySolu=Solution()
new_sorted=mySolu.merge_sorted(A,7,B,6)
print(new_sorted)

