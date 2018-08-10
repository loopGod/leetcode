'''
12.4 Best Time to Buy and Sell Stock II
描述
Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie,
buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions
at the same time (ie, you must sell the stock before you buy again).
分析
贪心法，低进高出，把所有正的价格差价相加起来。
把原始价格序列变成差分序列，本题也可以做是最大 m 子段和，m = 数组长度。
'''
def Stock(A):
	profit=0
	Allvalue=0
	for i in range(len(A)-1):
		if A[i]<A[i+1]:
			profit=A[i+1]-A[i]
			Allvalue=Allvalue+profit
	return Allvalue

A = [2,3,1,1,4]
res=Stock(A)
print(res)