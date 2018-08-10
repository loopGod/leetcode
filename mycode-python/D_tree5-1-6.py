'''
5.1.5 Binary Tree Level Order Traversal II
描述
Given a binary tree, return the bottom-up level order traversal of its nodes’ values. (ie, from left to right,
level by level from leaf to root).
For example: Given binary tree {3,9,20,#,#,15,7},
3
/ \
9 20
/ \
15 7
return its bottom-up level order traversal as:
[
[15,7]
[9,20],
[3],
]
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
	def level_traversal_BFS(self,root):
		res = [[root.val]]
		q=[root]
		while q!=[]:
			tmp=[]
			new_q=[]
			for i in q:
				if i.left:
					new_q.append(i.left)
					tmp.append(i.left.val)
				if i.right:
					new_q.append(i.right)
					tmp.append(i.right.val)
			if tmp!=[]:
				res.append(tmp)
			q=new_q
		return res[::-1]

	def level_traversal_DFS(self,root):
		res=[]
		res=self.dfs(root, 0, res)
		return res[::-1]

	def dfs(self,root,depth,res):
		if len(res)<depth+1:
			res.append([])
		res[depth].append(root.val)
		if root.left:
			self.dfs(root.left,  depth+1, res)
		if root.right:
			self.dfs(root.right, depth+1, res)
		return res

#preorder=[1,2,4,8,9,5,3,6,10,11,7]
tree=TreeNode(1)
tree.left=TreeNode(2)
tree.right=TreeNode(3)
tree.left.left=TreeNode(4)
tree.left.right=TreeNode(5)
mySolu=Solution()
preorder=mySolu.level_traversal_DFS(tree)
print(preorder)