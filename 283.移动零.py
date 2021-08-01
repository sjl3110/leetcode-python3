#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from typing import List
# @lc code=start


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]  # 左右指针内容互换
                l += 1
            r += 1
# @lc code=end


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)
