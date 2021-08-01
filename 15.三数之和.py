#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
import array
from typing import List

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            third, target = n - 1, -nums[first]
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


# @lc code=end
s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))
