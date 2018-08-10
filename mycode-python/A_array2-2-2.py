'''
2.2.2 Reverse Linked List II
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
'''
class Solution:
     # @param head, a ListNode
     # @param m, an integer
     # @param n, an integer
     # @return a ListNode
    def reverseList(self, head, m, n):
        if head is None or head.next is None:
             return head
        dummyhead = listNode(0)
        dummyhead.next = head
        
        p = dummyhead
         
        for i in range(m-1):
            p = p.next 
         
        curr = p.next
        for i in range(n-m):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = p.next
            p.next = tmp
             
        return dummyhead.next
'''

class Solution:
     # @param head, a ListNode
     # @param m, an integer
     # @param n, an integer
     # @return a ListNode
    def leftList(self, head, m, n):                          #n的左边链表
        if head is None or head.next is None:
             return head
        head2=head
        new=None
        for i in range(m-1):
            head2 = head2.next
        
        for i in range(n-m+1):
            p=head2
            head2=head2.next
            p.next=new
            new=p
        root=head      #链表的拼接，很重要
        tmp=root  
        for i in range(m-2):       #      
            tmp=tmp.next
        tmp.next=new
        return root            # 返回根节点 

    def rightList(self,head,n):                        #n的右边链表
        tmp=head
        for i in range(n):       #      
            tmp=tmp.next
        return tmp

    def onePlusone(self,l1,l2):#连接两个链表          #到时候左右相拼接
        root=l1
        temp=root
        while temp:
            last_temp=temp
            temp=temp.next
        last_temp.next=l2
        return root

    
'''
        root2=head      #链表的拼接，很重要
        tmp=root2  
        new_root=root
        new_tmp=new_root
        while new_tmp :      #      
            tmp=tmp.next
            new_tmp=new_tmp.next
            print(tmp.val)
        new_tmp.next=tmp.next
        return new_tmp            # 返回根节点 
'''

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
m=2
n=4
right_node=muSolu.rightList(l1,n)
left_node=muSolu.leftList(l1,m,n)
new_node=muSolu.onePlusone(left_node,right_node)
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



