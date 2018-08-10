'''
13.6 Interleaving String
描述
Given s1,s2,s3, find whether s3 is formed by the interleaving of s1 and s2.
For example, Given: s1 = ”aabcc”, s2 = ”dbbca”,
When s3 = ”aadbbcbcac”, return true.
When s3 = ”aadbbbaccc”, return false.
'''

class Solution():
    def Interleaving(self,A,B,C):
        l1=len(A)
        l2=len(B)
        l3=len(C)
        f=[[False for j in range(l2+1)] for i in range(l1+1)]
        if A[l1-1]==C[l1+l2-1]:
            f[l1-1][l2]=True
            l1=l1-1
        elif B[l2-1]==C[l1+l2-1]:
            f[l1][l2-1]=True
            l2=l2-1
        while l1>=0 or l2>=0:
            print(f)
            if l2>0 and B[l2-1]==C[l2+l1-1] and f[l1][l2]:
                l2=l2-1
                f[l1][l2]=True
                continue
            if l1>0 and A[l1-1]==C[l1-1+l2] and f[l1][l2]:
                l1=l1-1
                f[l1][l2]=True
                continue
            break
            
        return f[0][0]

A='aabcc'
B = 'dbbca'
C= 'aadbbcbcac'
#C='aadbbbaccc'
mySolu=Solution()
maxV=mySolu.Interleaving(A,B,C)
print(maxV)



