

# @3Sum Closest
# @return an integer;无序序列里面找到三个数和最接近目标值，返回组合值
#
# // Leet Code, Longest Consecutive Sequence
# // 时间复杂度O(n2)
#左右夹逼的方式
#threeSumClosest

class Solution:
    # @return a tuple, (index1, index2)
    def threeSumClosest(self, num, target):
        num.sort()
        print(num)
        for i in range(len(num)):
            first=i+1
            last=len(num)-1
            minC=abs(num[1]+num[last]+num[0]-target)
            while first<last:
                if(num[first]+num[last]+num[i]==target):
                    minC=0
                    minfirst=first
                    minlast=last
                    return [num[minfirst]+num[minlast]+num[i],[num[minfirst],num[minlast],num[i]]]
                if(num[first]+num[last]+num[i]<target):
                    if(abs(num[first]+num[last]+num[i]-target)<=minC):
                        minC=abs(num[first]+num[last]+num[i]-target)
                        minfirst=first
                        minlast=last
                        mini=i
                    first=first+1
                if(num[first]+num[last]+num[i]>target):
                    if(abs(num[first]+num[last]+num[i]-target)<=minC):
                        minC=abs(num[first]+num[last]+num[i]-target)
                        minfirst=first
                        minlast=last
                        mini=i
                    last=last-1
                print(minC)
        return [num[minfirst]+num[minlast]+num[mini],[num[minfirst],num[minlast],num[mini]]]
mSolu=Solution()
C=[]
C=mSolu.threeSumClosest(num=[-1, 2, 1, -4],target=1)
print(C)

#左右夹逼的方式,其实也是等同于2-1-7=twoSum
#twoSumClosest
'''
class Solution:
    # @return a tuple, (index1, index2)
    def twoSumClosest(self, num, target):

        num.sort()
        print(num)
        first=0
        last=len(num)-1
        minC=abs(num[first]+num[last]-target)

        while first<last:
            if(num[first]+num[last]==target):
                minC=abs(num[first]+num[last]-target)
                minfirst=first
                minlast=last
                return [minC,[num[minfirst],num[minlast]]]
            if(num[first]+num[last]<target):
                if(abs(num[first]+num[last]-target)<=minC):
                    minC=abs(num[first]+num[last]-target)
                    minfirst=first
                    minlast=last
                first=first+1
            if(num[first]+num[last]>target):
                if(abs(num[first]+num[last]-target)<=minC):
                    minC=abs(num[first]+num[last]-target)
                    minfirst=first
                    minlast=last
                last=last-1
        return [num[first]+num[last],[num[minfirst],num[minlast]]]

mSolu=Solution()
C=[]
C=mSolu.twoSumClosest(num=[-1, -2, -3, 0, 2, 3,4],target=0)
print(C)
'''


