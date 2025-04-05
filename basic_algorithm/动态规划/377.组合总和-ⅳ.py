#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        动态规划：从组合型回溯变形
        """
        n = len(nums)
        ### 1. 记忆化搜索
        # @cache
        # def dfs(target):
        #     if target == 0:
        #         return 1
        #     return sum([dfs(target-x) for x in nums if x<=target])
        # return dfs(target)

        ### 2. 递推
        dp = [1] + [0]*target
        for i in range(1,target+1):
            dp[i] = sum(dp[i-x] for x in nums if x<=i)
        return dp[-1]

# @lc code=end

