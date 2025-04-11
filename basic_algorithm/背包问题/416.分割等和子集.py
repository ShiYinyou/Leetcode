#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2==1:
            return False
        target = s//2
        n = len(nums)
        f = [True] + [False]*target
        for x in nums:
            for c in range(target,x-1,-1):
                f[c] = f[c] or f[c-x]
        return f[target]

# @lc code=end

