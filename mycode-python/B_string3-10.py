'''
3.10 Integer to Roman
描述
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
'''
#48,65,97
class Solution:
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        return list
        
#字符串是不可变，和元祖一样
s=1258
muSolu=Solution()
new_node=muSolu.intToRoman(s)
print(new_node)


