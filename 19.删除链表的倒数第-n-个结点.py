#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
import array

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 双指针
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        q = head
        while p:
            if n < 0:
                q = q.next
            n -= 1
            p = p.next
        if n == 0:
            return head.next
        q.next = q.next.next
        return head
# @lc code=end

