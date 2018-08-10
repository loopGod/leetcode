'''
5.2.2 Construct Binary Tree from Inorder and Postorder Traversal
描述
Given inorder and postorder traversal of a tree, construct the binary tree.
Note: You may assume that duplicates do not exist in the tree.
'''
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	"""docstring for ClassName"""
	
	# @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
	def buildTree(self,inorder,postorder):
		if len(inorder) == 0:
			return None
		if len(inorder)==1:
			return TreeNode(inorder[0])
		root=TreeNode(postorder[len(postorder)-1])
		index=inorder.index(postorder[len(postorder)-1])
		root.left=self.buildTree(inorder[0:index], postorder[0:index])
		root.right=self.buildTree(inorder[index+1:len(inorder)], postorder[index:len(postorder)-1])
		return root

inorder=[4,2,5,1,6,3,7]
postorder=[4,5,2,6,7,3,1]
mySolu=Solution()
root=mySolu.buildTree(inorder,postorder)
print(root.val)