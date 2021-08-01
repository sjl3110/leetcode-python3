#
# @lc app=leetcode.cn id=1104 lang=python3
#
# [1104] 二叉树寻路
#
import array
import math
from typing import List

# 假设不是之字形排列，而是顺序排列，已知目标值，求父节点路径怎么求？
# 只要对于每个数，除以2，取整，就是父节点的值，一直计算到1。就是父节点路径了。
# 针对上一步的结果，我们怎么求出取反层相应的值
# 最后一个我们肯定不用取反，因为是目标值，那从倒数第二层开始，每隔两层，我们计算一下取反的值
# 怎么取反呢？根据完全二叉树的特性，每一层的开始我们都知道，是 2**n (n从0开始)，所以要取反，可用下面公式
# 本行最大值 - （当前值 - 本行开始值）
# 总结: 理解完全二叉树，每行的个数、起始值，以及完全二叉树父子节点的关系，做出这道题就不难了。


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
