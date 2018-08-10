'''
3.8 Longest Common Prefix
描述
Write a function to find the longest common prefix string amongst an array of strings.
'''
#48,65,97
class Solution:
    def twoPrefix(self,s1,s2):
        if len(s1)<len(s2):
            s2=s2[:len(s1)]
        if len(s2)<len(s1):
            s1=s1[:len(s2)]
        while s1!=s2:
            #s1=s1[:len(s1)-1]
            #s2=s2[:len(s2)-1]
            return self.twoPrefix(s1[:len(s1)-1], s2[:len(s2)-1])
        return s1
    
    def LongestCommonPrefix(self,s):
        tmp=s[0]
        for i in range(len(s)):
            tmp=self.twoPrefix(tmp, s[i])
            if tmp=='':
                return ''
        return tmp



#字符串是不可变，和元祖一样
s=['123789','1234987','12456']
muSolu=Solution()
new_node=muSolu.LongestCommonPrefix(s)
print(new_node)


s1='123789'
s2='1234987'
muSolu=Solution()
new_node=muSolu.twoPrefix(s1,s2)
print(new_node)


