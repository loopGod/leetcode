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
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def diff(self,S1,S2):
        count=0
        if len(S1)!=len(S2):
            return -1
        else:
            for i in range(len(S1)):
                if(S1[i]!=S2[i]):
                    count+=1
            if count==1:
                return 1
            else:
                return -1

    def findLadders(self, beginWord, endWord, wordlist):
        ans,q = {},[]
        q.append(beginWord)
        ans[beginWord] = [[beginWord]]
        ans[endWord] = []
        while len(q) != 0:
            print(ans)
            tmp = q.pop(0)
            for i in range(len(beginWord)):
                part1,part2 = tmp[:i],tmp[i + 1:]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if tmp[i] != j:
                        newword = part1 + j + part2
                        if newword == endWord:
                            for k in ans[tmp]:
                                ans[endWord].append(k + [endWord])
                            while len(q) != 0:
                                 tmp1 = q.pop(0)
                                if len(ans[tmp1][0]) >= len(ans[endWord][0]):
                                    break
                                for ni in range(len(beginWord)):
                                    npart1,npart2 = tmp1[:ni],tmp1[ni+1:]
                                    for nj in "abcdefghijklmnopqrstuvwxyz":
                                        if tmp1[ni] != nj:
                                            nw = npart1 + nj + npart2
                                            if endWord == nw:
                                                for nk in ans[tmp1]:
                                                    ans[endWord].append(nk + [endWord])
                            break
                            
                        if newword in wordlist:
                            q.append(newword)
                            ans[newword] = []
                            for k in ans[tmp]:
                                ans[newword].append(k + [newword])
                            wordlist.remove(newword)
                        elif newword in ans and len(ans[newword][0]) == len(ans[tmp][0]) + 1:
                            for k in ans[tmp]:
                                ans[newword].append(k + [newword])
        return ans[endWord]
mySolu=Solution()
l=mySolu.findLadders('hit','cog', dict)
print(l)
