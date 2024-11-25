#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        要求从两端截取两个子数组，和等于x。
        反向思考，从中间取最长一个子数组，和等于sum-x

        两个小优化：
        1. 当target小于0时，一定没有解;
        2. target等于0时，解是全部元素

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        target = sum(nums)-x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        left = s = ans = 0
        for right,num in enumerate(nums):
            s += num
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans,right-left+1)
        return len(nums)-ans if ans!=0 else -1
# @lc code=end

