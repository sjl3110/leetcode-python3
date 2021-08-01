#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
import array
from typing import List


# @lc code=start
class Solution:
    #双指针
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ret = min(height[left], height[right]) * (right - left)
        while left < right:
            ret = max(ret, min(height[left], height[right])*(right - left))
            if(height[left] <= height[right]):
                left += 1
            else:
                right -= 1
        return ret
# @lc code=end


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
s = Solution()
print(s.maxArea(height))
