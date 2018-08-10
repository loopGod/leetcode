'''
2.2.2 Reverse Linked List I
描述
Reverse a linked list from position m to n. Do it in-place and in one-pass.
For example: Given 1->2->3->4->5->nullptr, m = 2 and n = 4,
return 1->4->3->2->5->nullptr.
Note: Given m, n satisfy the following condition: 1  m  n  length of list.
分析
这题非常繁琐，有很多边界检查，15 分钟内做到bug free 很有难度！

不妨拿出四本书，摞成一摞（自上而下为 A B C D），要让这四本书的位置完全颠倒过来（即自上而下为 D C B A）：

盯住书A，每次操作把A下面的那本书放到最上面

初始位置：自上而下为 A B C B

第一次操作后：自上而下为 B A C D

第二次操作后：自上而下为 C B A D

第三次操作后：自上而下为 D C B A
'''

class listNode:
    # @param num, a list of integer
    # @return a list of integer
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution:
     # @param head, a ListNode
     # 头插法，原链表滑动，中间链表尾部补齐新链表，新链表从none开始头插
     # @param n, an integer
     # @return a ListNode
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        new=None
        while head:
            p=head
            head=head.next
            p.next=new
            new=p
        return new
        
    #栈思路
    def reverseList2(self, head):
        p = head
        newList = []
        while p:
            newList.insert(0, p.val)
            p = p.next

        p = head
        for v in newList:
            p.val = v
            p = p.next
        return head

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
new_node=muSolu.reverseList2(l1)
print(new_node.val,new_node.next.val,new_node.next.next.val,new_node.next.next.next.val,new_node.next.next.next.next.val) 

