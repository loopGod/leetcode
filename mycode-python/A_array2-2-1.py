'''
2.2.1 Add Two Numbers
描述
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse
order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

class listNode:
    # @param num, a list of integer
    # @return a list of integer
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def twoNumAdd(self, l1, l2):
        twoSum=listNode(0)
        inttwoSum=twoSum
        upOne=0
        if(not l1):
            return l2
        if(not l2):
            return l1
        while(l1 or l2):  
            if(l1 and l2):
                if int((l1.val+l2.val)/10):
                    if(upOne):
                        twoSum.val=(l1.val+l2.val+1)%10
                    else:
                        twoSum.val=(l1.val+l2.val)%10
                    upOne=1
                else:
                    if(upOne):
                        twoSum.val=l1.val+l2.val+1
                    else:
                        twoSum.val=l1.val+l2.val
                    upOne=0
            elif(l1 and not l2):
                if(upOne and l1.val==9):
                    twoSum.val=0
                    upOne=1
                if(upOne and l1.val!=9):
                    twoSum.val=l1.val
                    upOne=0
                else:
                    twoSum.val=l1.val
                    upOne=0
            elif(not l1 and l2):
                if(upOne and l2.val==9):
                    twoSum.val=0
                    upOne=1
                if(upOne and l2.val!=9):
                    twoSum.val=l2.val
                    upOne=0
                else:
                    twoSum.val=l2.val
                    upOne=0
            l1=l1.next
            l2=l2.next
            print(twoSum.val)
            twoSum.next=listNode(0)
            twoSum=twoSum.next
        return inttwoSum


l1=listNode(3)
l1_2=listNode(6)
l1_3=listNode(4)
l1.next=l1_2
l1_2.next=l1_3  

l2=listNode(3)
l2_2=listNode(6)
l2_3=listNode(4)
l2.next=l2_2
l2_2.next=l2_3 

muSolu=Solution()
new_node=muSolu.twoNumAdd(l1,l2)
print(new_node.val,new_node.next.val,new_node.next.next.val,) 

