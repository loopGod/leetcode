'''
2.1.15 Trapping Rain Water
描述
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute
how much water it is able to trap after raining.
For example, Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def RainWater(self, water):
      if len(water)<=1:
        return 0
      lmax=0
      rmax=0
      lindex=0
      rindex=len(water)-1
      lsum=rsum=msum=0
      lmaxline=[0 for i in range(len(water))]
      rmaxline=[0 for i in range(len(water))]
      for i in range(len(water)):
        if water[i]>lmax:
          lmax=water[i]
          lindex=i
        lmaxline[i]=lmax
      for i in range(len(water)-1,-1,-1):
        if water[i]>rmax:
          rmax=water[i]
          rindex=i
        rmaxline[i]=rmax
      for i in range(len(water)):
        if i <lindex or i>rindex:
          if lmaxline[i]<lmax:
            lsum+=min(lmaxline[i],lmax)-water[i]
          if rmaxline[i]<rmax:
            rsum+=min(rmaxline[i],lmax)-water[i]
        elif i>=lindex and i<=rindex:
          msum+=lmax-water[i]
      return lsum+rsum+msum


water=[0,1,0,2,1,0,1,3,2,1,2,1]
muSolu=Solution()
new_num=muSolu.RainWater(water)
print(new_num) 

