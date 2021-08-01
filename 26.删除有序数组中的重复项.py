#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
import array
from typing import List
# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0 or size == 1:
            return size
        k = 1
        for i in range(1, size):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
# @lc code=end


nums = [1, 1, 2, 2, 3, 3, 4, 5, 6]
s = Solution()
print(s.removeDuplicates(nums))
