'''
8.6 Letter Combinations of a Phone Number
描述
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.148 

Input:Digit string ”23”
Output: [”ad”, ”ae”, ”af”, ”bd”, ”be”, ”bf”, ”cd”, ”ce”, ”cf”].
Note: Although the above answer is in lexicographical order, your answer could be in any order you
want
'''

class Solution(object):
    def addDigit(self,digit,ans):
        tmp = []
        for element in digit:
            if len(ans) == 0:
                tmp.append(element)
            for s in ans:
                tmp.append(s + element)
        return tmp
    def letterCombinations(self, digits):
       
        ans = []
        d = {'0':' ','1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        for element in digits:
            ans = self.addDigit(d[element],ans)
        return ans

S='234'
mySolu=Solution()
lis=mySolu.letterCombinations(S)
print(lis)