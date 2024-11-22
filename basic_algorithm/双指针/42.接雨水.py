#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        前后缀分解 + 双指针
        基于前后缀分解的解法，用两个变量替代两个数组
        当左挡板小于右挡板时，雨水不可能从右边流出，只可能从左边流出
        此时将左挡板向内移动判断下一个位置

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        pre_max = suf_max = ans = 0
        left,right = 0, len(height)-1
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
# @lc code=end

