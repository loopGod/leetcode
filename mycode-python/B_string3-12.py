'''
3.12 Count and Say
描述
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2", then "one 1" or 1211.
Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.
'''
#48,65,97
class Solution:
    def CountSet(self,s,setS):
        s+='0'
        index=0
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                setS+=str(i-index)
                index=i
                setS+=str(s[i-1])
                self.CountSet(s[i:], setS)
        return setS

    def CountandSay(self, n):
        s='1'
        for i in range(n-1):
            s=self.CountSet(s,'')
        return s
        
#字符串是不可变，和元祖一样

muSolu=Solution()
new_node=muSolu.CountandSay(4)
print(new_node)


