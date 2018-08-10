'''
2.1.17 Plus One
描述
Given a number represented as an array of digits, plus one to the number.
'''
class Solution:
    def PlusOne(self, arrayD):
        if len(arrayD)==0:
            return [1]
        result1=[1]
        stack=[-2]
        arrayD[len(arrayD)-1]=arrayD[len(arrayD)-1]+1
        for i in range(len(arrayD)-1,-1,-1):
            if stack[0]==i+1:
                arrayD[i]=arrayD[i]+1
            if arrayD[i]==10:
                stack[0]=i
                arrayD[i]=0
        if stack[0]==0:
            result1.extend(arrayD)
            result=result1
        else:
            result=arrayD
        return result
arrayD=[9,9,9,9,9]
mySolu=Solution()
result=mySolu.PlusOne(arrayD)
print(result)


