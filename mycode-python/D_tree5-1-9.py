'''
5.1.9 Symmetric Tree
描述
是否是对称的
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

	def symTree(self,left,right):
		if left.left==None and left.right==None and right.left==None and right.right==None:
			return left.val==right.val
		if left.val!=right.val:
			return False
		else:
			return self.symTree(left.left,right.right)
   
	def isSymTree(self, root):
		if not root.left and not root.right:
			return True
		elif root.left and root.right:
			return self.symTree(root.left,root.right) and self.symTree(root.right,root.left)
		else:
			return False

#preorder=[1,2,4,8,9,5,3,6,10,11,7]
tree=TreeNode(1)
tree.left=TreeNode(2)
tree.right=TreeNode(2)
tree.left.left=TreeNode(4)
tree.left.right=TreeNode(5)
tree.right.left=TreeNode(5)
tree.right.right=TreeNode(4)

mySolu=Solution()
preorder=mySolu.isSymTree(tree)
print(preorder)