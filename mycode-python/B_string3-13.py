'''
3.13 Anagrams
描述
Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case.
分析
Anagram（回文构词法）是指打乱字母顺序从而得到新的单词，比如 "dormitory" 打乱字母顺
序会变成"dirty room" ，"tea" 会变成"eat"。
回文构词法有一个特点：单词里的字母的种类和数目没有改变，只是改变了字母的排列顺序。
因此，将几个单词按照字母顺序排序后，若它们相等，则它们属于同一组 anagrams 。
'''
#48,65,97
class Solution:
    def Anagrams(self,s):
        res=[]
        dict0={}
        for i in s:
            dict0[''.join(sorted(i))]=[i] if ''.join(sorted(i)) not in dict0 else dict0[''.join(sorted(i))]+[i]
        for i in dict0.values():
            res.append(i)
        return res
        
#字符串是不可变，和元祖一样
s=["eat", "tea", "tan", "ate", "nat", "bat"]
muSolu=Solution()
new_node=muSolu.Anagrams(s)
print(new_node)

'''
word='a1bc'
print(sorted(word))
'''

