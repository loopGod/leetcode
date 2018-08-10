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
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        try:
            while True:
                pre, cur, nxt = cur, cur.next, cur.next.next
                # change the position of cur and nxt
                pre.next, cur.next, nxt.next = nxt, nxt.next, cur
                # now cur is in the third place
        except:
            return dummy.next
            
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


