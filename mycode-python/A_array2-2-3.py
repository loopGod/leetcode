'''
2.2.3 Partition List
描述
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater
than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
For example, Given 1->4->3->2->5->2 and x = 3, return 1->2->2->4->3->5.
'''

class listNode:
    # @param num, a list of integer
    # @return a list of integer
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution:
    def partitionList(self, head, x):                          #n的左边链表
        C_head=listNode('start')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        C_head.next=head
        point_last=C_head
        C2_head=head
        while C2_head!=None:
            if C2_head.val>=x:
                point=C2_head
                break
            if C2_head.next==None:
                return head
            else:
                point_last=C2_head
                C2_head=C2_head.next
        C3_head=point
        C3_head_last=point_last
        while C3_head!=None:
            if C3_head.val<x:
                C3_head_last.next=C3_head.next
                point_last.next=C3_head
                C3_head.next=point
                point_last=C3_head
            C3_head_last=C3_head
            C3_head=C3_head.next
        return C_head.next

l1=listNode(3)
l1_2=listNode(6)
l1_3=listNode(4)
l1_4=listNode(1)
l1_5=listNode(2)
l1.next=l1_2
l1_2.next=l1_3
l1_3.next=l1_4
l1_4.next=l1_5    

muSolu=Solution()
new_node=muSolu.partitionList(l1, 4)
print(new_node.val,new_node.next.val,new_node.next.next.val,new_node.next.next.next.val,new_node.next.next.next.next.val)

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



