'''
5.4.7 Sum Root to Leaf Numbers
描述
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
For example,
1
/ \
2 3
The root-to-leaf path 1->2 represents the number 12. The root-to-leaf path 1->3 represents the number
13.
Return the sum = 12 + 13 = 25.
'''
class TreeNode(object):
	def __init__(self,x):
		self.left=None
		self.right=None
		self.val=x
		
class Solution(object):
	def __init__(self):
		self.maxRes=0
	def sumRoottoLeaf(self,tree):
		#sub=str(tree.val)
		def dfs(tree,sub,res):
			if not tree:
				return 0
			if not tree.left and not tree.right:
				self.maxRes=str(int(self.maxRes)+int(sub))
				#底部的里面的res改变，上层的res并不变，依旧是0，因此用全局变量记录
			if tree.left:
				dfs(tree.left, sub+str(tree.left.val), res)
			if tree.right:
				dfs(tree.right, sub+str(tree.right.val), res)
			return
		res='0'
		dfs(tree, str(tree.val),res)
		return self.maxRes
tree=TreeNode(4)
tree.left=TreeNode(2)
tree.right=TreeNode(1)
tree.right.left=TreeNode(3)
tree.left.left=TreeNode(1)
tree.left.right=TreeNode(2)
mySolu=Solution()
root=mySolu.sumRoottoLeaf(tree)
print(root)