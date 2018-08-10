

# @param num, a list of integer
# @return an integer;无序序列里面找到三个数和为目标值0，返回所有的组合值
#
# // Leet Code, Longest Consecutive Sequence
# // 时间复杂度O(n2)
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        B=[]
        for i in range(len(num)):
            x = num[i]
            if target-x in dict:
                B.append([target-x, x]) #2sum下将所有情况输出
            dict[x] = i
        return B

    def threeSum(self, num):
        C=[]
        for y in num:
            num2=num.copy()
            num2.remove(y)
            B=self.twoSum(num2, -y)
            print(B)
            if(B):
                for z in B:
                    z.append(y)
                    z.sort()    #去重复，这一步骤很重要
                    if(z in C):
                        pass
                    else:
                        C.append(z)
        return C

mSolu=Solution()
C=[]
C=mSolu.threeSum(num=[-1, -2, -3, 0, 1, 2,3])
print(C)
'''
mSolu=Solution()
B=mSolu.twoSum(num=[100, 4, 101, 6, 1, 2],target=102)
print(B)
'''
a=[1,2,3]
b=a
b.append(4)
print(b)


