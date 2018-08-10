'''
5.1.8 Same Tree
描述
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.preorder=[]
	# @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
	def isSameTree(self, root1,root2):
		if root1.val!=root2.val:
			return False
		if (root1.left and not root2.left) or (not root1.left and root2.left):
			return False
		if (root1.left and not root2.left) or (not root1.left and root2.left):
			return False
		if (root1.right and not root2.right) or (not root1.right and root2.right):
			return False
		if (root1.right and not root2.right) or (not root1.right and root2.right):
			return False
		if root1.left and root2.left:
			return self.isSameTree(root1.left, root2.left)
		if root1.right and root2.right:
			return self.isSameTree(root1.right, root2.right)
		return True

#preorder=[1,2,4,8,9,5,3,6,10,11,7]
tree=TreeNode(1)
tree.left=TreeNode(2)
tree.right=TreeNode(3)
tree.left.left=TreeNode(4)
tree.left.right=TreeNode(5)

tree2=TreeNode(1)
tree2.left=TreeNode(2)
tree2.right=TreeNode(3)
tree2.left.left=TreeNode(4)
tree2.left.right=TreeNode(5)
mySolu=Solution()
preorder=mySolu.isSameTree(tree,tree2)
print(preorder)