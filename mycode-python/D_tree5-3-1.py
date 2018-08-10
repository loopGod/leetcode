'''
5.3.1 Unique Binary Search Trees
描述
Given n, how many structurally unique BST’s (binary search trees) that store values 1:::n?
For example, Given n = 3, there are a total of 5 unique BST’s.
1 3 3 2 1
\ / / / \ \
3 2 1 1 3 2
/ / \ \
2 1 2 3
分析
如果把上例的顺序改一下，就可以看出规律了。
1 1 2 3 3
\ \ / \ / /
3 2 1 3 2 1
/ \ / \
2 3 1 2
比如，以 1 为根的树的个数，等于左子树的个数乘以右子树的个数，左子树是 0 个元素的树，
右子树是 2 个元素的树。以 2 为根的树的个数，等于左子树的个数乘以右子树的个数，左子树是 1
个元素的树，右子树也是 1个元素的树。依此类推。
当数组为1; 2; 3; :::; n时，基于以下原则的构建的BST树具有唯一性：以i为根节点的树，其左
子树由 [1, i-1] 构成，其右子树由 [i+1, n] 构成。
定义f(i) 为以 [1; i] 能产生的Unique Binary Search Tree的数目，则
如果数组为空，毫无疑问，只有一种 BST，即空树，f(0) = 1。
如果数组仅有一个元素1，只有一种BST，单个节点，f(1) = 1。
如果数组有两个元素 1,2，那么有如下两种可能

f(3) = f(0)  f(2) ，1为根的情况
+ f(1)  f(1) ，2为根的情况
+ f(2)  f(0) ，3为根的情况
'''
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	def searchTree(self,n):
		f=[1 for i in range(n+1)]
		for i in range(2,n+1):
			sum0=0
			for j in range(0,i):
				sum0+=f[j]*f[i-1-j]
			f[i]=sum0
		return f[n]

mySolu=Solution()
root=mySolu.searchTree(4)
print(root)