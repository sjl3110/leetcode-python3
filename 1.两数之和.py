#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
import array
from typing import List

# @lc code=start


# class Solution:
#     # 哈希表
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashtable = dict()
#         for i, num in enumerate(nums):
#             if target - num in hashtable:
#                 return [hashtable[target - num], i]
#             hashtable[nums[i]] = i
#         return []


class Solution:
    # 暴力法
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i]+nums[j]:
                    return [i, j]


# @lc code=end
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8
s = Solution()
print(s.twoSum(num, target))
