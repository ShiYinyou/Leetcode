#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        统计窗口中最多个k个0

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        cnt = ans = left = 0
        for right,x in enumerate(nums):
            if x == 0:
                cnt += 1
                while cnt > k:
                    if nums[left]==0:
                        cnt -= 1
                    left += 1
            ans = max(ans, right-left+1)
        return ans
# @lc code=end

