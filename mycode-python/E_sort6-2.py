'''
6.2 Merge Two Sorted Lists
描述
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
the nodes of the first two lists.
'''
class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val=x
		self.next=None

class Solution(object):
	def merge_sorted_list(self,l1,l2):
		new_l=ListNode(0)
		root=new_l
		while l1 and l2:
			if(l1.val<l2.val):
				root.val=l1.val
				l1=l1.next
				if(l1==None and l2 != None):
					root.next=l2
				else:
					root.next=ListNode(1)
					root=root.next
			elif(l1.val>l2.val):
				root.val=l2.val
				l2=l2.next
				if(l1!=None and l2 == None):
					root.next=l1
				else:
					root.next=ListNode(1)
					root=root.next
			elif(l1.val==l2.val):
				root.val=l1.val
				l1=l1.next
				root.next=ListNode(1)
				root=root.next
				root.val=l2.val
				l2=l2.next
				if(l1==None and l2 == None):
					root.next=None
				else:
					root.next=ListNode(1)
					root=root.next
		return new_l
'''
#放外面判断不行，因为上面root指向了链表的最后一个地址，
#后面root=l2、root=l1只是让root指向了l2新地址，并没有改变原链表后面的元素
		if(l1==None and l2 != None):
			root=l2
			print(root.val)
		elif(l2==None and l1 != None):
			root=l1
			print(root.val)
		else:root=None
return new_l
'''

l1=ListNode(1)
l1_2=ListNode(3)
l1_3=ListNode(6)
l1_2.next=l1_3
l1.next=l1_2

l2=ListNode(2)
l2_2=ListNode(4)
l2_3=ListNode(5)
l2_2.next=l2_3
l2.next=l2_2

mySolu=Solution()
new_sorted=mySolu.merge_sorted_list(l1,l2)
print(new_sorted.val,new_sorted.next.val,new_sorted.next.next.val,new_sorted.next.next.next.val,new_sorted.next.next.next.next.val,new_sorted.next.next.next.next.next.val,new_sorted.next.next.next.next.next.next)

