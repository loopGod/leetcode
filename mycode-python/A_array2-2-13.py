'''
2.2.13 Reorder List
描述
Given a singly linked list L : L0 ! L1 !    ! Ln 1 ! Ln, reorder it to: L0 ! Ln ! L1 !
Ln 1 ! L2 ! Ln 2 !   
You must do this in-place without altering the nodes’ values.
For example, Given {1,2,3,4}, reorder it to {1,4,2,3}.
分析
题目规定要in-place，也就是说只能使用 O(1) 的空间。
可以找到中间节点，断开，把后半截单链表 reverse 一下，再合并两个单链表。
'''

# Definition for singly-linked list.
class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1=listNode(1)
l1_2=listNode(1)
l1_3=listNode(2)
l1_4=listNode(3)
l1_5=listNode(3)
l1.next=l1_2
l1_2.next=l1_3
l1_3.next=l1_4
l1_4.next=l1_5    

maps={}
maps[l1]=1
print(maps)
#以上说明实例对象可以作为字典的Key，因此此题可以用哈希表

#快慢指针的方法很巧妙
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head==None or head.next==None or head.next.next==None: return head
        
        # break linked list into two equal length
        slow = fast = head                              #快慢指针技巧
        while fast and fast.next:                       #需要熟练掌握
            slow = slow.next                            #链表操作中常用
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse linked list head2
        dummy=ListNode(0); dummy.next=head2             #翻转前加一个头结点
        p=head2.next; head2.next=None                   #将p指向的节点一个一个插入到dummy后面
        while p:                                        #就完成了链表的翻转
            tmp=p; p=p.next                             #运行时注意去掉中文注释
            tmp.next=dummy.next
            dummy.next=tmp
        head2=dummy.next

        # merge two linked list head1 and head2
        p1 = head1; p2 = head2
        while p2:
            tmp1 = p1.next; tmp2 = p2.next
            p1.next = p2; p2.next = tmp1
            p1 = tmp1; p2 = tmp2