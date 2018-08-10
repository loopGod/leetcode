'''
3.2 Implement strStr()
描述
Implement strStr().
Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
'''
#48,65,97
class Solution:
    def ImplementStr(self, s1,s2):                          #n的左边链表
        if len(s2)==0:
            return 0
        if len(s2)>len(s1):
            return -1
        n=len(s1)-len(s2)+1
        i_s1=0
        while i_s1<=n:
            for i in range(len(s2)):
                if s2[i]==s1[i_s1+i]:
                    if i==len(s2)-1:
                        return i_s1
                    else:
                        continue
                else:
                    i_s1+=1
                    break
        return -1

s1='A man, a plan, a canal: Panama'
s2='ana'
muSolu=Solution()
new_node=muSolu.ImplementStr(s1,s2)
print(new_node)

