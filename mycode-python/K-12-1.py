'''
12.1 Jump Game
描述
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
'''
def canJump(A):  
        index=0  
        reach=0  
        if len(A)<=1:  
            return True  
        while index<len(A):  
            if reach<index:  
                return False  
            reach=max(reach,A[index]+index)  
            index+=1  
        return True  
A = [3,2,2,0,4]
res=canJump(A)
print(res)