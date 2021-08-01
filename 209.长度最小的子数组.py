#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
import array
from typing import List
# @lc code=start


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        ans, left, sums = 100000, 0, 0
        for i in range(size):
            sums += nums[i]
            while sums >= target:
                ans = min(ans, i+1-left)
                sums -= nums[left]
                left += 1
        return ans if ans != 100000 else 0


# @lc code=end
nums = [1, 4, 4]
print(Solution().minSubArrayLen(4, nums))
