'''
5.1.10 Balanced Binary Tree
描述
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two
subtrees of every node never differ by more than 1.
'''
#平衡二叉树：高度差小于等于1，必是搜索二叉树，即左值小于中值，中值小于右值
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.preorder=[]

	def searchTree(self,root):
		if root.left:
			if root.val>root.left.val:
				return self.searchTree(root.left)
			else:
				return False
		if root.right:
			if root.val<root.right.val:
				return self.searchTree(root.right)
			else:
				return False
		return True

	def branchTree(self,root):
		if root==None:
			return 0
		q=[root]
		count=0
		while q!=[]:
			count+=1
			new_q=[]
			for i in q:
				if i.left:
					new_q.append(i.left)
				if i.right:
					new_q.append(i.right)
				q=new_q
		return count

	def balanceTree(self,root):
		if self.searchTree(root) and abs(self.branchTree(root.left)-self.branchTree(root.right))<=1:
			return True
		else:
			return False

#preorder=[1,2,4,8,9,5,3,6,10,11,7]
tree=TreeNode(20)
tree.left=TreeNode(10)
tree.right=TreeNode(30)
tree.left.left=TreeNode(7)
tree.left.right=TreeNode(14)
tree.right.left=TreeNode(25)
tree.right.right=TreeNode(40)

mySolu=Solution()
preorder=mySolu.balanceTree(tree)
print(preorder)