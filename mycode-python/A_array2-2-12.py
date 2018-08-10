'''
2.2.12 Linked List Cycle II
描述
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Follow up: Can you solve it without using extra space?
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

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None