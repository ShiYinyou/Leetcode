#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        0-1背包的模板
        设所有数之和为s，取+的数之和为p，则取-的数之和为s-p
        则添加符号后，和为p+(p-s) = 2p-s = target
        问题转化为在nums中找一些数，和为 p = (s+target)//2
        """
        s = sum(nums) - abs(target)
        if s<0 or s%2==1:
            return 0
        target = s//2 # 更新后的target，即p
        n = len(nums)
        ### 1. 两个数组：滚动数组
        # f = [[0]*(target+1) for _ in range(2)]
        # f[0][0] = 1
        # for i,x in enumerate(nums):
        #     for c in range(target+1):
        #         if c < x:
        #             f[(i+1)%2][c] = f[i%2][c]
        #         else:
        #             f[(i+1)%2][c] = f[i%2][c] + f[i%2][c-x]
        # return f[n%2][target]

        ### 2. 进一步优化空间为一个数组（逆序保证不覆盖）
        f = [0]*(target+1)
        f[0] = 1
        for x in nums:
            for c in range(target,x-1,-1):
                f[c] = f[c] + f[c-x]
        return f[target]
# @lc code=end

