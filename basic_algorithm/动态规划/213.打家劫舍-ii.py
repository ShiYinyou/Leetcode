#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def f(nums):
            n = len(nums)
            dp = [0]*(n+2)
            for i,x in enumerate(nums):
                dp[i+2] = max(dp[i+1],dp[i]+x)
            return dp[-1]
        return max(nums[0]+f(nums[2:n-1]),f(nums[1:]))
# @lc code=end

