'''
5.1.7 Recover Binary Search Tree
描述
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.
Note: Asolution usingO(n) space is pretty straight forward. Could you devise a constant space solution?
分析
O(n)空间的解法是，开一个指针数组，中序遍历，将节点指针依次存放到数组里，然后寻找两
处逆向的位置，先从前往后找第一个逆序的位置，然后从后往前找第二个逆序的位置，交换这两个
指针的值。
中序遍历一般需要用到栈，空间也是 O(n) 的，如何才能不使用栈？Morris 中序遍历。
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
	def inorder(self, root, list, listp):
        if root:
            self.inorder(root.left, list, listp)
            list.append(root.val); listp.append(root)
            self.inorder(root.right, list, listp)
    def recoverTree(self, root):
        list = []; listp = []
        self.inorder(root, list, listp)
        list.sort()
        for i in range(len(list)):
            listp[i].val = list[i]
        return root

#preorder=[1,2,4,8,9,5,3,6,10,11,7]
tree=TreeNode(1)
tree.left=TreeNode(2)
tree.right=TreeNode(3)
tree.left.left=TreeNode(4)
tree.left.right=TreeNode(5)
mySolu=Solution()
preorder=mySolu.recoverTree(tree)
print(preorder)