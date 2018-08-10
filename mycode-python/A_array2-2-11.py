'''
2.2.11 Linked List Cycle
描述
Given a linked list, determine if it has a cycle in it.
Follow up: Can you solve it without using extra space?
分析
最容易想到的方法是，用一个哈希表 unordered_map<int, bool> visited，记录每个元素是
否被访问过，一旦出现某个元素被重复访问，说明存在环。空间复杂度 O(n)，时间复杂度 O(N)。
最好的方法是时间复杂度 O(n)，空间复杂度 O(1) 的。设置两个指针，一个快一个慢，快
的指针每次走两步，慢的指针每次走一步，如果快指针和慢指针相遇，则说明有环。参考
http://leetcode.com/2010/09/detecting-loop-in-singly-linked-list.html
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

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False