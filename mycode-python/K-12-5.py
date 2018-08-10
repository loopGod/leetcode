'''
12.5 Longest Substring Without Repeating Characters
描述
Given a string, find the length of the longest substring without repeating characters. For example, the
longest substring without repeating letters for ”abcabcbb” is ”abc”, which the length is 3. For ”bbbbb” the
longest substring is ”b”, with the length of 1.
分析
假设子串里含有重复字符，则父串一定含有重复字符，单个子问题就可以决定父问题，因此可
以用贪心法。跟动规不同，动规里，单个子问题只能影响父问题，不足以决定父问题。
从左往右扫描，当遇到重复字母时，以上一个重复字母的 index+1，作为新的搜索起始位置，
直到最后一个字母，复杂度是 O(n)。如图 12-1所示。
'''
def Longest_Substring(A):
	index=0
	res=0
	maxlen=0
	for i in range(len(A)):
		for j in range(index,i):
			if A[i]==A[j]:
				if len(A[index:i])>maxlen:
					maxlen=len(A[index:i])
					res=(A[index:i])
				index=j+1
	if len(A[index:len(A)])>maxlen:
		maxlen=len(A[index:len(A)])
		res=(A[index:len(A)])
	return maxlen,res
B='bbbbbbbb'
A = 'abcabcbbhjklm'
maxlen,res=Longest_Substring(B)
print(maxlen,res)