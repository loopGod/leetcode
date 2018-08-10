'''
5.4.1 Minimum Depth of Binary Tree
描述
Given a binary tree, find its minimum depth.
Theminimumdepth is the number of nodes along the shortest path fromthe root node down to the nearest
leaf node.
'''
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	def __init__(self):
		self.res0=[]
	def midDepthBT(self,tree):
		def dfs(tree,depth,res):
			if tree==None:
				return 0
			if not tree.left and not tree.right:
				res.append(depth)
			if tree.left:
				dfs(tree.left, depth+1, res)
			if tree.right:
				dfs(tree.right, depth+1, res)
			return res
		res=[]
		dfs(tree, 1, res)
		return max(res)

tree=TreeNode(4)
tree.left=TreeNode(2)
tree.right=TreeNode(6)
tree.left.left=TreeNode(1)
tree.left.right=TreeNode(1)
mySolu=Solution()
root=mySolu.midDepthBT(tree)
print(root)