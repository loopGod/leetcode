'''
5.2.1 Construct Binary Tree from Preorder and Inorder Traversal
描述
Given preorder and inorder traversal of a tree, construct the binary tree.
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
	def buildTree(self,preorder,inorder):
		if len(inorder) == 0:
			return None
		if len(inorder)==1:
			return TreeNode(inorder[0])
		root=TreeNode(preorder[0])
		index=inorder.index(preorder[0])
		root.left=self.buildTree(preorder[1:index+1], inorder[0:index])
		root.right=self.buildTree(preorder[index+1:len(preorder)], inorder[index+1:len(inorder)])
		return root

preorder=[1,2,4,8,9,5,3,6,10,11,7]
inorder =[8,4,9,2,5,1,10,6,11,3,7]
mySolu=Solution()
root=mySolu.buildTree(preorder,inorder)
print(root.val)