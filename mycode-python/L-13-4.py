class Solution():
    def largestArea(self, heights):
        heights.append(0)
        mans = 0
        ans,ansindex,i = [],[],0
        while i < len(heights):
            if ans==[] or heights[i] >= ans[-1]:
                ans.append(heights[i])
                ansindex.append(i)
            else:
                lastindex = 0
                while ans and ans[-1] > heights[i]:
                    tmp = ans.pop()
                    lastindex = ansindex.pop()
                    mans = max(mans,tmp*(i - lastindex))
                ans.append(heights[i])
                ansindex.append(lastindex)
            i += 1
        return mans

    def maxRec(self, A):
        maxArea=0
        for i in range(len(A)):
            if i>0:
                for j in range(len(A[0])-1):
                    if A[i][j]==1 and A[i-1][j]!=0:
                        A[i][j]=A[i-1][j]+1
                tmpArea=self.largestArea(A[i])
                maxArea=max(maxArea,tmpArea)
        return maxArea

B=[[0,0,1,0],
   [0,0,1,1],
   [0,1,1,1],
   [0,0,1,0]]
mySolu=Solution()
maxArea=mySolu.maxRec(B)
print(maxArea)

