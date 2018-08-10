'''
13.3 Palindrome Partitioning II
描述
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
For example, given s = ”aab”,
Return 1 since the palindrome partitioning [”aa”,”b”] could be produced using 1 cut.
'''

def Partitioning2(A):
    f=[0 for i in range(len(A)+1)]
    p=[[False for i in range(len(A))]for i in range(len(A))]
    for i in range(0,len(A)+1):
        f[i]=len(A)-1-i
    for i in range(len(A)-1,-1,-1):
        for j in range(i,len(A),1):
            if (A[i] == A[j] and (j - i < 2 or  p[i + 1][j - 1])):
                p[i][j] =True;
                f[i]=min(f[i],f[j+1]+1)
    return f[0]



A ='aabbbeccd'
res=Partitioning2(A)
print(res)
