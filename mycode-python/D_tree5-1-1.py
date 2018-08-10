'''
5.1.1 Binary Tree Preorder Traversal
描述
Given a binary tree, return the preorder traversal of its nodes’ values.
For example: Given binary tree {1,#,2,3},
1
 \
  2
 /
3
return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively?
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
	def preorder_traversal(self,tree):
		if tree == None:
			return None
		self.preorder.append(tree.val)
		if(tree.left):
			self.preorder_traversal(tree.left)
		if(tree.right):
			self.preorder_traversal(tree.right)

		return self.preorder

#preorder=[1,2,4,8,9,5,3,6,10,11,7]
tree=TreeNode(1)
tree.left=TreeNode(2)
tree.right=TreeNode(3)
tree.left.left=TreeNode(4)
tree.left.right=TreeNode(5)
mySolu=Solution()
preorder=mySolu.preorder_traversal(tree)
print(preorder)