'''
3.11 Roman to Integer
描述
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''
#48,65,97
class Solution:
    def romanToInt(self, s):
        numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        sum=0
        s=s[::-1]
        last=None
        for x in s:
            if last and numerals[x]<last:
                sum-=2*numerals[x]
            sum+=numerals[x]
            last=numerals[x]
        return sum
        
#字符串是不可变，和元祖一样
s='DCLXVI'
muSolu=Solution()
new_node=muSolu.romanToInt(s)
print(new_node)


