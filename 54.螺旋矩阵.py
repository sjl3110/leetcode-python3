#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
import array
from typing import List
# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix[0]), len(matrix)
        if m == 0 or n == 0:
            return ans
        left, right, top, bottom = 0, m-1, 0, n-1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            for j in range(top + 1, bottom + 1):
                ans.append(matrix[j][right])
            if left < right and top < bottom:
                for i in range(right - 1, left, -1):
                    ans.append(matrix[bottom][i])
                for j in range(bottom, top, -1):
                    ans.append(matrix[j][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return ans


# @lc code=end
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s = Solution()
print(s.spiralOrder(matrix))
