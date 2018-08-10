'''
6.4 Insertion Sort List
描述
Sort a linked list using insertion sort.
'''
class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val=x
		self.next=None

class Solution(object):
	
	def sort_list(self,l1):
		new_l=ListNode(-1)
		root=new_l
		m=1
		while l1:
			m=1
			new_l=root
			while m==1:
				if(new_l.val==-1 and new_l.next==None):
					new_l.next=ListNode(l1.val)
					print('once')
					m=2
				elif(l1.val<=new_l.val and last_val==-1):
					last_node.next=ListNode(l1.val)
					last_node.next.next=new_l
					print('twice')
					print(root.val,root.next.val,root.next.next.val)
					m=2
				elif(l1.val>last_node.val and l1.val<=new_l.val):
					last_node.next=ListNode(l1.val)
					last_node.next.next=new_l
					print('third')
					m=2
				elif(l1.val>last_node.val and new_l==None):
					last_node.next=ListNode(l1.val)
					last_node.next.next=new_l
					print('forth')
					m=2
				last_val=new_l.val
				last_node=new_l
				new_l=new_l.next
		
			l1=l1.next
		return root


l1=ListNode(6)
l1_2=ListNode(1)
l1_3=ListNode(3)
l1_2.next=l1_3
l1.next=l1_2

mySolu=Solution()
new_sorted=mySolu.sort_list(l1)
print(new_sorted.val,new_sorted.next.val,new_sorted.next.next.val)

