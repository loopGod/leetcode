
'''
13.1 Triangle
描述
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent
numbers on the row below.
For example, given the following triangle
[
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note: Bonus point if you are able to do this using only O(n) extra space, where n is the total number of
rows in the triangle.
分析
设状态为 f(i; j)，表示从从位置 (i; j) 出发，路径的最小和，则状态转移方程为
f(i; j) = min ff(i; j + 1); f(i + 1; j + 1)g + (i; j)
'''

def Triangle(A):
	MAXvalue=0
	for i in range(len(A)-2,-1,-1):
		for j in range(i+1):
			A[i][j]=A[i][j]+min(A[i+1][j],A[i+1][j+1])
	return A[0][0]

A =[
    [2],
   [3,4],
  [6,5,7],
 [4,1,8,3],
[1,2,3,4,5]
]
res=Triangle(A)
print(res)
