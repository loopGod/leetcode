'''
2.2.14 LRU Cache
描述
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the
following operations: get and set.
'''

class Node:
    # @param num, a list of integer
    # @return a list of integer
    def __init__(self, key, value):
        self.key=key
        self.val=value
        self.pre=None
        self.next=None

class DoubleLinkList:
    def __init__(self):                          #n的左边链表
        self.head=None
        self.tail=None

    def add_first(self, node):
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            h=self.head
            self.head=node
            self.head.next=h
            h.pre=self.head

    def remove(self, node):
        pre,next0=node.pre,node.next
        if pre:
            pre.next=next0
        else:
            self.head=next0
        if next0:
            pre.next=next0
        else:
            self.tail=pre

    def remove_last(self):
        if self.tail==None:
            return None
        else:
            tail=self.tail
            self.remove(tail)
            return tail

class LRUcache(object):
    """docstring for ClassName"""
    def __init__(self, capacity):
        self.capacity=capacity
        self.count=0
        self.douLinkList=DoubleLinkList()
        self.maps={}

    def get(self, key):
        if key not in self.maps:
            return None
        else:
            node=self.maps[key]
            self.douLinkList.remove(node)
            self.douLinkList.add_first(node)
            return node.val

    def set(self, key, value):
        if key not in self.maps:
            self.count+=1
            node=Node(key, value)
            self.maps[key]=node
            if self.count>self.capacity:
                tail=self.douLinkList.remove_last()
                self.count-=1
                del self.maps[tail.key]
            self.douLinkList.add_first(node)
        else:
            node=self.maps[key]
            node.val=value
            self.douLinkList.remove(node)
            self.douLinkList.add_first(node)

'''
l1=listNode(1)
l1_2=listNode(1)
l1_3=listNode(2)
l1_4=listNode(3)
l1_5=listNode(3)
l1.next=l1_2
l1_2.next=l1_3
l1_3.next=l1_4
l1_4.next=l1_5    
'''
muSolu=LRUcache(10)
muSolu.set(1,2)
res=muSolu.get(1)
print(res)

