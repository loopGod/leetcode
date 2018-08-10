'''
2.1.20 Set Matrix Zeroes
描述
Given a m  n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
Follow up: Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
分析
O(m + n) 空间的方法很简单，设置两个 bool数组，记录每行和每列是否存在 0。
想要常数空间，可以复用第一行和第一列。
'''
class Solution:
    def setMatrixZeroes(self, matrix):
    	savei={}
    	savej={}
    	m=len(matrix)
    	n=len(matrix[0])
    	for i in range(m):
    		for j in range(n):
    			if matrix[i][j]==0:
    				savei[i]=j
    				savej[j]=i
    	for i in range(m):
    		for j in range(n):
    			if i in savei:
    				matrix[i][j]=0
    			if j in savej:
    				matrix[i][j]=0
    	return matrix
matrix=[[1,2,3,4],
		[5,6,0,8],
		[9,10,11,12]]
mySolu=Solution()
result=mySolu.setMatrixZeroes(matrix)
print(result)


#进制转换
'''
print(int('11', 2))
print(bin(int('15', 10)))
for i in bin(int('15', 10)):
	print(i)
'''


