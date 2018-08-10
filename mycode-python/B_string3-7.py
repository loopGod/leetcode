'''
3.7 Wildcard Matching
描述
Implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character. '*' Matches any sequence of characters (including the empty se-
quence).
The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''
#48,65,97
class Solution:
    def isMatch(self,s,p):  
        sLen = len(s)
        pLen = len(p)
        if (pLen == 0):
            return sLen == 0
        if (pLen == 1):
            if (p == s) or ((p == '?') and (len(s) == 1)) or  ((p == '*') and (len(set(s)) == 1)):
                return True
            else:
                return False
        #p的最后一个字符不是'*'也不是'.'且不出现在s里，p跟s肯定不匹配
        if (p[0] != '*') and (p[0] != '?') and (p[0] !=s[0]):
            return False
        if p[0]=='?':
            return self.isMatch(s[1:],p[1:])
        elif p[0]=='*':
            tmp=s[0]
            while s[0]==tmp:
                s=s[1:]
            return self.isMatch(s,p[1:])
        elif s[0]==p[0]:
            return self.isMatch(s[1:],p[1:])
        return
    ''' 
        if (p[1] != '*'):
            if (len(s) > 0) and ((p[0]==s[0]) or (p[0]=='.')):
                return self.isMatch(s[1:],p[1:])
            return False
        else:
            while (len(s) > 0) and ((p[0]==s[0]) or (p[0]=='.')):
                if (self.isMatch(s,p[2:])):
                    return True
                s = s[1:]
            return self.isMatch(s,p[2:])
        return
    '''
#字符串是不可变，和元祖一样
s1='ab'
s2='?*'
muSolu=Solution()
new_node=muSolu.isMatch(s1,s2)
print(new_node)


