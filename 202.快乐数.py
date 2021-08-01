#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    # 快慢指针
    # def isHappy(self, n: int) -> bool:
    #     def get_next(number):
    #         total_sum = 0
    #         while number > 0:
    #             number, digit = divmod(number, 10)
    #             total_sum += digit ** 2
    #         return total_sum

    #     slow_runner = n
    #     fast_runner = get_next(n)
    #     while fast_runner != 1 and slow_runner != fast_runner:
    #         slow_runner = get_next(slow_runner)
    #         fast_runner = get_next(get_next(fast_runner))
    #     return fast_runner == 1

    # 哈希表
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


# @lc code=end

print(Solution().isHappy(19))
