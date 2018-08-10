# @3Sum Closest
# @return an integer;无序序列里面找到4个数和等于目标值，返回组合值
#
# // Leet Code, Longest Consecutive Sequence
# // 时间复杂度O(n2)
#左右夹逼+hashMap的方式
#fourSum
#先排序，然后左右夹逼，复杂度O(n3)，会超时。
#可以用一个hashmap 先缓存两个数的和，最终复杂度O(n3)。这个策略也适用于3Sum 。
#如对于num=[1,2,3,2]来说，dict={3:[(0,1),(0,3)], 4:[(0,2),(1,3)], 5:[(1,2),(2,3)]}。
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        numLen, res, dict = len(num), set(), {}
        if numLen < 4: return []
        num.sort()
        for p in range(numLen):
            for q in range(p+1, numLen): 
                if num[p]+num[q] not in dict:
                    dict[num[p]+num[q]] = [(p,q)]
                else:
                    dict[num[p]+num[q]].append((p,q))
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target-num[i]-num[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j: res.add((num[i],num[j],num[k[0]],num[k[1]]))
        return [list(i) for i in res]

