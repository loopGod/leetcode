'''
5.1.11 Flatten Binary Tree to Linked List
描述
Given a binary tree, flatten it to a linked list in-place.
For example, Given
1
/ \
2 5
/ \ \
3 4 6
The flattened tree should look like:
1
\
2
\
3
\
4
\
5
\
6
'''
#平衡二叉树：高度差小于等于1，必是搜索二叉树，即左值小于中值，中值小于右值

#难度较大，递归要熟练掌握
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.preorder=[]

	def flatten(self,root):
		if root==None:
			return
		self.flatten(root.left)
		self.flatten(root.right)
		p=root
		if root.left==None:
			return
		#p=3,root=2
		while p.right:
			p=p.right
		p.right=root.right
		root.right=root.left
		root.left=None


		

#preorder=[1,2,4,8,9,5,3,6,10,11,7]
tree=TreeNode(20)
tree.left=TreeNode(10)
tree.right=TreeNode(30)
tree.left.left=TreeNode(7)
tree.left.right=TreeNode(14)
tree.right.left=TreeNode(25)
tree.right.right=TreeNode(40)

mySolu=Solution()
preorder=mySolu.flatten(tree)
print(tree.val,tree.right.val,tree.right.right.val)