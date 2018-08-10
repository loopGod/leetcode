'''
2.1.23 Single Number
描述
Given an array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using
extra memory?
'''
class Solution:
    def singleNumber(self,array):
        dict0={}
        for i in range(len(array)):
            if array[i] in dict0:
                del dict0[array[i]]
            else:
                dict0[array[i]]='once'
        for i in dict0.keys():
            return i

    def singleNumber2(self,array):
        res=0
        for i in array:
            res^=i
            print(res)
        return res
        
rating=[2,1,1,2,3,3,4,5,4]
mySolu=Solution()
result=mySolu.singleNumber(rating)
print(result)
result=mySolu.singleNumber2(rating)
print(result)


#进制转换
'''
print(int('11', 2))
print(bin(int('15', 10)))
for i in bin(int('15', 10)):
	print(i)
'''
'''
dicxx = {'a':'001', 'b':'002','c':'002'}
new_dict = {v:k for k,v in dicxx.items()}  # {'001': 'a', '002': 'b'}
print(new_dict['002'] ) # 'c'
'''


