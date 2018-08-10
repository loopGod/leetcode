#2.1.11 Remove Element
#描述
#Given an array and a value, remove all instances of that value in place and return the new length.
#The order of elements can be changed. It doesn’t matter what you leave beyond the new length.
class Solution:
    def Remove_Element(self, num, target):
        new_num=[]
        for i in num:
            if(i!=target):
                new_num.append(i)
        return new_num

muSolu=Solution()
new_num=muSolu.Remove_Element(num=[1,1,2,2,3,3,4,5,6,4,5,6], target=5)
print(new_num)