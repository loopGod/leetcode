'''
9.1 Word Ladder
描述
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence
from start to end, such that:
• Only one letter can be changed at a time
• Each intermediate word must exist in the dictionary
For example, Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is ”hit” -> ”hot” -> ”dot” -> ”dog” -> ”cog”, return its length 5.
Note:
• Return 0 if there is no such transformation sequence.
• All words have the same length.
• All words contain only lowercase alphabetic characters.
'''
dict = ["hot","dot","dog","lot","log"]
class Solution:
    
    def ladderLength(self, start, end, dict):
        dict.append(end)
        q=[]
        q.append((start,1))
        while q:
            curr=q.pop(0)
            print(curr)
            curword=curr[0]
            curlen=curr[1]
            if curword==end:
                return curlen
            for i in range(len(curword)):
                part1=curword[:i]
                part2=curword[i+1:]
                for j in 'qwertyuiopasdfghjklzxcvbnm':
                    if curword[i]!=j:
                        nextword=part1+j+part2
                        if nextword in dict:
                            q.append((nextword,curlen+1))
                            dict.remove(nextword)
            return 0
mySolu=Solution()
l=mySolu.ladderLength('hit','cog', dict)
print(l)
