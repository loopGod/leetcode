'''
2.1.21 Gas Station
描述
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next
station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station’s index if you can travel around the circuit once, otherwise return -1.
Note: The solution is guaranteed to be unique.
'''
class Solution:
    def gasStation(self,start,gas,cost):
        m=len(gas)
        rest=0
        for i in range(m):
            if i+start>=m:
                rest=rest+gas[i+start-m]-cost[i+start-m]
            else:
                rest=rest+gas[i+start]-cost[i+start]
            if rest < 0:
                return False
        return True

    def travel(self,gas,cost):
        m=len(gas)
        save=[]
        for i in range(len(gas)):
            if self.gasStation(i, gas, cost):
                save.append(i)
        if len(save)==0:
            return -1
        else:
            return save

#gas=[4,5,6,4,3,5]
gas=[3,4,5,6,4,4]
cost=[3,4,5,6,4,4]
mySolu=Solution()
result=mySolu. travel(gas,cost)
print(result)


#进制转换
'''
print(int('11', 2))
print(bin(int('15', 10)))
for i in bin(int('15', 10)):
	print(i)
'''


