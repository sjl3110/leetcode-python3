#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
import array
import math
from typing import List
# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        N = int((size+1)/2)
        for count in range(N):
            if count >= size - 1 - count:
                break
            for i in range(count,size - 1 - count):
                tmp = matrix[size - 1 - i][count]  # 保存左下顶点
                matrix[size - 1 - i][count] = matrix[size - 1 - count][size - 1 - i]  # 左下顶点 = 右下顶点
                matrix[size - 1 - count][size - 1 - i] = matrix[i][size - 1 - count]  # 右下顶点 = 右上顶点
                matrix[i][size - 1 - count] = matrix[count][i]  # 右上顶点 = 左上顶点
                matrix[count][i] = tmp  # 左上顶点 = 左下顶点


# @lc code=end
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)
print(matrix)
