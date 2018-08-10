'''
5.3.3 Validate Binary Search Tree
描述
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
• The left subtree of a node contains only nodes with keys less than the node’s key.
• The right subtree of a node contains only nodes with keys greater than the node’s key.
• Both the left and right subtrees must also be binary search trees.
'''
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	def __init__(self):
		self.res=[]
	def deterSearchTree(self,tree):
		if tree.left:
			self.deterSearchTree(tree.left)
		self.res.append(tree.val)
		if tree.right:
			self.deterSearchTree(tree.right)
		
	def findSearchTree(self,tree):
		self.deterSearchTree(tree)
		for i in range(1,len(self.res)):
			if self.res[i]<=self.res[i-1]:
				return False
		return True

#下面这个方法很好
	 def validBST(self, root, min, max):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.validBST(root.left, min, root.val) and self.validBST(root.right, root.val, max)
    def isValidBST(self, root):
        return self.validBST(root, -21474836480, 21474836470)
tree=TreeNode(4)
tree.left=TreeNode(2)
tree.right=TreeNode(6)
tree.left.left=TreeNode(1)
tree.left.right=TreeNode(1)
mySolu=Solution()
root=mySolu.findSearchTree(tree)
print(root)