#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        子集型回溯，每个数字选择+/-
        需要 @cache 减少时间开销

        时间复杂度：O(2^n)
        空间复杂度：O(n)
        """
        n = len(nums)
        ### @cache 可以大幅减少时间消耗，否则会超时
        @cache
        def dfs(i,s):
            if i == n:
                return 1 if s==target else 0
            ans = 0
            ans += dfs(i+1, s+nums[i])
            ans += dfs(i+1, s-nums[i])
            return ans
        return dfs(0,0)
# @lc code=end
## [1]\n1
## [5,16,45,7,20,5,32,38,43,14,29,11,2,25,36,28,27,26,45,45]\n17