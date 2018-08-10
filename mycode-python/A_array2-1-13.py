'''
2.1.12 Next Permutation
描述
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation
of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending
order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the
right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
就是全排列中的下一个排列组合，大小关系是上一个排列紧接着大的一个排列，
其中递增拍列为第一个，递减序列为最后一个拍列；

解题思路：输出字典序中的下一个排列。比如123生成的全排列是：123，132，213，231，312，321。
那么321的next permutation是123。下面这种算法据说是STL中的经典算法。
在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换，
然后将partition后的元素（不包括partition指向的元素）逆序排列。比如14532，那么升序对为45，
partition指向4，由于partition之后除了5没有比4大的数，所以45交换为54，即15432，
然后将partition之后的元素逆序排列，即432排列为234，则最后输出的next permutation为15234。确实很巧妙。
'''
'''
2.1.13 Permutation Sequence
描述
The set [1,2,3,⋯,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive.
分析
简单的，可以用暴力枚举法，调用k - 1 次next_permutation()。
暴力枚举法把前k 个排列都求出来了，比较浪费，而我们只需要第k 个排列。
利用康托编码的思路，假设有n 个不重复的元素，第k 个排列是a1; a2; a3; :::; an，那么a1是
哪一个位置呢？
我们把a1 去掉，那么剩下的排列为a2; a3; :::; an, 共计n􀀀1 个元素，n􀀀1 个元素共有(n􀀀1)!
个排列，于是就可以知道a1 = k/(n 􀀀 1)!。
下面是暴力法
'''
'''
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) <= 1: return num
        partition = -1
        for i in range(len(num)-2, -1, -1):#*******这种反序切记
            if num[i] < num[i+1]:
                partition = i
                break
        if partition == -1: 
            num.reverse()
            return num
        else:
            for i in range(len(num)-1, partition, -1):
                if num[i] > num[partition]:
                    num[i],num[partition] = num[partition],num[i]
                    break
        left = partition+1; right = len(num)-1
        while left < right:
            num[left],num[right] = num[right],num[left]
            left+=1; right-=1
        return num

    def kPermutation(self,n,k):
        num=[]
        for i in range(1,n+1,1):
            num.append(i)
        if(k==1) :
            return num
        else:
            for j in range(0,k-1,1):
                knum=self.nextPermutation(num)
            return knum

muSolu=Solution()
new_num=muSolu.kPermutation(3,3)
print(new_num)
'''

#康托编码
import math

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def kPermutation(self, n, k):
        k=k-1
        num=[1,2,3,4,5,6,7,8,9]
        ai=[]
        ki=[]
        new_a=[]
        for i in range(n):
            if(i==0):
                ai.append(int(k/math.factorial(n-1)))
                ki.append(k%math.factorial(n-1))
                new_a.append(num[ai[i]])
            else:
                ai.append(int(ki[i-1]/math.factorial(n-i-1)))
                ki.append(ki[i-1]%math.factorial(n-i-1))
                new_a.append(num[ai[i]])
            num.remove(num[ai[i]])
        return new_a
muSolu=Solution()
new_num=muSolu.kPermutation(4,17)
print(new_num) 

'''
1234
1243
1324
1342
1423
1432
2134
2143
2314 
2341
2413
2431
3124
3142
3214
3241
3412    <--- k = 17
3421
4123
4132
4213
4231
4312
4321
'''