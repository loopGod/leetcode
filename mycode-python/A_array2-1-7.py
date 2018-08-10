'''
class Solution:
    # @param num, a list of integer
    # @return an integer;无序序列里面找到两个数和为目标值，返回索引(不是下标)-哈希表
    #如果是返回数，可以先排序后左右夹逼，O(nlogn)
    # // Leet Code, Longest Consecutive Sequence
    # // 时间复杂度O(n)
    def TwoSum(self, A,target):
        index=0
        dict={}
        for x in A:
            index=index+1
            dict[x]=index
        print(dict)
        # dict = {x: False x in dict } # False means not visited
        i=0
        for i in dict:#while是寻找某值，for是遍历
            if(i>=target):
                pass
            else:
                if(target-i in dict.keys()):
                    print(max(dict[i],dict[target-i]),min(dict[i],dict[target-i]))
                    return max(dict[i],dict[target-i]),min(dict[i],dict[target-i])
        print(-1)
        return -1

mSolu=Solution()
mSolu.TwoSum(A=[100, 4, 200, 6, 3, 2],target=102)
'''

#网上的哈希表，很简洁,边建hash表边判断
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in range(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x]+1, i+1)
            dict[x] = i
mSolu=Solution()
B=mSolu.twoSum(num=[100, 4, 101, 6, 1, 2],target=102)
print(B)

'''
#左右夹逼O(n2)
1，由于要找到符合题意的数组元素的下标，所以先要将原来的数组深拷贝一份，然后排序。

2，然后在排序后的数组中找两个数使它们相加为target。这个思路比较明显：
使用两个指针，一个指向头，一个指向尾，两个指针向中间移动并检查两个指针指向的数的和是否为target。如果找到了这两个数，再将这两个数在原数组中的位置找出来就可以了。

3，要注意的一点是：在原来数组中找下标时，需要一个从头找，一个从尾找，要不无法通过。
如这个例子：numbers=[0,1,2,0]; target=0。如果都从头开始找，就会有问题。

***while i<j:i=j为停止条件，左右两值偏大，右边的指针左移，如果偏大左边的右移；
'''