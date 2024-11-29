#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        二分找到某个元素，若该元素小于右边元素，峰值在右边，更新left

        时间复杂度：O(lgn)
        空间复杂度：O(1)
        """
        left,right = -1,len(nums)-1
        while left+1<right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid
            else:
                right = mid
        return right
# @lc code=end

