#
# @lc app=leetcode.cn id=1104 lang=python3
#
# [1104] 二叉树寻路
#
import array
import math
from typing import List

# @lc code=start


# class Solution:
#     def pathInZigZagTree(self, label: int) -> List[int]:
#         row = int(math.log2(label))+1
#         ans = [0]*row
#         while row:
#             ans[row-1] = label
#             label = (2**row-1-label+2**(row-1))//2
#             row -= 1

#         return ans


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        # 先把不是Z字型的父节点算出来，顺序完全二叉树的父节点是 node//2
        res = []
        while label != 1:
            res.append(label)
            label //= 2

        res.append(1)
        res.reverse()

        # 从倒数第二个开始，每隔一个，找出取反相对应的值
        for i in range(len(res)-2, -1, -2):
            original = res[i]
            start = 2**i
            end = 2**(i+1)
            new = end - 1 - (original - start)
            res[i] = new

        return res


# @lc code=end
s = Solution()
label = 14
print(s.pathInZigZagTree(label))
