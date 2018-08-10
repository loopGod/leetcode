'''
4.1.3 Largest Rectangle in Histogram
描述
Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
图4-1 Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
'''
#暴力法：遍历，从每个点左右扩展求面积;用栈：O(n)
class Solution(object):
	"""docstring for Solution"""
	def largestArea(self, his_list0):
		his_list.append(0)
		stack=[]
		maxArea=0
		for i in range(len(his_list)):
			if(stack==[] or his_list[i]>his_list[stack[-1]]):
				stack.append(i)
			else:
				while stack and (his_list[i]<his_list[stack[-1]]):
					lasti=stack.pop()
					maxArea=max(maxArea,(i-lasti)*his_list[lasti])
					#print(maxArea)
					#if(stack==[]):
				stack.append(lasti)
					#	break
		return maxArea

his_list=[2,1,5,6,3,4]
mySolu=Solution()
maxArea=mySolu.largestArea(his_list)
print(maxArea)

his_list=[4,3,6,5,1,2]
mySolu=Solution()
maxArea=mySolu.largestArea(his_list)
print(maxArea)

class Solution0(object):
    def largestRectangleArea(self, heights):
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

his_list=[2,1,5,6,3,4]
mySolu=Solution0()
maxArea=mySolu.largestRectangleArea(his_list)
print(maxArea)

his_list=[2,1,5,6,3,4][::-1]
mySolu=Solution0()
maxArea=mySolu.largestRectangleArea(his_list)
print(maxArea)
