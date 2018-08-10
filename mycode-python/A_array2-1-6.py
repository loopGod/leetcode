'''
class Solution:
    # @param num, a list of integer
    # @return an integer;无序序列里面找到最大的连续序列的长度-哈希表
    # // Leet Code, Longest Consecutive Sequence
    # // 时间复杂度O(n)，空间复杂度O(n)
    def longestConsecutive(self, num):
        dict = {x: False for x in num} # False means not visited
        maxLen = -1
        for i in dict:
            if dict[i] == False:
                curr = i+1; lenright = 0
                while curr in dict:
                    lenright += 1; dict[curr] = True; curr += 1
                curr = i-1; lenleft = 0
                while curr in dict:
                    lenleft += 1; dict[curr] = True; curr -= 1
                maxLen = max(maxLen, lenleft+1+lenright)
        print(maxLen)
        return maxLen

mSolu=Solution()
mSolu.longestConsecutive(num=[100, 4, 200, 1, 3, 2])
'''
A=[100, 4, 200, 1, 3, 2]
def Mysolution(A):
    maxlen=-1;
    dict={x:False for x in A }
    for i in dict:
        cur=0;
        if(dict[i]==False):
            dict[i]=True;
            cur=i+1;lenright=0;#向右扩张
            while cur in dict:
                lenright=lenright+1;dict[cur]=True;cur=cur+1;
            cur=i-1;lenleft=0;#向左扩张
            while cur in dict:
                lenleft=lenleft+1;dict[cur]=True;cur=cur-1;
        maxlen=max(maxlen,lenleft+lenright+1)
    print(maxlen)
    return maxlen
Mysolution(A)
