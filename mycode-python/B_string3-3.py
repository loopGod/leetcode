'''
3.3 String to Integer (atoi)
描述
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and
ask yourself what are the possible input cases.
Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are respon-
sible to gather all the input requirements up front.
Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace
character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by
as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored
and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such
sequence exists because either str is empty or it contains only whitespace characters, no conversion is per-
formed.
If no valid conversion could be performed, a zero value is returned. If the correct value is out of the
range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''
#48,65,97
class Solution:
    def StringtoInteger(self,s):                          #n的左边链表
        number=0
        flag=1
        s=s.strip()
        if len(s)==0:
            return 0
        if s[0]=='-':
            flag=-1
            ds=s[1:]
        elif s[0]=='+':
            flag=1
            ds=s
        else:
            ds=s
        for i in ds:
            if ord(i)>=ord('0') and ord(i)<=ord('9'):
                number=number+ord(i)-ord('0')
            else:
                number+=ord(i)
        number=flag*number
        number=number if number<= 2147483647 else  2147483647
        number=number if number>=-2147483648 else -2147483647
        return number

s='-A man, a plan, a canal: Panama'
muSolu=Solution()
new_node=muSolu.StringtoInteger(s)
print(new_node)

