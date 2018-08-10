'''
5.4.6 Populating Next Right Pointers in Each Node

Initially, all next pointers are set to NULL.
Note:
• You may only use constant extra space.
• You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent
has two children).
For example, Given the following perfect binary tree,
1
/ \
2 3
/ \ / \
4 5 6 7
After calling your function, the tree should look like:
1 -> NULL
/ \
2 -> 3 -> NULL
/ \ / \
4->5->6->7 -> NULL
'''
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.next=None
		self.val=x
		
class Solution(object):
	def __init__(self):
		self.maxRes=-10000000
	def connect(self, root):
		if root and root.left:
			root.left.next=root.right
			if root.next:
				root.right.next=root.next.left
			self.connect(root.left)
			self.connect(root.right)

tree=TreeNode(4)
tree.left=TreeNode(2)
tree.right=TreeNode(1)
tree.right.left=TreeNode(3)
tree.left.left=TreeNode(1)
tree.left.right=TreeNode(2)
mySolu=Solution()
mySolu.connect(tree)
print(tree.left.next.val)