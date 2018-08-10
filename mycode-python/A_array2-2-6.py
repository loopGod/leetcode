'''
2.2.6 Rotate List
描述
Given a list, rotate the list to the right by k places, where k is non-negative.
For example: Given 1->2->3->4->5->nullptr and k = 2, return 4->5->1->2->3->nullptr.
分析
先遍历一遍，得出链表长度 len，注意 k 可能大于 len，因此令 k% = len。将尾节点 next 指针
指向首节点，形成一个环，接着往后跑 len   k 步，从这里断开，就是要求的结果了。
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
                tmp=point
                point=point.next
                tmp.next=start_point.next
                start_point.next=tmp
                start_point=tmp
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
print(new_node.val,new_node.next.val,new_node.next.next.val,new_node.next.next.next.val,new_node.next.next.next.next.val)


