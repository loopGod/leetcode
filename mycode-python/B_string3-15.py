'''
3.15 Length of Last Word
描述
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length
of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
For example, Given s = "Hello World", return 5.
'''
#48,65,97
class Solution:
    def LengthLastWord(self,s):
        sList=s.split(' ')
        return len(sList[-1])
        
#字符串是不可变，和元祖一样
s="Hello World"
muSolu=Solution()
new_node=muSolu.LengthLastWord(s)
print(new_node)

'''
word='a1bc'
print(sorted(word))
'''


