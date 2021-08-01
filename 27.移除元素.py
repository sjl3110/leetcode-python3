#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index ,size = 0, len(nums)
        for i in range(0, size):
            if nums[i] != val:
                nums[index] = nums[i]
                index +=1
            elif nums[i] == val:
                size -=1
        return size
# @lc code=end

