#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        不断扩大右窗口，当乘积大于等于k时，缩小左端点

        ** 注意trick：当k<=1时，一定是不存在解的，直接返回0
        
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if k <= 1:
            return 0
        ans = left = 0
        s = 1
        for right,x in enumerate(nums):
            s *= x
            while s >= k:
                s //= nums[left]
                left += 1
            ans += right-left+1
        return ans
# @lc code=end

