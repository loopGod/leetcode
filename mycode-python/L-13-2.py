'''
13.2 Maximum Subarray
描述
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [−2,1,−3,4,−1,2,1,−5,4], the contiguous subarray [4,−1,2,1] has
the largest sum = 6.
'''

def Subarray(A):
	f=0
	fk=[]
	result=0
	for i in A:
		f=max(f+i,i)
		fk.append(f)
		result=max(result, f)
	return fk

def Subarray1(A):
	fk=[0 for i in range(len(A))]
	fk[0]=A[0]
	for i in range(len(A)):
		if i >0:
			fk[i]=max(fk[i-1]+A[i], A[i])
	return max(fk)

A =[-2,1,-3,4,-1,2,1,-5,4]
res=Subarray1(A)
print(res)
