class Solution():
    def BestStock1(self,A):
        minV=A[0]
        maxV=0
        for i in range(len(A)):
            if A[i]<minV:
                minV=A[i]
            maxV=max(maxV,A[i]-minV)
        return maxV

    def BestStock3(self,A_price):
        maxV=0
        for i in range(len(A_price)-1):
            A_1=A_price[0:i+1]
            A_2=A_price[i:len(A_price)]
            maxV=max(maxV,self.BestStock1(A_1)+self.BestStock1(A_2))
        return maxV

B=[5,2,8,4,3,1,6,5,8,9]
mySolu=Solution()
maxV=mySolu.BestStock3(B)
print(maxV)



