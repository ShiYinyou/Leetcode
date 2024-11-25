#
# @lc app=leetcode.cn id=2779 lang=python3
#
# [2779] 数组的最大美丽值
#

# @lc code=start
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """
        由于要求的是子序列，对顺序没有要求，因此将数组排序
        当左窗口和右窗口元素之差不大于2k时满足要求

        时间复杂度：O(nlgn) 时间复杂度的限制是排序开销
        空间复杂度：O(1)
        """
        nums.sort()
        left = ans = 0
        for right,x in enumerate(nums):
            while x-nums[left]>2*k:
                left += 1
            ans = max(ans,right-left+1)
        return ans
# @lc code=end

