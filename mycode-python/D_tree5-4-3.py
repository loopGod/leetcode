'''
5.4.3 Path Sum
描述
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the
values along the path equals the given sum.
For example: Given the below binary tree and sum = 22,
5
/ \
4 8
/ / \
11 13 4
/ \ \
7 2 1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	def __init__(self):
		self.res0=[]
	def pathSum(self,tree,sum0):
		def dfs(tree,depth,res,sum0):
			if tree==None:
				return False
			if not tree.left and not tree.right:
				if res==sum0:
					return True
				else:
					return
			if tree.left:
				if dfs(tree.left, depth+1, res+tree.left.val,sum0):
					return True
			if tree.right:
				if dfs(tree.right, depth+1, res+tree.right.val,sum0):
					return True
			return False
		
		return dfs(tree, 1, tree.val,sum0)
		

tree=TreeNode(4)
tree.left=TreeNode(2)
tree.right=TreeNode(6)
tree.right.left=TreeNode(3)
tree.left.left=TreeNode(1)
tree.left.right=TreeNode(2)
mySolu=Solution()
root=mySolu.pathSum(tree,13)
print(root)