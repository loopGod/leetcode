'''
3.4 Add Binary
描述
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return ”100”.
'''
#48,65,97
class Solution:
    def AddBinary(self,s1,s2):                          #n的左边链表
        result=''
        if len(s1)>=len(s2):
            s_1=s1
            s_2=s2
        else:
            s_1=s2
            s_2=s1
        s=list(str(int(s_1)+int(s_2)))
        flag=0
        for i in range(len(s)-1,-1,-1):
            if flag==1:
                s[i]=str(int(s[i])+1)
                flag=0
            if int(s[i])>=2:
                s[i]=str(int(s[i])-2)
                flag=1
        if flag==1:
            result='1'+''.join(s)
        else:
            result=''.join(s)
        return result
#字符串是不可变，和元祖一样
s1='11'
s2='1'
muSolu=Solution()
new_node=muSolu.AddBinary(s1,s2)
print(new_node)


