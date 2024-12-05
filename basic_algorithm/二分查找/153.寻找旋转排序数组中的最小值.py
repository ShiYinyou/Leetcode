#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        旋转后的数组可以看成两段，最小的元素在第二段的开头
        对于某个元素，如果这个元素大于最后一个元素，那么在第一段
        如果这个元素小于最后一个元素，那么在第二段

        时间复杂度：O(lgn)
        空间复杂度：O(1)
        """
        left, right = -1, len(nums)-1
        lst = nums[-1]
        while left+1 < right:
            mid = (left+right)//2
            if nums[mid] > lst:
                left = mid
            else:
                right = mid
        return nums[right]
# @lc code=end

