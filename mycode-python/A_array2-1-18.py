'''
2.1.18 Climbing Stairs
描述
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    def ClimbingStairs(self, n):
        f=[0 for i in range(n+1)]
        f[1]=1
        f[2]=2
        for i in range(3,n+1):
            f[i]=f[i-1]+f[i-2]
        return f[n]

mySolu=Solution()
result=mySolu.ClimbingStairs(10)
print(result)


