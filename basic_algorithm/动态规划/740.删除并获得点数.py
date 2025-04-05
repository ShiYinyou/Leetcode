#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        动态规划
        不选相邻的，选了一个数，相同的就全选
        参考 198. 打家劫舍
        """
        n = max(nums)
        cnt = [0]*(n+1)
        for x in nums:
            cnt[x]+=x
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = max(dp[i-2]+cnt[i], dp[i-1])
        return dp[n]

# @lc code=end

