'''
2.2.4 Remove Duplicates from Sorted List
描述
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

class listNode:
    # @param num, a list of integer
    # @return a list of integer
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution:
    def removeDuplicates(self, head):                          #n的左边链表
        last_point=head
        point=head.next
        while point!=None:
            if point.val==last_point.val:
                last_point.next=point.next
            last_point=point
            point=point.next
        return head

l1=listNode(1)
l1_2=listNode(1)
l1_3=listNode(2)
l1_4=listNode(3)
l1_5=listNode(3)
l1.next=l1_2
l1_2.next=l1_3
l1_3.next=l1_4
l1_4.next=l1_5    

muSolu=Solution()
new_node=muSolu.removeDuplicates(l1)
print(new_node.val,new_node.next.val,new_node.next.next.val)#,new_node.next.next.next.val,new_node.next.next.next.next.val)

#test
'''
l1=listNode(3)
l1_2=listNode(6)
l1_3=listNode(4)
l1.next=l1_2
l1_2.next=l1_3  

l2=listNode(3)
l2_2=listNode(5)
l2_3=listNode(4)
l2.next=l2_2
l2_2.next=l2_3 

muSolu=Solution()
new_node=muSolu.rightList(l1,2)
print(new_node.val)#,new_node.next.val,new_node.next.next.val,new_node.next.next.next.val) 
'''



