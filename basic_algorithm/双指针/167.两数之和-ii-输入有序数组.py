#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        题目给出的是一个有序数组，相向双指针从两端向中间寻找答案
        本题需要注意下标从1开始
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        left, right = 0, len(numbers)-1
        while left < right:
            x = numbers[left] + numbers[right]
            if x < target:
                left += 1
            elif x > target:
                right -= 1
            else:
                return [left+1, right+1]
# @lc code=end

