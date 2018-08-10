'''
2.2.5 Remove Duplicates from Sorted List II
描述
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers
from the original list.
For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

class listNode:
    # @param num, a list of integer
    # @return a list of integer
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution:
    def removeDuplicates2(self, head):                          #n的左边链表
        if head.next==None or head==None:
            return head
        last_point=listNode('start')
        point=head
        last_point.next=point
        root=last_point
        while point!=None and point.next!=None:
            if point.val==point.next.val:
                pValue=point.val
                while point.val==pValue :
                    if point.next!=None:
                        last_point.next=point.next
                        point=point.next
                    else:
                        last_point.next=point.next
                        point=point.next
                        break
            else:
                last_point=point
                point=point.next
        return root.next

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
new_node=muSolu.removeDuplicates2(l1)
print(new_node.val)#,new_node.next.val)#,new_node.next.next.val)#,new_node.next.next.next.val,new_node.next.next.next.next.val)

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



