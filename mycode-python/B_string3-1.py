'''
3.1 Valid Palindrome
描述
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring
cases.
For example,
”A man, a plan, a canal: Panama” is a palindrome.
”race a car” is not a palindrome.
Note: Have you consider that the string might be empty? This is a good question to ask during an
interview.
For the purpose of this problem, we define empty string as valid palindrome.
'''
#48,65,97
class Solution:
    def ValidPalindrome(self, string):                          #n的左边链表
        n=len(string)-1
        left=0
        right=n 
        s=[ord(string[i]) for i in range(n+1)]
        while left<right:
            s[left]=ord(string[left])
            s[right]=ord(string[right])
            if s[left]>=65 and s[left]<=90:
                s[left]+=32
            if s[right]>=65 and s[right]<=90:
                s[right]+=32
            if s[left]<97 or s[left]>122:
                left+=1
                continue
            if s[right]<97 or s[right]>122:
                right-=1
                continue
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True

s='A man, a plan, a canal: Panama'
muSolu=Solution()
new_node=muSolu.ValidPalindrome(s)
print(new_node)

