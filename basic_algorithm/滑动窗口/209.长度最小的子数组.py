#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        遍历每一个right，通过缩小左窗口寻找target

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        left = s = 0
        n = len(nums)
        ans = n+1
        for right,x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans,right-left+1)
                s -= nums[left]
                left += 1
        return ans if ans!=n+1 else 0
# @lc code=end

