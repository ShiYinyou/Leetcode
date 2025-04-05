#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        动态规划-记忆化搜索
        先思考回溯的写法，然后改成记忆化搜索
        因为有很多重复计算的地方
        """
        ### 1. 回溯写法，会超时
        n = len(nums)
        ### 2. 在python中，最简单的记忆化就是使用cache装饰器
        ## 也可以用一个hashmap来统计
        ## cache装饰器本身就是将函数的输入和输出记入hashmap
        # @cache
        # def dfs(i):
        #     if i == -1:
        #         return 0
        #     if i == 0:
        #         return nums[0]
        #     return max(dfs(i-1),dfs(i-2)+nums[i])
        # return dfs(n-1)

        ### 3. 1:1翻译为递推
        ## 使用一个数组进行保存,将递归改为循环
        # f = [0]*(n+2)
        # for i,x in enumerate(nums):
        #     f[i+2] = max(f[i+1], f[i]+nums[i])
        # return f[-1]
    
        ### 4. 空间优化
        # 上面3的空间复杂度仍是O(n)，将其优化为O(1)
        # 根据递推数，0和1推出2，1和2推出3，2和3推出4……
        # 每个状态只与前两个状态相关
        f0 = f1 = 0
        for i in range(n):
            f0,f1 = f1,max(f1, f0+nums[i])
        return f1
        
# @lc code=end

# [104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]