'''
5.4.5 Binary Tree Maximum Path Sum
描述
Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree. For example: Given the below binary tree,
1
/ \
2 3
Return 6.
'''
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	def __init__(self):
		self.maxRes=-10000000
	def maxPathSum(self,tree):
		def maxsum(tree):
			lmax=0
			rmax=0
			if not tree:
				return 0
			if tree.left:
				lmax=maxsum(tree.left)
			if tree.right:
				rmax=maxsum(tree.right)
			self.maxRes=max(self.maxRes,tree.val+lmax+rmax)
			return max(tree.val, max(tree.val+lmax,tree.val+rmax))
		maxsum(tree)
		return self.maxRes

tree=TreeNode(4)
tree.left=TreeNode(2)
tree.right=TreeNode(1)
tree.right.left=TreeNode(3)
tree.left.left=TreeNode(1)
tree.left.right=TreeNode(2)
mySolu=Solution()
root=mySolu.maxPathSum(tree)
print(root)