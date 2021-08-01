#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # a e i o u                                         #元音元素
        dic = {'a','e','i','o','u','A','E','I','O','U'}     #大小写元音元素集合作为判断依据
        left = 0                                             #左指针
        right = len(s)-1                                      #右指针
        lst = list(s)                                        #str类型数据无法直接查询in和not in，转换为list
        while left < right:                                    #左右指针交错循环停止
            if lst[left] in dic and lst[right] in dic:           #左右指针所指元素均在集合中
                lst[left], lst[right] = lst[right], lst[left]         #交换左右指针所指元素
                right -= 1                                    #右指针左移
                left += 1                                    #左指针右移
            if lst[right] not in dic:                          #右指针所指元素不在集合中
                right -= 1                                    #右指针左移
            if lst[left] not in dic:                          #左指针所指元素不在集合中
                left += 1                                    #左指针右移
        return ''.join(lst)                                  #返回str格式数据

# @lc code=end

