#
# @lc app=leetcode.cn id=2302 lang=python3
#
# [2302] 统计得分小于 K 的子数组数目
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        找到一个符合要求的窗口后，固定右端点，左端点以内所有数均满足要求

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        ans = left = s = 0
        for right,x in enumerate(nums):
            s += x
            while s*(right-left+1) >= k:
                s -= nums[left]
                left += 1
            ans += right-left+1
        return ans
# @lc code=end

