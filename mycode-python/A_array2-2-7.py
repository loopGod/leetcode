'''
2.2.7 Remove Nth Node From End of List
描述
Given a linked list, remove the nth node from the end of list and return its head.
For example, Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
• Given n will always be valid.
• Try to do this in one pass.
'''

class listNode:
    # @param num, a list of integer
    # @return a list of integer
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution:
    def RotateList(self, head,k):                          #n的左边链表
        C_head=head
        count=0
        while C_head!=None:
            count+=1
            C_head=C_head.next
        if k>count:
            return head
        k0=count-k
        dummyhead=listNode('start')
        dummyhead.next=head
        start_point=dummyhead
        last_point=dummyhead
        point=head
        K_add=0
        while point!=None:
            K_add+=1
            if K_add<=k0:
                last_point=point
                point=point.next
            else:
                last_point.next=point.next
                return dummyhead.next

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
new_node=muSolu.RotateList(l1,2)
print(new_node.val,new_node.next.val,new_node.next.next.val,new_node.next.next.next.val)#,new_node.next.next.next.next.val)


