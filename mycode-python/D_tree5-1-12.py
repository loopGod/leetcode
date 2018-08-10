'''
5.1.11 Populating Next Right Pointers in Each Node
描述
下面是II的题目：解法是I->满二叉树
Follow up for problem ”Populating Next Right Pointers in Each Node”.
What if the given tree could be any binary tree? Would your previous solution still work?
Note: You may only use constant extra space.
For example, Given the following binary tree,
1
/ \
2 3
/ \ \
4 5 7
After calling your function, the tree should look like:
1 -> NULL
/ \
2 -> 3 -> NULL
/ \ \
4-> 5 -> 7 -> NULL
'''
#平衡二叉树：高度差小于等于1，必是搜索二叉树，即左值小于中值，中值小于右值

#难度较大，递归要熟练掌握
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		self.next=None
		
class Solution(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.preorder=[]

	def populating(self,root):
		if root==None:
			return
		if root and root.left:
			root.left.next=root.right
			if root.next:
				root.right.next=root.next.left
			else:
				root.right.next=None
		self.populating(root.left)
		self.populating(root.right)



		

#preorder=[1,2,4,8,9,5,3,6,10,11,7]
tree=TreeNode(20)
tree.left=TreeNode(10)
tree.right=TreeNode(30)
tree.left.left=TreeNode(7)
tree.left.right=TreeNode(14)
tree.right.left=TreeNode(25)
tree.right.right=TreeNode(40)

mySolu=Solution()
preorder=mySolu.populating(tree)
print(tree.left.next.val)