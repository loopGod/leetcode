'''
2.1.22 Candy
描述
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
• Each child must have at least one candy.
• Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''
class Solution:
    def candy(self,rating):
        candyNum=[1 for i in range(len(rating))]
        for i in range(1,len(rating)):
            if rating[i]==rating[i-1]:
                candyNum[i]=candyNum[i-1]
            if rating[i]>rating[i-1]:
                candyNum[i]=candyNum[i-1]+1
        for i in range(len(rating)-2,-1,-1):
            if rating[i]>rating[i+1] and candyNum[i+1]+1>candyNum[i]:
                candyNum[i]=candyNum[i+1]+1
        return sum(candyNum)
rating=[2,1,1,2,3,3,2,2,3]
mySolu=Solution()
result=mySolu.candy(rating)
print(result)


#进制转换
'''
print(int('11', 2))
print(bin(int('15', 10)))
for i in bin(int('15', 10)):
	print(i)
'''


