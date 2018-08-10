'''
2.1.16 Rotate Image
描述
You are given an n  n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up: Could you do this in-place?
'''
class Solution:
    def RotateImage(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix


image=[[1,2],
       [3,4]]
muSolu=Solution()
new_num=muSolu.RotateImage(image)
print(new_num) 

