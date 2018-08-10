'''
5.4.4 Path Sum II
描述
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.
For example: Given the below binary tree and sum = 22,
5
/ \
4 8
/ / \
11 13 4
/ \ / \
7 2 5 1
return
[
[5,4,11,2],
[5,8,4,5]
]
'''
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	def __init__(self):
		self.res0=[]
	def pathSum2(self,tree,sum0):
		def dfs(tree,depth,sub,res,sum0):
			if tree==None:
				return False
			if not tree.left and not tree.right:
				if sum(sub)==sum0:
					res.append(sub)
				else:
					return
			if tree.left:
				dfs(tree.left, depth+1, sub+[tree.left.val],res,sum0)
			if tree.right:
				dfs(tree.right, depth+1, sub+[tree.right.val],res,sum0)
			return res
		
		return dfs(tree, 1, [tree.val],[],sum0)
		

tree=TreeNode(4)
tree.left=TreeNode(2)
tree.right=TreeNode(1)
tree.right.left=TreeNode(3)
tree.left.left=TreeNode(1)
tree.left.right=TreeNode(2)
mySolu=Solution()
root=mySolu.pathSum2(tree,8)
print(root)